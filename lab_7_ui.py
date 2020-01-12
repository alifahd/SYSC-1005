# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from lab_7_filters import *
import sys

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().


def choose():
    print ("L)oad image\nN)egative  G)rayscale  S)olarize   2)-tone  3)-tone\nQ)uit")
    prompt = (": ")    
    command = input(prompt)
    image_selected = False
    
    while True:  
        
        if command in ["L", "Q", "N", "G", "S", "2", "3"]:
            if command == "L":
                image = get_image()
                image_selected = True
            if image_selected == True:
                if command == "N":
                        image = negative(image)
                        show(image)
                elif command == "G":
                        image = grayscale(image)
                        show(image)        
                elif command == "S":
                    prompt_threshold = ("Threshold? (0 - 256): ")
                    threshold = int(input(prompt_threshold))
                    while threshold > 256 or threshold < 0:
                        print("Out of range, enter a threshold:")
                        prompt_threshold = ("Threshold? (0 - 256): ")
                        threshold = int(input(prompt_threshold))
                    image = solarize(image, threshold)
                    show(image)          
                elif command == "2":
                        image = black_and_white(image)
                        show(image)          
                elif command == "3":
                        image = black_and_white_and_gray(image)
                        show(image)          
                elif command == "Q":
                    sys.exit()
            else:
                print("No image loaded")
        else:
            print("No such command")
            
        print ("\nL)oad image\nN)egative  G)rayscale  S)olarize   2)-tone  3)-tone\nQ)uit")
        prompt = (": ")    
        command = input(prompt)            
        
        
      
        
if __name__ == "__main__":
    img = choose()
    show(img)


    