#!/usr/bin/python
# Start
# Testing
# Modules
import tempfile
import shutil
import os


def pytest_funcarg_temp_dir(request):
    dir = tempfile.mkdtemp()
    print(dir)

    def cleanup():
        shutil.rmtree(dir)
    # This files plays the teardown
    request.addfinalizer(cleanup)

    return dir

def test_os_office(temp_dir):
    os.mkdir(os.path.join(temp_dir, "a"))
    os.mkdir(os.path.join(temp_dir, "b"))
    dir_contents = os.listdir(temp_dir)
    assert len(dir_contents) == 2
    assert "a" in dir_contents
    assert "b" in dir_contents





# End