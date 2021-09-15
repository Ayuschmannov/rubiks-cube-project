# rubiks-cube-project
This code is about detecting colors of Rubik's Cube and arranging them left to right and top to bottom.
Main code is in main.py
Input images are in "input_images" folder.
Output txt file gets generated in "Output" folder.

# Code Explanation
First, the images are read serially using glob. The path for input image folder is to be provided in "path". There are some lists mentioned in code, like: final = [] stores the sequence of occurence of colors in the image. color = [] stores all the [B, G, R] values of colors arranged from top-bottom and left-right. color2 = [] stores the distinct colors in color[]. After getting all the different contours, we sort them using sorted() function and then we get the bounding rectangles around the contours and get the color at the middle of the bounding rectangle. Then this color gets appended in color[]. Then we proceed by checking each color and how many times it hsa occurred etc. Then finally we write the matrix on  a txt file whose folder address can be provided in "output_path".
