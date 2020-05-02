# Project :  add function to robot anki vector

the vector from anki is not perfect. There is still a lot function to be developed.
this project will be target to add personal function 

## 1. give the robot command to let him show pictures in his screen.

the difficulty is the robot screen can only show pixel 184 x 96
image.convert_image_to_screen_data(img) does not support resize directly
-> use image.resize(sizeImage, Image.LANCZOS) to do it
