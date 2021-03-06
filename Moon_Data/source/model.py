import torch
import torch.nn as nn
import torch.nn.functional as F

## TODO: Complete this classifier
class SimpleNet(nn.Module):
    
    ## TODO: Define the init function
    def __init__(self, input_dim, hidden_dim, output_dim):
        '''Defines layers of a neural network.
           :param input_dim: Number of input features
           :param hidden_dim: Size of hidden layer(s)
           :param output_dim: Number of outputs
         '''
        super(SimpleNet, self).__init__()
        
        # https://cs230-stanford.github.io/pytorch-getting-started.html   good reference
        # define all layers, here **AMIRI**
        self.linear1 = nn.Linear(input_dim, hidden_dim) 
        self.linear2 = nn.Linear(hidden_dim, output_dim)
        self.drop = nn.Dropout(0.3)
        #sigmoid layer
        self.sig = nn.Sigmoid()
    
    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        '''Feedforward behavior of the net.
           :param x: A batch of input features
           :return: A single, sigmoid activated value
         '''
        # your code, here
        out = F.relu(self.linear1(x)) # activation of hidden layer
        out = self.drop(out)
        out = self.linear2(out)
        return self.sig(out) # returning class score