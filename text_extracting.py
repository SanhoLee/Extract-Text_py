START_INDICATOR = '<coordinates>'
FINISH_INDICATOR = '</coordinates>'

temp=''

with open('original.xml','r') as f:
    while(START_INDICATOR not in temp):
        temp = f.readline()
        listed = [temp]
    while(FINISH_INDICATOR not in temp):
        temp = f.readline()
        listed.append(temp)
    with open('new_file.xml','w') as new_f:
        new_f.writelines(listed)
