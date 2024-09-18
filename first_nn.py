import torch
#setup data here
class deepish(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(9*9*14,350)
        self.r = nn.ReLu()
        self.fc2 = nn.Linear(350, 800)
        self.fc3 = nn.Linear(800, 2)
    def forward(self, board): #board is probably going to be 9x9x14 for rn will make better with the next model
        a = self.fc1(board)
        a = self.r(a)
        a = self.fc2(a)
        a = self.r(a)
        a = self.fc3(a)
        return a
model = deepish()
num_epochs = 5
optimizer = torch.optim.Adam(model.parameters(), lr = 0.002)
loss = nn.CrossEntropyLoss()
#training stuff here
for epoch in range(num_epochs):
    pass


