import crypten
import torch
from mpc_linear_svm import train_linear_svm, evaluate_linear_svm

# Prepare data
dim_features = 100
num_train_examples = 1000
num_test_examples = 100
torch.manual_seed(1002)
features = torch.randn(dim_features, num_train_examples)
w_true = torch.randn(1, dim_features)
b_true = torch.randn(1)
labels = w_true.matmul(features).add(b_true).sign()
features_test = torch.randn(dim_features, num_test_examples)
labels_test = w_true.matmul(features_test).add(b_true).sign()

print(f'Training dataset contains {(labels==1).sum()} negative and {(labels==-1).sum()} negative samples')
print(f'Testing dataset contains {(labels_test==1).sum()} negative and {(labels_test==-1).sum()} negative samples')
print('features.dtype:', features.dtype)
print('labels.dtype:', labels.dtype)

features_alice = features[:40]
features_bob = features[40:]

torch.save(features_alice, 'features_alice.pth')
torch.save(features_bob, 'features_bob.pth')
torch.save(labels, 'labels.pth')
torch.save(features_test, 'features_test.pth')
torch.save(labels_test, 'labels_test.pth')

# Run training and testing using plaintext features and labels
crypten.init()
epochs = 10
lr = 3.0
w, b = train_linear_svm(features, labels, epochs=epochs, lr=lr)
evaluate_linear_svm(features_test, labels_test, w, b)
