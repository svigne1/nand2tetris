
import sys
import os

from helpers.Translator import *

# File Argument
if(len(sys.argv) != 2):
    sys.exit("Pass the file to translate as command line argument. Don't pass any other arguments")

vm_dir = sys.argv[1]

if not os.path.isdir(vm_dir): 
    sys.exit("Pass me a directory with vm files")

# Name of output file
split_parts = vm_dir.split("/")
output_filename = split_parts[-1]

# If path to dir ends with a blackslash, we ignore it
if (split_parts[-1] == ""):
    output_filename = split_parts[-2]

# Full path to file 
output_file = os.path.join(vm_dir, output_filename + ".asm") 

# Delete if output file already exists
if os.path.exists(output_file):
    os.remove(output_file)

for file in os.listdir(vm_dir):
    if file.endswith(".vm"):
        TranslateFile(vm_dir, file, output_file)


