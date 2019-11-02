
import sys

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


def pushD():
    # Push D into Stack
    print("@SP", file=output)
    print("A=M", file=output)
    print("M=D", file=output)
    # Increment
    print("@SP", file=output)
    print("M=M+1", file=output)

def popToD():
    print("@SP", file=output)
    print("AM=M-1", file=output)
    print("D=M", file=output)

# Pop happens in the order of the name -> M first, D second.
# So y = M, x = D
def popToMD():
    
    popToD()
    
    # Save y in 13
    print("@13", file=output)
    print("M=D", file=output)

    popToD()

    # Now, x in D, & y in M
    print("@13", file=output)

# This creates 3 labels
# One that returns 0 as output for False (D.zeroes)
# One that returns 1 as output for True (D.ones)
# One that acts as a if-else, preventing both labels from running together (pushD)
# Index is added to the labels for uniqueness.
def prepareBoolean(index):
    
    # Index is required to make the jump labels unique to this transaction
    # There can be many such add, subtract commands in a file, they should always 
    # jump forwards, not backwards to a previous subtract commands labels and cause a loop
    
    # D.zeroes -> Sets D as sixteen 0s.. 0000000000000000 (0) & exits to pushD
    print("(" + index + "D.zeroes)", file=output)
    print("@0", file=output)
    print("D=A", file=output)
    print("@" + index + "pushD", file=output)
    print("0;JMP", file=output)
    
    # D.ones -> Sets D as sixteen 1s... 1111111111111111 (-1) & exits to pushD
    print("(" + index + "D.ones)", file=output)
    # !0 = 1111111111111111
    print("@0", file=output)
    print("D=!A", file=output)
    # No need to jump to pushD, pushD is what that comes next.
    
    # PushD -> Pushed D into Stack
    print("(" + index + "pushD)", file=output)
    pushD()

# Pops 2 things, So, pop y to M and x to D
def add_(index):
    popToMD()
    print("D=D+M", file=output)
    pushD()

# Pops 2 things, So, pop y to M and x to D
def sub_(index):
    popToMD()
    print("D=D-M", file=output)
    pushD()

# Pops 2 things, So, pop y to M and x to D
def and_(index):
    popToMD()
    print("D=D&M", file=output)
    pushD()

# Pops 2 things, So, pop y to M and x to D
def or_(index):
    popToMD()
    print("D=D|M", file=output)
    pushD()

# Pops only 1 thing, So, pop y to D
def neg_(index):
    popToD()
    print("D=-D", file=output)
    pushD()

# Pops only 1 thing, So, pop y to D
def not_(index):
    popToD()
    print("D=!D", file=output)
    pushD()

# Pops 2 things, So, pop y to M and x to D
def eq_(index):
    popToMD()
    print("D=D-M", file=output)
    # If 0, x & y are equal, jump to D.ones
    print("@" + index + "D.ones", file=output)
    print("D;JEQ", file=output)
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(index)
    
# Pops 2 things, So, pop y to M and x to D
def gt_(index):
    popToMD()
    print("D=D-M", file=output)
    # If 0, x & y are equal, jump to D.ones
    print("@" + index + "D.ones", file=output)
    print("D;JGT", file=output)
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(index)

# Pops 2 things, So, pop y to M and x to D
def lt_(index):
    popToMD()
    print("D=D-M", file=output)
    # If 0, x & y are equal, jump to D.ones
    print("@" + index + "D.ones", file=output)
    print("D;JLT", file=output)
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(index)

# Fetch address in A
def local_(offset):
    # Base location
    print("@LCL", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def argument_(offset):
    # Base location
    print("@ARG", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def this_(offset):
    # Base location
    print("@THIS", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def that_(offset):
    # Base location
    print("@THAT", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def pointer_(offset):
    if(offset == "0"):
        print("@THIS", file=output)
    if(offset == "1"):
        print("@THAT", file=output)

# Fetch address in A
def temp_(offset):
    # Base location
    print("@5", file=output)
    print("D=A", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
# Since A is used as a pointer to a address than as value by everyone else
# Save the value of A in 13 and point A to 13
def constant_(offset):
    # Constant
    print("@"+offset, file=output)
    print("D=A", file=output)
    print("@13", file=output)
    print("M=D", file=output)

# Fetch address in A
def static_(offset):
    # @Filename.offset
    print("@" + filename + "." + offset, file=output)

# Every syntax word has a function associated with it which will do the work.
# All functions return by setting the A register.
segment = {
    "local": local_,
    "argument": argument_,
    "this": this_,
    "that": that_,
    "constant": constant_,
    "static": static_,
    "pointer": pointer_,
    "temp": temp_,
}

# Args contain the next keyword & offset
# index is used to name the labels uniquely by subsequent functions.
# Push reads the value from the memory location saved in A register & pushes the value to stack
def push_(index, args):
    # removing push
    args = args[1:3]

    # Same as command in loop
    segment_ = segment.get(args[0], lambda: print("ERROR", file=output))
    segment_(args[1])
    
    # If Push, put the value(M) of address(A) in D
    print("D=M", file=output)

    # Push D to Stack
    pushD()

# Args contain the next keyword & offset
# index is used to name the labels uniquely by subsequent functions.
# Pop modifies the value stored in the memory location stored in A register.
# A register is a pointer here. And the memory it points, is changed using the stack
def pop_(index, args):
    # removing pop
    args = args[1:3]

    # Same as command in loop
    segment_ = segment.get(args[0], lambda: print("ERROR", file=output))
    segment_(args[1])
    
    # If Pop, save the address (A) in 13
    print("D=A", file=output)
    print("@13", file=output)
    print("M=D", file=output)
    
    # Pop the stack's value into D
    popToD()

    # Set D as value in the address found in 13
    print("@13", file=output)
    print("A=M", file=output)
    print("M=D", file=output)


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

    # A function for each keyword.
    command = {
        "add": add_,
        "sub": sub_,
        "eq": eq_,
        "gt": gt_,
        "lt": lt_,
        "and": and_,
        "or": or_,
        "neg": neg_,
        "not": not_
    }

    if(split_by_spaces[0] == "push"):
        push_(index, split_by_spaces)
    elif(split_by_spaces[0] == "pop"):   
        pop_(index, split_by_spaces)
    else:
        command_ = command.get(split_by_spaces[0], lambda: print("ERROR", file=output))
        command_(str(index))
    

output.close()
