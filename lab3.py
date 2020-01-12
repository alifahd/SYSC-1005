import math 
 
def area_of_disk(radius):     
    """ (number) -> float 
 
    Return the area of a ring with the specified      
    non-negative radius. 
 
    >>> area_of_disk(2.0)     
    12.57     
    """     
    return math.pi * radius ** 2 
 
def area_of_ring(outer, inner):     
    """ (number, number) -> float 
 
    Return the area of a ring with radius outer.     
    The radius of the hole is inner. 
 
    This function requires outer > inner >= 0. 
 
    >>> area_of_ring(4.0, 2.0)     
    37.7     
    """     
    return area_of_disk(outer) - area_of_disk(inner) 

       
       
def volume_of_sphere(radius):
    """ (number) -> float       
    Return the volume of a sphere with the specified     
    non-negative radius.
    
    volume = volume_of_sphere(5)
    """
    return (4/3)*math.pi*(radius**3)   


def area_of_cone(height, radius): 
    """ (number, number) -> float 
 
    Return the lateral surface area of a right circular 
    cone with the specified non-negative height and radius. 
    
    area = area_of_cone(3, 2) 
    """  
    return math.pi*radius*(((radius**2)+(height**2))**(1/2))