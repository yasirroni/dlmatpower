from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

import os
import re

import urllib
import shutil

PACKAGE_NAME = 'matpower'
current_path = os.path.abspath(os.path.dirname(__file__))
version_line = open(os.path.join(current_path, PACKAGE_NAME, 'version.py'), "rt").read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

print(__version__)

def post_install():
    matpower_folder = "matpower"
    matpower_version = '7.1'
    matpower_url = "https://github.com/MATPOWER/matpower/archive/refs/tags/" + matpower_version + ".zip"
    file_name = os.path.join(matpower_folder, "matpower.zip")

    print("Downloading MATPOWER...")
    print(matpower_url)
    urllib.request.urlretrieve(matpower_url, file_name) # source, dest

    shutil.unpack_archive(file_name, matpower_folder, 'zip')
    os.rename(os.path.join(matpower_folder,'matpower-' + matpower_version), os.path.join(matpower_folder,'matpower'))

    os.remove(file_name)
    pass

class CustomInstallCommand(install):
    def run(self):
        print('CustomInstallCommand')
        install.run(self)
        print('CustomInstallCommand_')
        post_install()

class CustomDevelopCommand(develop):
    def run(self):
        print('CustomDevelopCommand')
        develop.run(self)
        print('CustomDevelopCommand_')
        post_install()

setup(
    name = PACKAGE_NAME,
    version = __version__, # versions '0.0.x' are unstable and subject to refactor
    author = "Muhammad Yasirroni",
    author_email = "muhammadyasirroni@gmail.com",
    # description = "IBM CPLEX optimization tools implementation on electrical power system",
    # long_description = long_description,
    # long_description_content_type = "text/markdown",
    url = "https://gitlab.com/yasirroni/matpower-pip",
    package_data = {},
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "Scientific Engineering :: Mathematics",
    ],
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        }
)



