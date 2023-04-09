"""
# 用途：参数量计算
"""

import torch.nn as nn

def count_parameters(model):
    res = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"count_training_parameters: {res}")
    res = sum(p.numel() for p in model.parameters())
    print(f"count_all_parameters:      {res}")

class Model(nn.Module):
    def __init__(self, num_inputs, num_hiddens, num_outputs):
        super().__init__()
        self.hidden = nn.Linear(num_inputs, num_hiddens)
        self.act = nn.ReLU()
        self.output = nn.Linear(num_hiddens, num_outputs)

    def forward(self, x):
        return self.output(self.act(self.hidden(x)))

if __name__ == '__main__':
    num_inputs = 100
    num_hiddens = 200
    num_outputs = 2
    num_ins = 2

    net = Model(num_hiddens=num_hiddens, num_outputs=num_outputs, num_inputs=num_inputs)

    count_parameters(net)

    
"""
# 样例输出
count_training_parameters: 20602
count_all_parameters:      20602
"""