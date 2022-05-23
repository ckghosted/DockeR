import json, os

a = json.load(open('split_0.8_1002.json', 'r'))
b = [[os.path.join(sample[0].split('/')[-3], sample[0].split('/')[-2], sample[0].split('/')[-1]), sample[1]] for sample in a['test']]
c = {'test': b}

with open('split.json', 'w') as f:
    json.dump(c, f)
