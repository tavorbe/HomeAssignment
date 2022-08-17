# Import modules #
import pyminizip
import os
from pathlib import Path

# Text file creation
NewFile = open("newFile.txt", "w")
# Write to the file
NewFile.write("This file will compressed to zip file")
# Close the file
NewFile.close()

# File path
filePath = "newFile.txt"

# Prefix path
pre = None

# Zip file path
zipPath = "./zipFile.zip"

# Set password
password = "Varonis2022"

# Compress level
compressLevel = 5

# Compressing the file
pyminizip.compress(filePath, None, zipPath, password, compressLevel)
