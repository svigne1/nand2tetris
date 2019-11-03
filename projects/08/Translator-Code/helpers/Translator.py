
from helpers.PushPop import *
from helpers.Arithmetic import *
from helpers.Branching import *
from helpers.Functions import *

import os

def TranslateFile(dir, input_filename, output_file_path):

    input_file_path = os.path.join(dir, input_filename)

    # Read vm file
    f = open(input_file_path, "r")

    input_filename = input_filename.split(".vm")[0]

    # print(output_file)
    output = open(output_file_path, "a")

    """ 
        Bootstrap code
            - Set SP to 256
            - Call Sys.init
    """

    # print("@256", file=output)
    # print("D=A", file=output)
    # print("@0", file=output)
    # print("M=D", file=output)
    # print("@Sys.init", file=output)
    # print("0;JMP", file=output)

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
            # Index is line number in the vm file (which is unique)
            "index": index,
            "command": command,
            
            # Multiple RETURN statements are there.. !! Now WHAT TO DO !!?? 

            # You can have same label in different files or different functions of same file.
            # So File.Function is unique key for label.
            # If label not declared inside function, use NaN as default function.

            # Needed by static
            "input_filename": input_filename,
            # Function name by default comes with the input filename.
            "file_name_fn_name": input_filename,
            # You need this if you have multiple eq, gt, lt commands in a single file
            # Each eq, gt, lt command generates labels that need to be unique, so u need
            # the line number. And file numbers are duplicate across filenames.
            "input_filename_with_line_number": input_filename + ".Line." + index,
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
            "push": push_,
            "pop": pop_,
            "label": label_,
            "goto": goto_,
            "if-goto": ifGoto_,
            # Can be found in Functions.py
            "call": call_,
            "function": function_,
            "return": return_,
        }

        if(command in commands):
            command_ = commands.get(split_by_spaces[0], lambda: print("ERROR", file=output))
            command_(args)
        else:
            print("ERROR, command not found", file=output)
    
    output.close()
