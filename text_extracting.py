temp=''

with open('original.xml','r') as f:
    while('<coordinates>' not in temp):
        temp = f.readline()
        listed = [temp]
    
    while('world' not in temp):
        temp = f.readline()
        listed.append(temp)

    with open('new_file.xml','w') as new_f:
        new_f.writelines(listed)
