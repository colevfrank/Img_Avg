"""
echo "## active_line 2 ##"
This script calculates the pixel-wise average of all images in the ~/Desktop/Screenshots directory 
echo "## active_line 3 ##"
and saves the result as an image in the same directory.
echo "## active_line 4 ##"
"""
echo "## active_line 5 ##"

echo "## active_line 6 ##"
import glob
echo "## active_line 7 ##"
import os
echo "## active_line 8 ##"
import numpy as np
echo "## active_line 9 ##"
from PIL import Image

echo "## active_line 2 ##"
dir_path = os.path.expanduser("~/Desktop/Screenshots")
echo "## active_line 3 ##"
image_files = glob.glob(os.path.join(dir_path, "*.[Pp][Nn][Gg]")) + glob.glob(os.path.join(dir_path, "*.[Jj][Pp][Gg]*"))
echo "## active_line 4 ##"

echo "## active_line 5 ##"
images = []
echo "## active_line 6 ##"
min_width = min_height = np.inf

echo "## active_line 2 ##"
for file in image_files:
echo "## active_line 3 ##"
    img = Image.open(file)
echo "## active_line 4 ##"
    images.append(img)
echo "## active_line 5 ##"
    if img.size[0] < min_width:
echo "## active_line 6 ##"
        min_width = img.size[0]
echo "## active_line 7 ##"
    if img.size[1] < min_height:
echo "## active_line 8 ##"
        min_height = img.size[1]

echo "## active_line 2 ##"
images = [img.resize((min_width, min_height)) for img in images]
echo "## active_line 3 ##"
image_arrays = [np.array(img) for img in images]
echo "## active_line 4 ##"
average_image_array = np.average(image_arrays, axis=0)
echo "## active_line 5 ##"
average_image_array = average_image_array.astype(int)
echo "## active_line 6 ##"
average_image = Image.fromarray(np.uint8(average_image_array))

echo "## active_line 2 ##"
output_path = os.path.join(dir_path, "averaged_image.png")
echo "## active_line 3 ##"
average_image.save(output_path)
