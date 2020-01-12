#Ali Fahd, 101107270, SYSC 1005, Lab 4

from Cimpl import *
import random

image = load_image('great_big_c.jpg')


def red_channel(image):
   """ (Cimpl.Image) -> Cimpl.Image

   Returns a copy of image great_big_c.jpg where the blue and green
   components are zero and the red component unchanged.

   >>> red_filter = red_channel(image)
   >>> show(red_filter)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      g = 0
      b = 0
      new_color = create_color(r, g, b)
      set_color(new_image, x, y, new_color)
   return new_image

#Red is in the modified image


def green_channel(image):
   """ (Cimpl.Image) -> Cimpl.Image

   Returns a copy of image great_big_c.jpg where the red and blue
   components are zero and the green component unchanged.

   >>> green_filter = green_channel(image)
   >>> show(green_filter)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      r = 0
      b = 0
      new_color = create_color(r, g, b)
      set_color(new_image, x, y, new_color)
   return new_image

#Green is in the modified image


def blue_channel(image):
   """ (Cimpl.Image) -> Cimpl.Image

   Returns a copy of image great_big_c.jpg where the red and green
   components are zero and the blue component unchanged.

   >>> blue_filter = blue_channel(image)
   >>> show(blue_filter)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      r = 0
      g = 0
      new_color = create_color(r, g, b)
      set_color(new_image, x, y, new_color)
   return new_image

#Blue is in the modified image


def reduce_brightness(image, multiplier):
   """ (Cimpl.Image, multiplier) -> Cimpl.Image, float

   Returns a copy of image great_big_c.jpg where brightness of the image 
   has been reduced.

   >>> darker = reduce_brightness(image, 0.25)
   >>> show(darker)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      r = r*multiplier
      b = b*multiplier
      g = g*multiplier
      new_color = create_color(r, g, b)
      set_color(new_image, x, y, new_color)
   return new_image


def swap_red_blue(image):
   """ (Cimpl.Image) -> Cimpl.Image

   Returns a copy of image great_big_c.jpg where the red and blue
   components are swapped.

   >>> swapped = swap_red_blue(image)
   >>> show(swapped)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      old_r = r
      r = b
      b = old_r
   
      new_color = create_color(r, g, b)
      set_color(new_image, x, y, new_color)
   return new_image


def hide_image(image):
   """ (Cimpl.Image) -> Cimpl.Image

   Returns a copy of image great_big_c.jpg where the image
   is hidden.

   >>> hidden = hide_image(image)
   >>> show(hidden)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      r = ((r+g+b)/3)/10
      g = random.randint(0, 255)
      b = random.randint(0, 255)
   
      new_color = create_color(r, g, b)
      set_color(new_image, x, y, new_color)
   return new_image


def recover_image(image):
   """ (Cimpl.Image) -> Cimpl.Image

   Returns a copy of image great_big_c.jpg where the image
   is recovered from the hidden function.

   >>> recover = recover_image(image)
   >>> show(recover)
   """    
   new_image = copy(image)
   for x, y, (r, g, b) in image:
      r = r*10-g-b
   
      new_color = create_color(r, 0, 0)
      set_color(new_image, x, y, new_color)
   return new_image