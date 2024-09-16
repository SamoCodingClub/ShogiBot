import requests
import csv
home = "https://japanesechess.org/gsdb/index.php?collection="
collection = ["meijin","ryu_o", "kisei", "oi", "oza","kio", "ginga","junisen","zen_nihon_pro","belgian_championships", "colmar"] # add more from https://japanesechess.org/gsdb/ eventually
database = []
file = "database.csv"
for c in collection:
    count = 1
    print(c)
    url = home+c+"&index="+str(count)
    boolean_value = True
    while boolean_value:
        r = requests.get(url).text
        if "White_grade" in r: #test all of this eventually probably
            print(r.split("Proam")[1].split(">")[1].split("<")[0].split()[-1])
            if r.split("Result \"")[1].split("\"")[0] == "1-0":
                winner  = -1 #black won
            elif r.split("Result \"")[1].split("\"")[0] == "0-1":
                winner = 1
            elif r.split("Result \"")[1].split("\"")[0] == "1/2-1/2":
                winner = 0
            elif "~" in r.split("Proam")[1].split(">")[1].split("<")[0]: #sometimes they are messed up:
                print("Why did they do this")
                count+=1
                url = url.split("&")[0] + str("&") + "index=" + str(count)
                continue
            elif r.split("Proam")[1].split(">")[1].split("<")[0].split()[-1] == "{Resigns}": #sometimes its not there
                if len(r.split("Proam")[1].split(">")[1].split("<")[0].split()) % 2 == 0:   
                    winner = -1
                else:
                    winner = 1
            elif r.split("Proam")[1].split(">")[1].split("<")[0].split()[-1] == "{Sennichite}" or r.split("Proam")[1].split(">")[1].split("<")[0].split()[-1] == "{Jishogi}": #checks for ties
                winner =0
            else:
                count+=1
                url = url.split("&")[0] + str("&") + "index=" + str(count)
                continue
            database.append([r.split("Proam")[1].split(">")[1].split("<")[0].split(), winner])

        else:
            boolean_value = False 
        count += 1
        print(count)
        url = url.split("&")[0] + str("&") + "index=" + str(count)
print(database)
f = open(file, "w", newline="")
csv_f = csv.writer(f)
for d in database:
    csv_f.writerow(database)