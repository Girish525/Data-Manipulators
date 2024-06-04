import os

image_path=r"D:\Project Periyar-Final\Dataset 3Jun24\valid\images"
label_path=r"D:\Project Periyar-Final\Dataset 3Jun24\valid\labels"

image_file_paths=[]
label_file_paths=[]
orphan_images=[]
i=0

image_files = [file.rstrip(".jpg") for file in os.listdir(image_path)]
label_files=[file.rstrip(".txt") for file in os.listdir(label_path)]


for image_file in image_files:
    if image_file not in label_files:
        os.remove(os.path.join(image_path,image_file+".jpg"))
        i+=1
print(f"Number of orphan images removed:{i}")
    


