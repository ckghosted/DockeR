import crypten
from crypten import mpc
import crypten.communicator as comm
import torch
from mpc_linear_svm import train_linear_svm, evaluate_linear_svm

crypten.init()

party_names = ['alice', 'bob']
feature_dims = [40, 60]
rank = comm.get().get_rank()

# Aggregate training features
features_train = []
features_local = torch.load(f'features_{party_names[rank]}.pth')
for i, (name, dim) in enumerate(zip(party_names, feature_dims)):
    if i == rank:
        assert features_local.shape[0] == dim, \
                f"{name} feature dimension should be {dim}, but get {features_local.shape[0]}"
        features_enc = crypten.cryptensor(features_local, src=i)
    else:
        '''
        ## In tutorial 2
        - CrypTen follows the standard MPI programming model: it runs a separate process for each party,
          but each process runs an identical (complete) program.  
        - MPI protocols require that both processes to provide a tensor with the same size as their input.
          CrypTen ignores all data provided from non-source processes when encrypting.  
        '''
        features_dummy = torch.zeros((dim, features_local.shape[1]), dtype=torch.float32)
        features_enc = crypten.cryptensor(features_dummy, src=i)
    #print(f'i={i}')
    #print(f'Alice sees features_enc[:2,:2]: {features_enc[:2,:2]}')
    features_train.append(features_enc)
features = crypten.cat(features_train, dim=0)

# Load training labels
labels = torch.load('labels.pth')
labels = crypten.cryptensor(labels)

# Load testing data
features_test = torch.load('features_test.pth')
features_test = crypten.cryptensor(features_test)
labels_test = torch.load('labels_test.pth')
labels_test = crypten.cryptensor(labels_test)

# Inspect data
#print('Alice sees features.size():', features.size())
#print('Alice sees labels.size():', labels.size())
#print('Alice sees features_test.size():', features_test.size())
#print('Alice sees labels_test.size():', labels_test.size())

# Run training and testing
epochs = 10
lr = 3.0
w, b = train_linear_svm(features, labels, epochs=epochs, lr=lr)
evaluate_linear_svm(features_test, labels_test, w, b)
