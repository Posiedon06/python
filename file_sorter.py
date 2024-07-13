import os, shutil
path= r"C:/Users/Aryan Chowdhury/OneDrive/Desktop/python/"
file_name= os.listdir(path)
#print("file_name")
folder_name = ["csv files","image files", "text files","pdf files"]

for i in range(4):
    if not os.path.exists(path + folder_name[i]):
        print(path + folder_name[i] )
        os.makedirs(path + folder_name[i])
for file in file_name:
    if file.endswith(".csv"):
        shutil.move(path + file, path + "csv files/" + file)
    elif file.endswith(".png") :
        shutil.move(path + file, path + "image files/" + file) 
    elif file.endswith(".pdf"):
        shutil.move(path + file, path + "pdf files/" + file)
    elif file.endswith(".txt"):
        shutil.move(path + file, path + "text files/" + file)



