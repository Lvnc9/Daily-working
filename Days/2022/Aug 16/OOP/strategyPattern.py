#!/usr/bin/python
# Start 
# Strategy Pattern -> we have a user area and for user
# there are couple of objects that do the same functionality 
# but not are the same
# Modules
import PIL as Image

class TiledStrategy:
    
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new("RGB", desktop_size)
        num_tiles = [
            o // i + 1 for o, i in 
            zip(out_img.size, in_img.size)
        ]

        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] * y,
                        in_img.size[0] * (x+1),
                        in_img.size[1] * (y+1)
                    )
                    )
        return out_img

# End