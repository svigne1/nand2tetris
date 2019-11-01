
import sys

# File Argument
if(len(sys.argv) != 2):
    sys.exit("Pass the file to assemble as command line argument. Don't pass any other arguments")

vm_file = sys.argv[1]

filename = vm_file.split("/")[-1].split(".")[0]

# Read file
f = open(vm_file, "r")

print(vm_file.split(".")[0] + ".asm")

output = open(vm_file.split(".")[0] + ".asm", "a")

def push(args):
    """
        Options
            - Local (LCL - 1)
            - Argument (ARG - 2)
            - THIS (3)
            - THAT (4)
            - pointer (O - THIS, 1 - THAT)
            - Static (LABEL - FILENAME.INDEX)
            - constant
            - temp (5 TO 12)
    """
    read_base_value = False
    set_base_value = False
    sum_location = False 
    set_location = False
    read_value = False
    set_value = False

    if (args[0] == "local"):
        print("@LCL", file=output)
        read_base_value = True
    elif (args[0] == "argument"):
        print("@ARG", file=output)
        read_base_value = True
    elif (args[0] == "this"):
        print("@THIS", file=output)
        read_base_value = True
    elif (args[0] == "that"):
        print("@THAT", file=output)
        read_base_value = True
    elif (args[0] == "temp"):
        print("@5", file=output)
        set_base_value = True
    # Pointer - if 0, u get 3 + 0 = 3, if 1, u get 3 + 1 = 4
    elif ((args[0] == "pointer") & (args[1] == "0")):
        print("@3", file=output)
        set_location = True
    elif ((args[0] == "pointer") & (args[1] == "1")):
        print("@4", file=output)
        set_location = True
    elif (args[0] == "static"):
        print("@" + filename + "." + args[1], file=output)
        set_location = True
    # For this alone NO, memory read.
    elif (args[0] == "constant"):
        print("@"+args[1], file=output)
        set_value = True
    # Else, error - do nothing, return
    else:
        print("Error, in push", file=output)

    sum_location = read_base_value | set_base_value
    read_value = sum_location | set_location

    if(read_base_value):
        print("D=M", file=output)
    if(set_base_value):
        print("D=A", file=output)
    if(sum_location):
        print("@"+args[1], file=output)
        print("D=D+A", file=output)
    if(set_location):
        print("D=A", file=output)
    if(read_value):
        print("A=D", file=output)
        print("D=M", file=output)
    if(set_value):
        print("D=A", file=output)
    
    # Now push value in D to SP 
    print("@SP", file=output)
    print("A=M", file=output)
    print("M=D", file=output)
    # Increment SP
    print("@SP", file=output)
    print("M=M+1", file=output)

    
def pop(args):
    """
        Options
            - Local (LCL - 1)
            - Argument (ARG - 2)
            - THIS (3)
            - THAT (4)
            - pointer (O - THIS, 1 - THAT)
            - Static (LABEL - FILENAME.INDEX)
            - constant
            - temp (5 TO 12)
    """ 
    
    read_base_value = False
    set_base_value = False
    sum_location = False
    set_location = False

    if (args[0] == "local"):
        print("@LCL", file=output) 
        read_base_value = True
    elif (args[0] == "argument"):
        print("@ARG", file=output)
        read_base_value = True
    elif (args[0] == "this"):
        print("@THIS", file=output)
        read_base_value = True
    elif (args[0] == "that"):
        print("@THAT", file=output)
        read_base_value = True
    elif (args[0] == "temp"):
        print("@5", file=output)
        set_base_value = True
    # Pointer - if 0, u get 3 + 0 = 3, if 1, u get 3 + 1 = 4
    elif ((args[0] == "pointer") & (args[1] == "0")):
        print("@3", file=output)
        set_location = True
    elif ((args[0] == "pointer") & (args[1] == "1")):
        print("@4", file=output)
        set_location = True
    elif (args[0] == "static"):
        set_location = True
        print("@" + filename + "." + args[1], file=output)
    else:
        print("Error, in pop", file=output)

    sum_location = read_base_value | set_base_value
    
    if(read_base_value):
        print("D=M", file=output)
    if(set_base_value):
        print("D=A", file=output)
    if(sum_location):
        print("@"+args[1], file=output)
        print("D=D+A", file=output)
    if(set_location):
        print("D=A", file=output)

    # Save address saved in D in 13
    print("@13", file=output)
    print("M=D", file=output)

    # Decrement SP & pop value into D
    print("@SP", file=output)
    print("AM=M-1", file=output)
    print("D=M", file=output)

    # Save D into address saved in 13
    print("@13", file=output)
    print("A=M", file=output)
    print("M=D", file=output)

        
