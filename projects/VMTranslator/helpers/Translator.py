
from helpers.PushPop import *
from helpers.Arithmetic import *
from helpers.Branching import *
from helpers.Functions import *

import os

def TranslateFile(dir, input_filename, output):

    input_file_path = os.path.join(dir, input_filename)

    # Read vm file
    f = open(input_file_path, "r")

    input_filename = input_filename.split(".vm")[0]

    """ 
        Test code. For testing my AddFunction tests under FunctionCalls.
            - Set SP to 16
            - Set LCL, ARG, THIS, THAT to 1,2,3,4
            - Call Sys.init
    """

    # print("@16", file=output)
    # print("D=A", file=output)
    # print("@0", file=output)
    # print("M=D", file=output)

    # print("@1", file=output)
    # print("M=A", file=output)

    # print("@2", file=output)
    # print("M=A", file=output)

    # print("@3", file=output)
    # print("M=A", file=output)

    # print("@4", file=output)
    # print("M=A", file=output)

    # By default, we have seen no function. So initial value is NaN
    global_fn_name = "NaN"

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
            # Index is line number in the vm file (which is unique) for one file. 
            "index": index,
            "command": command,

            # Needed by static
            "filename": input_filename,
            
            # Function name by default comes as filename + fn_name from the compiler
            "fn_name": global_fn_name,

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
        
        # We need to remember, what is the last read function & keep using it until we see a new function
        global_fn_name = args["fn_name"]
    

