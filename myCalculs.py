# this is a calculation module
# Created 26/04/2019

# Calculate circle area
def findCircleArea(radius):
    area = 3.14159 * radius ** 2
    return area

# Calculate the perimeter of the square
def findSquarePerim(size):
    perimeter = 4 * size
    return perimeter

# Calculate Euclidian distance between two points defined by
# coordinates
def findEuclidDistance(x1, y1, x2, y2):
    import math

    # Calculate triangle sides
    x = abs(x1 - x2) ** 2
    y = abs(y1 - y2) ** 2
    distance = math.sqrt(x + y)
    return distance
