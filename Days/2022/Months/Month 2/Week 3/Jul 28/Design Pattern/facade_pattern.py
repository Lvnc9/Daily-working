#!/usr/bin/python3
# Start
# An Exmaple of using facade pattern
# Modules
import zipfile
import os
import tarfile
import re
import string
import gzip

class Archive:

    def __init__(self, filename:str):
        self._name = None
        self._unpack = None
        self._file = None
        self.filename = filename
    
    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, name:str):
        self.close()
        self.__filename = name

    def close(self):
        if self._file is not None:
            self._file.close()
        self._name = self._file = self.unpack = None

    def names(self):
        if self._file is None:
            self._prepare()
        return self._names()

    def unpack(self):
        if self._file is None:
            self._prepare()
        self._unpack()
    
    def _prepare(self):
        if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz",
        ".zip")):
            self._prepare_tarball_or_zip()
        elif self.filename.endswith('.gz'):
            self._prepare_gzip()
        else:
            raise ValueError(f"UNREADABLE: {self.filename}")

    def _prepare_tarball_or_zip(self):
        def safe_extractall():
            unsafe = []
            for name in self.names():
                if not self.is_safe(name):
                    unsafe.append(name)
            if unsafe:  
                raise ValueError(f"UNSAFE TO UNPACK {unsafe}")
            self._file_extractall()
        if self.filename.endswith('.zip'):
            self._file = zipfile.ZipFile(self.filename)
            self._names = self._file.namelist
            self._unpack = safe_extractall
        else: # Ends with .tar.gz, .tar.bz2, or .tar.xz
            suffix = os.path.splitext(self.filename)[1]
            self._file = tarfile.open(self.filename, "r:" + suffix[1:])
            self._names = self._file.getnames
            self._unpack = safe_extractall

    def is_safe(self, filename):
        return not (filename.startswith(("/", "\\")) or
            (len(filename) > 1 and filename[1] == ":" and
            filename[0] in string.ascii_letter) or
            re.search(r"[.][.][/\\]", filename))

    def _prepare_gzip(self):
        self._file = gzip.open(self.filename)
        filename = self.filename[:-3]
        self._names = lambda: [filename]
        def extractall():
            with open(filename, "wb") as file:
                file.write(self._file.read())
        self._unpack = extractall

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()



zipFilename = 'idk'
with Archive(zipFilename) as archive:
    print(archive.names())
    archive.unpack()
    


# End