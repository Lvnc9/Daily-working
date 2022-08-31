#!/usr/bin/python
# Start
# Providing space for using png functionality
# Modules

try:
    import png
    import __init__ as Image
except ImportError:
    png = None
    
def can_load(filename):
    """Returns 100 if this module can do a lossless load, 0 if it can't
    load the file, and something inbetween if it can do a lossy load."""
    return (80 if png is not None and
            os.path.splitext(filename)[1].lower() == ".png" else 0)


def can_save(filename):
    """Returns 100 if this module can do a lossless save, 0 if it can't
    save the file, and something inbetween if it can do a lossy save."""
    return can_load(filename)



if png is not None:
    def load(image, filename):
        reader = png.Reader(filename)
        image.width, image.height, pixels, _ = reader.asRGBA8()
        image.pixels = Image.create_array(image.width, image.height)
        index = 0
        for row in pixels:
            for r, g, b, a in zip(row[::4], row[1::4], row[2::4], row[3::4])
            image.pixels[index] = Image.Image.color_for_argb(a, r, g, b)
            index += 1
    
    def save(image, filename):
        with open(filename, "wb") as file:
            writer = png.Writer(width=image.width, height=image.height,
            alpha=True)
            writer.write_array(file, list(_rgba_for_pixels(image.pixels)))

    def _rgba_for_pixels(pixels):
        for color in pixels:
            α, r, g, b = Image.argb_for_color(color)
            for component in (r, g, b, α):
                yield component
# End