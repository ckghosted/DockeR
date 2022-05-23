import crypten
import os
import yaml
import json
import pickle as pkl
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torchvision.transforms as torch_transforms

PATHS_DB = '/backup/jacob/flower_photos/'

def load_file(path):
    loader = {"yaml": yaml_load,
              "pkl": pkl_load,
              "json": json_load}
    ext = os.path.basename(path).split(".")[-1]
    if ext not in loader:
        raise RuntimeError("File extension is not supported by loader")
    return loader[ext](path)

def json_load(path):
    return json.load(open(path))

def yaml_load(path):
    return yaml.full_load(open(path))

def pkl_load(path):
    return pkl.load(open(path, "rb"))

class FlowerData(Dataset):
    DEFAULTS = {}
    def __init__(self, mode, config):
        self.__dict__.update(self.DEFAULTS, **config)
        split_fname = "split_{}_{}.json".format(self.train_frac, self.random_state)
        if not os.path.exists(os.path.join(PATHS_DB, split_fname)):
            raise RuntimeError("training/testing list {} does not exist, please run preprocess.py to make it".format(split_fname))
        split_dict = load_file(os.path.join(PATHS_DB, split_fname))
        self.examples = split_dict[mode]

        transforms = {"train": torch_transforms.Compose([
                                   torch_transforms.Resize(256),
                                   torch_transforms.RandomCrop(self.img_size),
                                   torch_transforms.RandomHorizontalFlip(),
                                   torch_transforms.ToTensor(),
                                   torch_transforms.Normalize((0.6959, 0.6537, 0.6371), (0.3113, 0.3192, 0.3214))
                               ]),
                      "test": torch_transforms.Compose([
                                  torch_transforms.Resize(256),
                                  torch_transforms.CenterCrop(self.img_size),
                                  torch_transforms.ToTensor(),
                                  torch_transforms.Normalize((0.6959, 0.6537, 0.6371), (0.3113, 0.3192, 0.3214))
                              ])
        }
        self.transforms = transforms[mode]
        
    def __len__(self):
        return len(self.examples)

    def __getitem__(self, index):
        img_path, label = self.examples[index]
        img = Image.open(img_path).convert("RGB")
        img = self.transforms(img)
        return img, label

class FlowerDataEnc(FlowerData):
    DEFAULTS = {}
    def __init__(self, mode, config, source):
        super(FlowerDataEnc, self).__init__(mode, config)
        self.source = source
        
    def __getitem__(self, index):
        img_path, label = self.examples[index]
        img = Image.open(img_path).convert("RGB")
        img = self.transforms(img)
        img_enc = crypten.cryptensor(img, src=self.source)
        label_enc = crypten.cryptensor(label, src=self.source)
        return img_enc, label_enc

def crypten_collate(batch):
    elem = batch[0]
    elem_type = type(elem)

    if isinstance(elem, crypten.CrypTensor):
        return crypten.stack(list(batch), dim=0)

    elif isinstance(elem, typing.Sequence):
        size = len(elem)
        assert all(len(b) == size for b in batch), "each element in list of batch should be of equal size"
        transposed = zip(*batch)
        return [crypten_collate(samples) for samples in transposed]

    elif isinstance(elem, typing.Mapping):
        return {key: crypten_collate([b[key] for b in batch]) for key in elem}

    elif isinstance(elem, tuple) and hasattr(elem, '_fields'):  # namedtuple
        return elem_type(*(crypten_collate(samples) for samples in zip(*batch)))

    return "crypten_collate: batch must contain CrypTensor, dicts or lists; found {}".format(elem_type)
