"""
SYSC 1005 Fall 2018 Lab 9, Parts 2 and 3
"""

def get_points():
    """ (None) -> set of 2-tuples of float
    
    Return a set of (x, y) points, with each point stored in a tuple.
    
    >>> get_points()
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}




def fit_line_to_points(points):
    sumx = 0
    sumy = 0
    sumxx = 0
    sumxy = 0
    for x,y in points:
        sumx = sumx + x
        sumy = sumy + y
        sumxx = sumxx + x**2
        sumxy = sumxy + x*y
    n = len(points)
    m = (sumx*sumy - n*sumxy)/(sumx*sumx - n*sumxx)
    b = (sumx*sumxy - sumxx*sumy )/(sumx*sumx - n*sumxx)
    return m, b


def read_and_print_lines():
    infile = open('data.txt', 'r')
    for line in infile:
        print(line)
    infile.close()

def read_points(filename):
    infile = open(filename, 'r')
    data = set()
    for line in infile:
        numbers = line.split()
        point = float(numbers[0]), float(numbers[1])
        data.add(point)
    infile.close()
    return data

if __name__ == "__main__":
    print("Input name of text file")
    prompt = (": ")
    filename = input(prompt)
    points = read_points(filename)
    answer = fit_line_to_points(points)
    print("The best-fit line is y = " + str(answer[0]) + "x + " + str(answer[1]))
    