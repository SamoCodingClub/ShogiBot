import torch
from torch import nn
import pathlib
import pandas as pd
import random
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
class cnn(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Conv2d(48,20,kernel_size = (10, 3, 3)) #idk if this is any good but we will see
        self.r = nn.ReLU()
        self.m = nn.MaxPool2d(2,2) #this architecture is def messed up will fix later
        self.fc2 = nn.Conv2d(20, 2, 2)
        self.l1 = nn.Linear(16 * 5 * 5, 120)
        self.l2 = nn.Linear(120, 84)
    def forward(self, board): #board is going to be 9x9(board dimensions) x48 (pieces + in hand). This is probably a bad way to do this but we will see
        a = self.fc1(board)
        a = self.r(a)
        a = self.m(a)
        a = self.m(self.fc2(a))
        a = self.r(a)
        a = self.l2(self.l1(a))
        return a
class Board: #should import fom shogi_game but have to control code in there so that it doesnt run on import. will do later.

    def __init__(self, array, string, p1, p2):
        self.array = array
        self.string = string
        self.p1 = p1
        self.p2 = p2

    def set(self, string):
        self.array = [[Empty() for y in range(9)] for x in range(9)]
        input_arr = string.split("/")
        for entry in input_arr:
            try:
                if entry.islower():
                    color = -1
                else:
                    color = 1
                entry = entry.lower()
                if "p" in entry: 
                    self.array[int(entry[0])][int(entry[1])] = Pawn(
                        color, int(entry[0]), int(entry[1]))
                elif "k" in entry:
                    self.array[int(entry[0])][int(entry[1])] = King(
                        color, int(entry[0]), int(entry[1]))
                elif "s" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Silver_General(
                        color, int(entry[0]), int(entry[1]))
                elif "r" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Rook(
                        color, int(entry[0]), int(entry[1]))
                elif "b" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Bishop(
                        color, int(entry[0]), int(entry[1]))
                elif "g" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Gold_General(
                        color, int(entry[0]), int(entry[1]))
                elif "n" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Knight(
                        color, int(entry[0]), int(entry[1]))
                elif "l" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Lance(
                        color, int(entry[0]), int(entry[1]))
            except:
                print(
                    "There was an error with setting the board. The issue was with:",
                    entry)
#note to self to make sure lowercase is black. no biggie if not tho
model = cnn()
num_epochs = 5
optimizer = torch.optim.Adam(model.parameters(), lr = 0.002)
loss = nn.CrossEntropyLoss()
test_dataset = []
for numberoftimesthishappens in range(int(sum(1 for _ in open('./games_I_think'))/1000)):
    file = open('./games_I_think') #games don't include ties rn idk why that is. will fix later. so don't spend too much time training on potentially wrong data
    data = pd.DataFrame(file)
    print(data)
    #int(sum(1 for _ in open('./games_I_think'))/1000)
    #board.set("data")
    #board.print()
    bigarray = []
    smallarray = []
    pieces = ["p", "n", "l", "g", "k", "s", "r", "b", "h", "d"]
    for pieceofdata in data:
        board = Board([], "", 0) #why do we change from board array to the set stuff just to change it back later. This is dumb, but i guess its fine for now.
        moves = pieceofdata.split("^")[0]
        hand = pieceofdata.split("^")[1]
        hand1 = []
        hand2 = []
        winner = pieceofdata.split("^")[:-2]
        if "/" in winner:
            winner = winner[1]
        smallarray.append(winner)
        board.set(moves[:-1])
        arr = [[[0 for b in range(9)]for a in range(9)] for c in range(48)] #this looks funny
        for i,y in enumerate(board.array): #clean this code up later, but it gets the pieces in the array
            for z,x in enumerate(y):
                if x.color != 0:
                    p = board.array[i][z].__class__.__name__
                    if p[0].isupper():
                        arr[pieces.index(p)][i][z] = 1
                    else:
                        arr[pieces.index(p) + 10][i][z] = 1
        if "!" in hand: #this is because of dumb decisions
            hand1 = hand.split("&")[0]
            hand1 = hand.split("/")
        if "?" in hand:
            hand2 = hand.split("@")[0]
            hand2 = hand.split("/")
        for x in hand1:
            for w in range(9):
                for e in range(4):
                    arr[pieces.index(x)+20][w][e] = 1
            q = hand1.pop(hand1.index(x)) #i just wrote code probably check later
            if q in hand1:
                for r in range(9):
                    for t in range(5):
                        arr[pieces.index(p)+20][w][e] = 1
        for x in hand2:
            for w in range(9):
                for e in range(4):
                    arr[pieces.index(x)+20][w][e] = 1
            q = hand2.pop(hand2.index(x))
            if q in hand2:
                for r in range(9):
                    for t in range(5):
                        arr[pieces.index(p)+20][w][e] = 1
        bigarray.append(arr)
    data = pd.concat([bigarray, smallarray], ignore_index = False)
    data["winner"] = data.iloc[:, -1:]
    df_min = data[data["winner"] == 1] #white wins
    df_maj = data[data["winner"] == -1]
    print(len(df_maj)) #             this is my favorite comment by far ↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    while len(df_maj) > len(df_min): #downsampling, but this is going to gerrymander when i turn it into batches so probably find a better way to do it. 
        r = random.randrange(0, len(df_maj) -1)
        df_maj[r].drop
    data = pd.concat([df_maj, df_min], ignore_index = True)
    finTensor = torch.Tensor(data.iloc[:,:-1])
    y = torch.Tensor(data.iloc[:,-1:])
    data = data_utils.TensorDataset(finTensor,y)
    trains,tests=(torch.utils.data.random_split(data,[int(len(data)*0.8),len(data)-int(len(data)*0.8)])) #idk why I didn't just use variables for this. I will probably clean it up later
    train_loader = data_utils.DataLoader(trains, batch_size=200, shuffle=True, drop_last = True)
    test_dataset.append(tests)
    
    for epoch in range(num_epochs):
        train_batch = iter(train_loader)
        for inputs, targets in train_batch:
            inputs = inputs.to(device)
            targets = targets.to(device)
            model.train()
            model.to(device)
            guess = model(inputs)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_fn(outputs, targets)
            loss.backward()
            optimizer.step()
            print(loss)
    torch.save(model.state_dict(), str(numberoftimesthishappens)+ "badnn.pt")
with open("testing", r) as f:
	f.writelines(test_dataset)

