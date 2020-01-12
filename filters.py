""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""

from Cimpl import *

image = load_image('great_big_c.jpg')

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
    
    Return a grayscale copy of image.
   
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