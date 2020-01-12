# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from filters import *
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
    print ("L)oad image\nB)lur  E)dge detect  P)osterize   S)catter  T)int sepia\nW)eighted grayscale  X)treme contrast\nQ)uit")
    prompt = (": ")    
    command = input(prompt)
    image_selected = False
    
    while True:  
        
        if command in ["L", "Q", "B", "E", "P", "S", "T", "W", "X"]:
            if command == "L":
                image = get_image()
                image_selected = True
            if image_selected == True:
                if command == "B":
                        image = blur(image)
                        show(image)
                elif command == "E":
                    prompt_threshold = ("Threshold? (0 - 256): ")
                    threshold = int(input(prompt_threshold))
                    while threshold > 256 or threshold < 0:
                        print("Out of range, enter a threshold:")
                        prompt_threshold = ("Threshold? (0 - 256): ")
                        threshold = int(input(prompt_threshold))                    
                    image = detect_edges_better(image, threshold)
                    show(image)        
                elif command == "P":
                    image = posterize(image)
                    show(image)          
                elif command == "S":
                        image = scatter(image)
                        show(image)          
                elif command == "T":
                        image = sepia_tint(image)
                        show(image)
                elif command == "W":
                        image = weighted_grayscale(image)
                        show(image)    
                elif command == "X":
                        image = extreme_contrast(image)
                        show(image)                            
                elif command == "Q":
                    sys.exit()
            else:
                print("No image loaded\n")
        else:
            print("No such command\n")
            
        print ("L)oad image\nB)lur  E)dge detect  P)osterize   S)catter  T)int sepia\nW)eighted grayscale  X)treme contrast\nQ)uit")
        prompt = (": ")    
        command = input(prompt)            
        
        
      
        
if __name__ == "__main__":
    img = choose()
    show(img)


    