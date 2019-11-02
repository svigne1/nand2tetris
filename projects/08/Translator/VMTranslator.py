
import sys

from helpers.PushPop import *
from helpers.Arithmetic import *
from helpers.Branching import *
from helpers.Functions import *

# File Argument
if(len(sys.argv) != 2):
    sys.exit("Pass the file to translate as command line argument. Don't pass any other arguments")

vm_file = sys.argv[1]

filename = vm_file.split("/")[-1].split(".")[0]

# Read file
f = open(vm_file, "r")

# Write file
output_file = vm_file.split(".")[0] + ".asm"
# print(output_file)

# Delete if already exists
import os
if os.path.exists(output_file):
    os.remove(output_file)

output = open(output_file, "a")


for index, line in enumerate(f):
    
    # For concatenation with strings
    index = str(index)
    # Extract whatever code comes before the beginning of a comment
    no_comments = line.split("//", 1)[0]
    # Remove spaces before & after
    no_spaces = no_comments.strip()
    
    # Ignore comments and empty lines
    if(no_spaces == ""):
        continue
    
    # Have the vm code as comment in hack code
    print("// " + no_spaces, file=output)

    # Let's try to parse this thing.
    split_by_spaces = no_spaces.split(" ")
    command = split_by_spaces[0]
    
    args = {
        "index": index,
        "command": command,
        "filename": filename,
        "output": output,
        "remaining_command": split_by_spaces[1:3]
    }

    # A function for each keyword.
    commands = {
        # Can be found under Arithmetic.py
        "add": add_,
        "sub": sub_,
        "eq": eq_,
        "gt": gt_,
        "lt": lt_,
        "and": and_,
        "or": or_,
        "neg": neg_,
        "not": not_,
        # "return": return_,
        "push": push_,
        "pop": pop_,
        "label": label_,
        "goto": goto_,
        "if-goto": ifGoto_,
        # "call": call_,
        # "function": function_,
    }

    if(command in commands):
        command_ = commands.get(split_by_spaces[0], lambda: print("ERROR", file=output))
        command_(args)
    else:
        print("ERROR, command not found", file=output)
    

output.close()