def push_D_to_Stack():
    print("@SP", file=output)
    print("A=M", file=output)
    print("M=D", file=output)
    print("@SP", file=output)
    print("M=M+1", file=output)

def arithmetic(index, arg):
    # We need index, to add to the labels, otherwise, for every other eq operation in the code
    # The same label will be used & there will be loops in the code.

    # Decrement Stack & pop y into D
    print("@SP", file=output)
    print("AM=M-1", file=output)
    print("D=M", file=output)

    oneArgument = False

    if(arg == "neg"):
        print("D=-D", file=output)
        oneArgument = True
    elif(arg == "not"):
        print("D=!D", file=output)
        oneArgument = True
    
    if (oneArgument):
        push_D_to_Stack()
        return

    # Save y at 13
    print("@13", file=output)
    print("M=D", file=output)
    
    # Decrement Stack & pop x into D
    print("@SP", file=output)
    print("AM=M-1", file=output)
    print("D=M", file=output)

    # y in M, x in D
    print("@13", file=output)

    jump_to_return0 = False

    if(arg == "add"):
        print("D=D+M", file=output)
    elif(arg == "sub"):
        print("D=D-M", file=output)
    elif(arg == "eq"):
        print("D=D-M", file=output)
        print("@"+ index +"return1", file=output)
        print("D;JEQ", file=output)
        jump_to_return0 = True
    elif(arg == "gt"):
        print("D=D-M", file=output)
        print("@"+ index +"return1", file=output)
        print("D;JGT", file=output)
        jump_to_return0 = True
    elif(arg == "lt"):
        print("D=D-M", file=output)
        print("@"+ index +"return1", file=output)
        print("D;JLT", file=output)
        jump_to_return0 = True
    # Not sure what to return..
    elif(arg == "and"):
        print("D=D&M", file=output)
    elif(arg == "or"):
        print("D=D|M", file=output)
    else:
        print("Error, not found in arithmetic", file=output)
    
    if(jump_to_return0):
        print("@"+ index +"return0", file=output)
        print("0;JMP", file=output)
    else:
        print("@"+ index +"pushToStack", file=output)
        print("0;JMP", file=output)

    print("("+ index +"return1)", file=output)
    print("@1", file=output)
    print("D=A", file=output)
    print("@"+ index +"pushToStack", file=output)
    print("0;JEQ", file=output)

    print("("+ index +"return0)", file=output)
    print("@0", file=output)
    print("D=A", file=output)
    print("@"+ index +"pushToStack", file=output)
    print("0;JEQ", file=output)
    
    print("("+ index +"pushToStack)", file=output)
    push_D_to_Stack()
    

for index, line in enumerate(f):
    
    # Extract whatever code comes before the beginning of a comment
    no_comments = line.split("//", 1)[0]
    # Remove spaces before & after
    no_spaces = no_comments.strip()
    
    # Ignore comments and empty lines
    if(no_spaces == ""):
        continue
    
    # Have the vm code as comment in hack code
    print("// " + no_spaces, file=output)

    split_by_spaces = no_spaces.split(" ")

    # If there are spaces it is push or pop command
    if(split_by_spaces[0] == "push"):
        push(split_by_spaces[1:3])
    elif(split_by_spaces[0] == "pop"):
        pop(split_by_spaces[1:3])
    else:
        arithmetic(str(index), split_by_spaces[0])
    

output.close()
