# This is very simple tar file extraction program using python

import os
os.chdir("D:\\nkaushik")

import tarfile
my_tar = tarfile.open('diksha.fingerspelling5.tar.bz2')

my_tar.extractall('my_folder') # specify which folder to extract to
my_tar.close()