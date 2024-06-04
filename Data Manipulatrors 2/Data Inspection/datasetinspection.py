import cv2
import os
import random
import numpy as np
import time

def visualizer(image_path, label_path):
    #Listing all the images of the image directory.
    files = os.listdir(image_path)
    #Picking up a random image.
    random_image = random.choice(files)
    #Getting the path of the random image.
    imagerandom_path=os.path.join(image_path,random_image)
    #Reading the image using cv2.
    r_image=cv2.imread(imagerandom_path)
    #Getting the name of the corresponding text file of the image.
    text_file=random_image.rstrip('.jpg')+'.txt'
    #Getting the path of the text file.
    text_file_path=os.path.join(label_path,text_file)
    #Recording the class names for future use.
    names=['Elephant','Tiger','Person','Buffalo']
    #Reading the text file line by line.
    with open(text_file_path,'r') as f:
        annotations=f.readlines()
    #Iterating over each annotations.
    for annotation in annotations:
        #Taking the list of values for each annotation.
        anootation_list=annotation.split()
        #Converting the yolo data format into cv2 format.
        x_min = int(np.floor((float(anootation_list[1]) - float(anootation_list[3]) / 2) * 640))
        y_min = int(np.floor((float(anootation_list[2]) - float(anootation_list[4]) / 2) * 640))
        x_max = int(np.ceil((float(anootation_list[1]) + float(anootation_list[3]) / 2) * 640))
        y_max = int(np.ceil((float(anootation_list[2]) + float(anootation_list[4]) / 2) * 640))
        #Drawing the bounding box around the object.
        cv2.rectangle(r_image, (x_min, y_max), (x_max, y_min), (255, 0, 0), 1)
        #writing the class of the object.
        cv2.putText(r_image, str(names[int(anootation_list[0])]), (x_min,y_max - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    #Saving the output to Output.jpg
    cv2.imwrite('Output.jpg',r_image)
if __name__=="__main__":
    #Loop to read and annotate the data iteratively.
    while True:
        visualizer(image_path=r"C:\Users\quadt\OneDrive\Desktop\Data_for_training_03.6.24\train\images", label_path=r"C:\Users\quadt\OneDrive\Desktop\Data_for_training_03.6.24\train\labels")
        #Sleeping the time for three seconds for better readability of classes and boxes.
        time.sleep(3)
