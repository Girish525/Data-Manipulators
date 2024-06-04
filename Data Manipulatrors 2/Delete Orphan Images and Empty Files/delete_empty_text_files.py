import os

label_path=r"D:\Project Periyar-Final\Dataset 3Jun24\valid\labels"

text_file_paths=[]
empty_files=[]
i=0

text_files = [file for file in os.listdir(label_path)]
for text_file in text_files:
    text_file_paths.append(os.path.join(label_path,text_file))
for text_file_path in text_file_paths:
    with open(text_file_path,'rb') as f:
        if len(f.read())==0:
            empty_files.append(text_file_path)
print(len(empty_files))

for empty_file in empty_files:
    os.remove(empty_file)
    i+=1
print(f"Removed {i} empty files.")
