
import sys

# File Argument
if(len(sys.argv) != 2):
    sys.exit("Pass the file to assemble as command line argument. Don't pass any other arguments")

vm_file = sys.argv[1]

filename = vm_file.split("/")[-1].split(".")[0]

# Read file
f = open(vm_file, "r")

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
        print("@LCL") 
        read_base_value = True
    elif (args[0] == "argument"):
        print("@ARG")
        read_base_value = True
    elif (args[0] == "this"):
        print("@THIS")
        read_base_value = True
    elif (args[0] == "that"):
        print("@THAT")
        read_base_value = True
    elif (args[0] == "temp"):
        print("@5")
        set_base_value = True
    # Pointer - if 0, u get 3 + 0 = 3, if 1, u get 3 + 1 = 4
    elif ((args[0] == "pointer") & (args[1] == "0")):
        print("@3")
        set_location = True
    elif ((args[0] == "pointer") & (args[1] == "1")):
        print("@4")
        set_location = True
    elif (args[0] == "static"):
        print("@" + filename + "." + args[1])
        set_location = True
    # For this alone NO, memory read.
    elif (args[0] == "constant"):
        print("@"+args[1])
        set_value = True
    # Else, error - do nothing, return
    else:
        print("Error, in push")

    sum_location = read_base_value | set_base_value
    read_value = sum_location | set_location

    if(read_base_value):
        print("D=M")
    if(set_base_value):
        print("D=A")
    if(sum_location):
        print("@"+args[1])
        print("D=D+A")
    if(set_location):
        print("D=A")
    if(read_value):
        print("A=D")
        print("D=M")
    if(set_value):
        print("D=A")
    
    # Now push value in D to SP 
    print("@SP")
    print("A=M")
    print("M=D")
    # Increment SP
    print("@SP")
    print("M=M+1")

    
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
        print("@LCL") 
        read_base_value = True
    elif (args[0] == "argument"):
        print("@ARG")
        read_base_value = True
    elif (args[0] == "this"):
        print("@THIS")
        read_base_value = True
    elif (args[0] == "that"):
        print("@THAT")
        read_base_value = True
    elif (args[0] == "temp"):
        print("@5")
        set_base_value = True
    # Pointer - if 0, u get 3 + 0 = 3, if 1, u get 3 + 1 = 4
    elif ((args[0] == "pointer") & (args[1] == "0")):
        print("@3")
        set_location = True
    elif ((args[0] == "pointer") & (args[1] == "1")):
        print("@4")
        set_location = True
    elif (args[0] == "static"):
        set_location = True
        print("@" + filename + "." + args[1])
    else:
        print("Error, in pop")

    sum_location = read_base_value | set_base_value
    
    if(read_base_value):
        print("D=M")
    if(set_base_value):
        print("D=A")
    if(sum_location):
        print("@"+args[1])
        print("D=D+A")
    if(set_location):
        print("D=A")

    # Save address saved in D in 13
    print("@13")
    print("M=D")

    # Decrement SP & pop value into D
    print("@SP")
    print("AM=M-1")
    print("D=M")

    # Save D into address saved in 13
    print("@13")
    print("A=M")
    print("M=D")

        
def push_D_to_Stack():
    print("@SP")
    print("A=M")
    print("M=D")
    print("@SP")
    print("M=M+1")

def arithmetic(index, arg):
    # We need index, to add to the labels, otherwise, for every other eq operation in the code
    # The same label will be used & there will be loops in the code.

    # Decrement Stack & pop y into D
    print("@SP")
    print("AM=M-1")
    print("D=M")

    oneArgument = False

    if(arg == "neg"):
        print("D=-D")
        oneArgument = True
    elif(arg == "not"):
        print("D=!D")
        oneArgument = True
    
    if (oneArgument):
        push_D_to_Stack()
        return

    # Save y at 13
    print("@13")
    print("M=D")   
    
    # Decrement Stack & pop x into D
    print("@SP")
    print("AM=M-1")
    print("D=M")

    # y in M, x in D
    print("@13")

    jump_to_return0 = False

    if(arg == "add"):
        print("D=D+M")
    elif(arg == "sub"):
        print("D=D-M")
    elif(arg == "eq"):
        print("D=D-M")
        print("@"+ index +"return1")
        print("D;JEQ")
        jump_to_return0 = True
    elif(arg == "gt"):
        print("D=D-M")
        print("@"+ index +"return1")
        print("D;JGT")
        jump_to_return0 = True
    elif(arg == "lt"):
        print("D=D-M")
        print("@"+ index +"return1")
        print("D;JLT")
        jump_to_return0 = True
    # Not sure what to return..
    elif(arg == "and"):
        print("D=D&M")
    elif(arg == "or"):
        print("D=D|M")
    else:
        print("Error, not found in arithmetic")
    
    if(jump_to_return0):
        print("@"+ index +"return0")
        print("0;JMP")
    else:
        print("@"+ index +"pushToStack")
        print("0;JMP")

    print("("+ index +"return1)")
    print("@1")
    print("D=A")
    print("@"+ index +"pushToStack")
    print("0;JEQ")

    print("("+ index +"return0)")
    print("@0")
    print("D=A")
    print("@"+ index +"pushToStack")
    print("0;JEQ")
    
    print("("+ index +"pushToStack)")
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
    print("// " + no_spaces)

    split_by_spaces = no_spaces.split(" ")

    # If there are spaces it is push or pop command
    if(split_by_spaces[0] == "push"):
        push(split_by_spaces[1:3])
    elif(split_by_spaces[0] == "pop"):
        pop(split_by_spaces[1:3])
    else:
        arithmetic(str(index), split_by_spaces[0])
