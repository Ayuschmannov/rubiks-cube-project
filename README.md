# rubiks-cube-project
This code is about detecting colors of Rubik's Cube and arranging them left to right and top to bottom.
Main code is in main.py
Input images are in "input_images" folder.
Output txt file gets generated in "Output" folder.

# Code Explanation
First, the images are read serially using glob. The path for input image folder is to be provided in "path". There are some lists mentioned in code, like: <br />
"final" stores the sequence of occurence of different and same colors in the image. <br />
"cord" stores the coordinates of mid-points of contours found by moments(). <br />
"sorted_cord" stores the coordinates top to bottom and left to right. First coordiantes are sorted in max Y coordinate value. Then it is sliced in three parts (rows). Then these individual rows are sorted wrt ascending X coordinates.<br />
"color" stores all the [B, G, R] values of colors arranged top to bottom and left to right.<br />
"color_distinct" stores the distinct colors of "color". <br />
Then all colors of "color" are checked against "color_distinct" and accordingly, the index of color is appended to "final".<br />
Then finally we write the index of colors as a matrix on a txt file whose folder address can be provided in "output_path".

# How to use the code:
Please provide the image folder path in "path = " in line 5. <br />
Please provide the output folder path to store the output txt files in "output_path" in line 95. <br />
