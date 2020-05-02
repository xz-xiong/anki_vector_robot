#!/usr/bin/env python3



"""Display an image on Vector's face
"""

import os
import sys
import time
import io



try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees

#vector screen size
sizeImage = 184, 96

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        if len(robot.photos.photo_info) == 0:
            print('\n\nNo photos found on Vector. load default photo."\n\n')
            current_directory = os.path.dirname(os.path.realpath(__file__))
            image_path = os.path.join(current_directory, "..", "face_images", "cozmo_image.jpg")
            # Load an image
            image_file = Image.open(image_path)
            # Convert the image to the format used by the Screen
            print("Display image on Vector's face...")
            screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)

            duration_s = 4.0
            robot.screen.set_screen_with_image_data(screen_data, duration_s)
            time.sleep(duration_s)
            return
        for photo in robot.photos.photo_info:
            print(f"Opening photo {photo.photo_id}")
            val = robot.photos.get_photo(photo.photo_id)
            image = Image.open(io.BytesIO(val.image))

            #convert function can only change pixel to height 184, this is too large to fit screen
            #use resize to force change image size
            resize_image = image.resize(sizeImage, Image.LANCZOS)
            #image.show()
            # Convert the image to the format used by the Screen
            print("Display image on Vector's face...")
            
            screen_data = anki_vector.screen.convert_image_to_screen_data(resize_image)

            duration_s = 4.0
            robot.screen.set_screen_with_image_data(screen_data, duration_s)
            time.sleep(duration_s)


if __name__ == "__main__":
    main()
    

