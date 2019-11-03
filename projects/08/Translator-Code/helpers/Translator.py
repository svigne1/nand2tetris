
from helpers.PushPop import *
from helpers.Arithmetic import *
from helpers.Branching import *
from helpers.Functions import *

def TranslateFile(input_file_path, output_file_path):

    # Read vm file
    f = open(input_file_path, "r")

    input_filename = input_file_path.split(".vm")[1]

    # print(output_file)
    output = open(output_file_path, "a")


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
            "input_filename": input_filename,
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
