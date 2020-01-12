""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""
import math
import random

from Cimpl import *

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a weighted grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = weighted_grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r*0.299 + g*0.587 + b*0.114)
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def extreme_contrast(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image, maximizing the contrast between
    the light and dark pixels.
   
    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        if r <= 127:
            r = 0
        else:
            r = 255
            
        if g <= 127:
            g = 0
        else:
            g = 255
                
        if b <= 127:
            b = 0
        else:
            b = 255        
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        contrast = create_color(r, g, b)
        set_color(new_image, x, y, contrast)
        
    return new_image


def sepia_tint(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of image, maximizing the contrast between
    the light and dark pixels.
   
    >>> image = load_image(choose_file())
    >>> newer_image = sepia_tint(image)
    >>> show(newer_image)
    """
    new_image = copy(image)
    
    gray_image = weighted_grayscale(new_image)
    
    for x, y, (r, g, b) in gray_image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        if r < 63: 
            r = r*1.1 
            b = b*0.9

        elif r <= 191 and r >= 63:
            r = r*1.15
            b = b*0.85
           
        else:
            r = r*1.08
            b = b*0.93
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        contrast = create_color(r, g, b)
        set_color(gray_image, x, y, contrast)
        
    return gray_image

def _adjust_component(amount):
    """ (int) -> int
   
    >>> _adjust_component(10)
    >>> _adjust_component(85)
    >>> _adjust_component(142)
    >>> _adjust_component(230)

    """

        #Divide the range 0..255 into 4 equal-size quadrants,
        #and return the midpoint of the quadrant in which the
        #specified amount lies.

    range = 255 / 4
        
    if amount <= range:
            amount = 31
    elif amount > range and amount <= range*2:
            amount = 95
    elif amount > range*2 and amount <= range*3:
            amount = 159
    elif amount > range*3 and amount <= range*4:
            amount = 223
            
    return amount


def posterize(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Returns a "posterized" copy of image.

    >>>  image = load_image(choose_file())
    >>> new_image = posterize(image)
    >>> show(new_image)
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
         
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        

        # create_color will convert an argument of type float to an int
        
        contrast = create_color(r, g, b)
        set_color(new_image, x, y, contrast)
        
    return new_image




#Lab 6 Functions


def detect_edges(image, threshold):
    
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    
    #Goes through each pixel
    for y in range(0, get_height(new_image) -1):
        for x in range(0, get_width(new_image)):
            
            r, g, b = get_color(new_image, x, y)
            
            brightness_top = (r + g + b) // 3
            
            r, g, b = get_color(new_image, x, y+1)
            brightness_bottom = (r + g + b) // 3
            
            brightness = abs(brightness_top - brightness_bottom)
            
            #Creates contrast
            if brightness > threshold:
                contrast = create_color(0, 0, 0)
                set_color(new_image, x, y, contrast)
            else:
                contrast = create_color(255, 255, 255)
                set_color(new_image, x, y, contrast) 
                
    return new_image




def detect_edges_better(image, threshold):
    
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges_better(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    
    #Goes through each pixel
    for y in range(0, get_height(new_image) -1):
        for x in range(0, get_width(new_image) -1):
            
            r, g, b = get_color(new_image, x, y)
            
            brightness_top = (r + g + b) // 3
            
            r, g, b = get_color(new_image, x, y+1)
            brightness_bottom = (r + g + b) // 3
            
            r, g, b = get_color(new_image, x+1, y)
            brightness_right = (r + g + b) // 3            
            
            brightness1 = abs(brightness_top - brightness_bottom)
            brightness2 = abs(brightness_top - brightness_right)
            
             #Creates contrast
            if brightness1 > threshold or brightness2 > threshold:
                contrast = create_color(0, 0, 0)
                set_color(new_image, x, y, contrast)
            else:
                contrast = create_color(255, 255, 255)
                set_color(new_image, x, y, contrast) 
                
    return new_image






def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    for y in range(1, get_height(image) -1):
        for x in range(1, get_width(image) -1):

            # Grab the pixel @ (x, y) and its eight neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            
            top_right_red, top_right_green, top_right_blue = get_color(image, x+1, y - 1)
            top_left_red, top_left_green, top_left_blue = get_color(image, x-1, y - 1)
            bottom_right_red, bottom_right_green, bottom_right_blue = get_color(image, x+1, y + 1)
            bottom_left_red, bottom_left_green, bottom_left_blue = get_color(image, x-1, y + 1)

            # Average the red components of the nine pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + top_right_red + top_left_red + bottom_right_red + bottom_left_red) // 9

            # Average the green components of the nine pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green + top_right_green + top_left_green + bottom_right_green + bottom_left_green ) // 9

            # Average the blue components of the nine pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue + top_right_blue + top_left_blue + bottom_right_blue + bottom_left_blue ) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target





def flip_vertical(image):
    
    """ (Cimpl.Image) -> Cimpl.Image
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary vertical line
    drawn through its midpoint.
    >>> image = load_image(choose_file())
    >>> filtered = flip_vertical(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    
    for y in range(1, get_height(image) -1):
        for x in range(1, get_width(image) -1):
            
            r, g, b = get_color(image, (get_width(image) -1)-x, y)
            
            flip = create_color(r, g, b)
            set_color(new_image, x, y, flip)
    
    return new_image





def flip_horizontal(image):
    
    """ (Cimpl.Image) -> Cimpl.Image
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary horizontal line
    drawn through its midpoint.
    >>> image = load_image(choose_file())
    >>> filtered = flip_horizontal(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    
    for y in range(1, get_height(image) -1):
        for x in range(1, get_width(image) -1):
            
            r, g, b = get_color(image, x, get_height(image)-y)
            
            flip = create_color(r, g, b)
            set_color(new_image, x, y, flip)
    
    return new_image






def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> image = load_image(choose_file())
    >>> scattered = scatter(image)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in new_image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(-10, 11)
            rand2 = random.randint(-10, 11)
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = x+rand1
            random_row = y+rand2
            
            # Determine if the random coordinates are in bounds.

            if random_column >=0 and random_row >= 0 and random_column < (get_width(image)) and random_row < (get_height(image)):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        new_color = get_color(image, random_column, random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, new_color)
                    
    # Return the scattered image.
    return new_image