import os, shutil
path = r"C:/Users/19544/OneDrive/Desktop/BeyonceK/"
file_name = os.listdir(path)
folder_titles = ['XLSX Files', "Pics", "Text Files"]

for loop in range(0,3):
    if not os.path.exists(path + folder_titles[loop]):
        print(path + folder_titles[loop])
        os.makedirs(path + folder_titles[loop])

for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "XLSX Files/" + file):
        shutil.move(path + file, path + "XLSX Files/" + file)
    elif ".png" in file and not os.path.exists(path + "Pics/" + file):
        shutil.move(path + file, path + "Pics/" + file)
    elif ".txt" in file and not os.path.exists(path + "Text Files/" + file):
        shutil.move(path + file, path + "Text Files/" + file)



#File Explorer Organizer

