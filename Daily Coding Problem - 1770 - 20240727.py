# Daily Coding Problem: Problem #1770
# Date: Saturday, July 27th, 2024
# Author: Spencer Trumbore

# NOTE: Special thanks to Nick White, who made this algorithm very simple and cut all the fat from the solution.
# This solution follows his pretty closely but is also structured and annotated to point out potential errors.
# https://www.youtube.com/watch?v=aehEcTEPtCs

'''
(Flood Fill Algorithm)
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color 'C', replace the color of the given pixel and all adjacent same colored pixels with 'C'.
'''

def main():
    image = [['B','B','W'],
              ['W','W','W'],
              ['W','W','W'],
              ['B','B','B']]
    
    print("ORIGINAL: ")
    prettyPrint(image)
    print()

    floodFill(image,1,2,'G')

    print("RESULT: ")
    prettyPrint(image)

def fill(_image, _posX, _posY, _color, _newColor):
    '''Finds a pixels that match _color which are at or adjacent to (_posX,_posY) and changes their color to _newColor.'''
    # Stop filling if pixel position (_posX, _posY) is out of bounds
    if (
        _posX < 0 or
        _posY < 0 or
        _posX >= len(_image) or
        _posY >= len(_image[0])   
        ): return
    
    # Stop filling if pixel color doesn't match _color
    if (_image[_posX][_posY] != _color):
        return
    
    # Change the pixel's color to _newColor (Important to do this before recursive step)
    _image[_posX][_posY] = _newColor
    # Recursive call on adjacent pixels (will be called on pixels we already checked until we hit recursion depth limit if we don't fill the pixels as we go)
    fill(_image, _posX - 1, _posY, _color, _newColor)
    fill(_image, _posX + 1, _posY, _color, _newColor)
    fill(_image, _posX, _posY - 1, _color, _newColor)
    fill(_image, _posX, _posY + 1, _color, _newColor)

def floodFill(_image, _posX, _posY, _newColor):
    if (_image[_posX][_posY] == _newColor):
        return
    fill(_image,_posX,_posY,_image[_posX][_posY], _newColor)

def prettyPrint(_array):
    print('[')
    for row in _array[:-1]:
        print(str(row) + ',')
    print(_array[-1])
    print(']')        

if __name__ == "__main__":
    main()