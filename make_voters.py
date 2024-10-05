import torch
import torch.utils.data
from torch import nn
import pathlib
import pandas as pd
import random
import itertools
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
class Empty:
	def __init__(self):
		self.color = 0
		self.__class__.__name__ = " "
class Board: #should import fom shogi_game but have to control code in there so that it doesnt run on import. will do later.

    def __init__(self, array, string):
        self.array = array
        self.string = string
        self.p1 = []
        self.p2 = []

    def set(self, string): #does not load hands
            self.array = [["." for y in range(9)] for x in range(9)]
            input_arr = string.split("/")
            for entry in input_arr:
                try:
                    self.array[int(entry[0])][int(entry[1])] = entry[2]
                except:
                    print("There was an error with setting the board. The issue was with:", entry)
#note to self to make sure lowercase is black. no biggie if not tho
model = cnn()
num_epochs = 5
optimizer = torch.optim.Adam(model.parameters(), lr = 0.002)
loss = nn.CrossEntropyLoss()
batch_size_idkifimadethisavariablealreadysonowitsreallylong = 1000
test_dataset = []
for numberoftimesthishappens in range(int(sum(1 for _ in open('./games_I_think'))/batch_size_idkifimadethisavariablealreadysonowitsreallylong)):
    data = []
    with open("./games_I_think", "r") as f: #games don't include ties rn idk why that is. will fix later. so don't spend too much time training on potentially wrong data
        for line in itertools.islice(f, numberoftimesthishappens*batch_size_idkifimadethisavariablealreadysonowitsreallylong,(numberoftimesthishappens*batch_size_idkifimadethisavariablealreadysonowitsreallylong)+batch_size_idkifimadethisavariablealreadysonowitsreallylong):
            data.append(line)
    #print(data)
    data = pd.DataFrame(data)
    #int(sum(1 for _ in open('./games_I_think'))/1000)
    #board.set("data")
    #board.print()
    bigarray = []
    smallarray = []
    pieces = ["p", "n", "l", "g", "k", "s", "r", "b", "h", "d"]

    for pieceofdata in data.index:
        board = Board([], "") #why do we change from board array to the set stuff just to change it back later. This is dumb, but i guess its fine for now.
        moves = data[0][pieceofdata].split("^")[0]
        hand = data[0][pieceofdata].split("^")[1]
        hand1 = []
        hand2 = []
        winner = data[0][pieceofdata].split("^")[1][-3:-1]
        if "-1" in winner:
            winner = -1
        elif "1" in winner:
            winner = 1
        elif "0" in winner:
            winner = 0
        smallarray.append(winner)
        board.set(moves[:-1])
        arr = [[[0 for b in range(9)]for a in range(9)] for c in range(48)] #this looks funny
        for i,y in enumerate(board.array): #clean this code up later, but it gets the pieces in the array
            for z,x in enumerate(y):
                if x != ".":
                    p = board.array[i][z]
                    if p[0].isupper():
                        arr[pieces.index(p.lower())][i][z] = 1
                    else:
                        arr[pieces.index(p) + 10][i][z] = 1
        if "!" in hand: #this is because of dumb decisions
            hand1 = hand[1:]
            hand1 = hand1.split("&")[0]
            hand1 = hand1.split("/") #THIS HAS EMPTY SPOTS IN THE LIST

        if "?" in hand:
            hand2 = hand[hand.index("?")+1:]
            hand2 = hand2.split("@")[0]
            hand2 = hand2.split("/")
        for x in hand1: 
            if x != "":
                for w in range(9):
                    for e in range(4):
                        arr[pieces.index(x.lower())+20][w][e] = 1 
                q = hand1.pop(hand1.index(x)) #i just wrote code probably check later
                if q in hand1:
                    for r in range(9):
                        for t in range(5):
                            arr[pieces.index(p.lower())+20][w][e] = 1
        for x in hand2:
            if x != "":
                for w in range(9):
                    for e in range(4):
                        arr[pieces.index(x.lower())+20][w][e] = 1
                q = hand2.pop(hand2.index(x))
                if q in hand2:
                    for r in range(9):
                        for t in range(5):
                            arr[pieces.index(p.lower())+20][w][e] = 1
        bigarray.append(arr)
    bigarray = pd.DataFrame(bigarray)
    smallarray = pd.DataFrame(smallarray)
    #print(smallarray)
    #print(bigarray)
    bigarray[48] = smallarray
    
    data = bigarray
    
    data = pd.DataFrame(data)
    #data["winner"] = data.iloc[:, -1:]
    #print(data)
    #print(data) 
    #was working on downsampling, but it might not do anything because of further resarch showing that black actually doesn't have an advantage will leave as comment for now
    """
    major = data[data.columns[-1]].sum()
    if major ==
    df_min = data.loc[data[48] == 1] #white wins
    #print(len(df_min))
    df_maj = data.loc[data[48] == -1]
    #print(df_maj) #             this is my favorite comment by far ↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    while len(df_maj) > len(df_min): #downsampling, but this is going to gerrymander when i turn it into batches so probably find a better way to do it. 
        r = random.randrange(0, len(df_maj) -1)
        df_maj[r].drop
    data = pd.concat([df_maj, df_min], ignore_index = True)
    """
    #print("got this far")
    print(data)
    finTensor = torch.Tensor(data.columns[-1])
    #print(finTensor)
    y = torch.Tensor(data.columns[:-1]) #this is all dumb fix later
    data = torch.utils.data.TensorDataset(finTensor,y)
    print(data)
    trains,tests=(torch.utils.data.random_split(data,[int(len(data)*0.8),len(data)-int(len(data)*0.8)])) #idk why I didn't just use variables for this. I will probably clean it up later
    train_loader = torch.utils.data.DataLoader(trains, batch_size=200, shuffle=True, drop_last = True)
    test_dataset.append(tests)
    print(len(train_loader))
    for epoch in range(num_epochs):
        #print("here")
        train_batch = iter(train_loader)
        for inputs, targets in train_batch:
            print("over here")
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
test_dataset = [str(x) for x in test_dataset]
with open("testing", "w") as f:
	f.writelines(test_dataset)

