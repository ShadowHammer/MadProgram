import os

directory_list = list()
x = str("C:/Users/Tobias/source/repos/Mad Program v2/Mad Program v2/Retter/Desserter")
for root, dirs, files in os.walk(x, topdown=False):
    for name in dirs:
        
        #print(y)
        directory_list.append(os.path.join(root, name))

print (directory_list)

root=x

