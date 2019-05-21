import json

t1 = open("indicator.json")
elms = json.loads(t1.read())


def headAdding(text):
    with open(text, 'a') as f1:
        f1.writelines('<?xml version="1.0" encoding="" ?>\n')
        f1.writelines("<Solver>\n")

def extractContent(original, newfile, initial, finish):
    temp = ''
    with open(original, 'r') as f:
        while(initial not in temp):
            temp = f.readline()
            listed = [temp]
        while(finish not in temp):
            temp = f.readline()
            listed.append(temp)
        with open(newfile, 'a') as f1:
            f1.writelines(listed)
            f1.writelines("</xxx_Solver>\n")

def filteredData(original, newfile, initial, finish):
    temp=''
    listed_all=[]

    with open(original,'r') as f2:
        while(1):
            temp=f2.readline()
            if(initial in temp):
                break
            listed_all.append(temp)

    temp=''
    listed_after=[]
    with open(original,'r') as f3:
        while(finish not in temp):
            temp = f3.readline()
        while(temp != ''):
            temp = f3.readline()
            listed_after.append(temp)

    listed_all.extend(listed_after)
    return listed_all

for i in range(len(elms)):
    print("Stating Process :", i)
    headAdding(elms[i]["TARGET_FILE"])
    print("Head Addede :", i)
    extractContent(
        original=elms[0]["ORIGINAL_FILE"],
        newfile=elms[i]["TARGET_FILE"],
        initial=elms[i]["INITIAL_INDICATOR"],
        finish=elms[i]["FINISH_INDICATOR"]
    )
    print("Extracted ! :", i)
    listed_all = filteredData(
        original=elms[0]["ORIGINAL_FILE"],
        newfile=elms[i]["TARGET_FILE"],
        initial=elms[i]["INITIAL_INDICATOR"],
        finish=elms[i]["FINISH_INDICATOR"]
    )
    print("after Extracted process done, list up : ",i)
    with open(elms[0]["ORIGINAL_FILE"], 'w') as f4:
        f4.writelines(listed_all)
    print("Rewrite original file ! :", i)