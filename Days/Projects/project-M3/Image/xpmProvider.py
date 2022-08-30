#!/usr/bin/python
# Start
# Extracing, Parsing, Recognizing .xpm files
# Modules
import os
import Image
import re


def can_load(filename):
    return 80 if os.path.splitext(filename)[1] == '.xpm' else 0

def can_save(filename):
    can_load(filename)


(_WANT_XPM, _WANT_NAME, _WANT_VALUES, _WANT_COLOR,
_WANT_PIXELS, _DONE) = ("WANT_XPM", "WANT_NAME", "WANT_VALUES", "WANT_COLOR",
                    "WANT_PIXELS", "DONE")


def load(image, filename):
    colors = cpp = count = None
    state = _WANT_XPM
    palette = {}
    index = 0
    with open(filename, 'rt', encoding="ascii") as file:
        for lino, line in enumerate(file, start=1):
            line = line.strip()
            '...'

def name(image, filename):
    name = Image.sanitized_name(filename)

def save(image, filename):
    name = Image.sanitized_name(filename)
    palette, cpp = _palette_and_cpp(image.pixels)
    with open(filename, "w+t", encoding="ascii") as file:
        _write_header(image, file, name, cpp, len(palette))
        _write_palette(file, palette)
        _write_pixels(image, file, palette)

def senizied_name(name):
    name = re.sub(r"\W+", "", os.path.basename(os.path.splitext(name)[0]))
    if not name or name[0].isdigit():
        name = "z" + name
        

def _write_header(): pass
def _write_palette() : pass
def _write_pixels(): pass


# End