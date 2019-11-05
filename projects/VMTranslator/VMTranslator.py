
import sys
import os

from helpers.Translator import *

# File Argument
if(len(sys.argv) != 2):
    sys.exit("Pass a file or directory to translate as command line argument. Don't pass any other arguments")

vm_dir = sys.argv[1]

bootstrap = True

# If given a filename, extract the directory name, switch off adding boostrap code.
if os.path.isfile(vm_dir):
    vm_dir = vm_dir.rsplit("/", 1)[0]
    bootstrap = False

# Name of output file
split_parts = vm_dir.split("/")
dir_name = split_parts[-1]

# If path to dir ends with a blackslash, we ignore it
if (split_parts[-1] == ""):
    dir_name = split_parts[-2]

# Output file path
output_file_path = os.path.join(vm_dir, dir_name + ".asm") 

# Delete if output file already exists
if os.path.exists(output_file_path):
    os.remove(output_file_path)

output = open(output_file_path, "a")

if bootstrap:
    """ 
        Bootstrap code
            - Set SP to 261 (Strangely, thats what functionCalls want. Ideally, it should be 256)
            - Call Sys.init
    """
    print("@261", file=output)
    print("D=A", file=output)
    print("@0", file=output)
    print("M=D", file=output)
    print("@Sys.init", file=output)
    print("0;JMP", file=output)


for file in os.listdir(vm_dir):
    if file.endswith(".vm"):
        TranslateFile(vm_dir, file, output)

output.close()


