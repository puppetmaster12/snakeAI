import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
    # Initializing the model and the layers
    # Network currently has only one hidden layer
    def __init__(self, input_size, hidden_size, output_size):
        super.__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    # Feedforward function of each layer
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)

        return x

    def save(self, file_name='model.pth'):
        pass