
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

def prepareBoolean(index):
    
    # Index is required to make the jump labels unique to this transaction
    # There can be many such add, subtract commands in a file, they should always 
    # jump forwards, not backwards and cause a loop
    
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
    print("@" + index + "pushD", file=output)
    print("0;JMP", file=output)
    
    # PushD -> Pushed D into Stack
    print("(" + index + "pushD)", file=output)
    pushD()


def add_(index, args):
    popToMD()
    print("D=D+M", file=output)
    pushD()

def sub_(index, args):
    popToMD()
    print("D=D-M", file=output)
    pushD()

def and_(index, args):
    popToMD()
    print("D=D&M", file=output)
    pushD()

def or_(index, args):
    popToMD()
    print("D=D|M", file=output)
    pushD()

def neg_(index, args):
    popToD()
    print("D=-D", file=output)
    pushD()

def not_(index, args):
    popToD()
    print("D=!D", file=output)
    pushD()

def eq_(index, args):
    popToMD()
    print("D=D-M", file=output)
    # If 0, x & y are equal, jump to D.ones
    print("@" + index + "D.ones", file=output)
    print("D;JEQ", file=output)
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(index)
    

def gt_(index, args):
    popToMD()
    print("D=D-M", file=output)
    # If 0, x & y are equal, jump to D.ones
    print("@" + index + "D.ones", file=output)
    print("D;JGT", file=output)
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(index)

def lt_(index, args):
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
def local_(index, offset):
    # Base location
    print("@LCL", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def argument_(index, offset):
    # Base location
    print("@ARG", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def this_(index, offset):
    # Base location
    print("@THIS", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def that_(index, offset):
    # Base location
    print("@THAT", file=output)
    print("D=M", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def pointer_(index, offset):
    if(offset == "0"):
        print("@THIS", file=output)
    if(offset == "1"):
        print("@THAT", file=output)

# Fetch address in A
def temp_(index, offset):
    # Base location
    print("@5", file=output)
    print("D=A", file=output)
    # Add offset to base location
    print("@"+offset, file=output)
    print("A=D+A", file=output)

# Fetch address in A
def constant_(index, offset):
    # Constant
    print("@"+offset, file=output)
    print("D=A", file=output)
    print("@13", file=output)
    print("M=D", file=output)

# Fetch address in A
def static_(index, offset):
    # @Filename.offset
    print("@" + filename + "." + offset, file=output)

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
    
def push_(index, args):
    args = args[1:3]

    segment_ = segment.get(args[0], lambda: print("ERROR", file=output))
    segment_(index, args[1])
    # If Push, put the value(M) of address(A) in D
    print("D=M", file=output)
    # Set stack to value in D
    print("@SP", file=output)
    print("A=M", file=output)
    print("M=D", file=output)
    # Increment stack
    print("@SP", file=output)
    print("M=M+1", file=output)

def pop_(index, args):
    args = args[1:3]

    segment_ = segment.get(args[0], lambda: print("ERROR", file=output))
    segment_(index, args[1])
    
    # If Pop, put the address (A) in 13
    print("D=A", file=output)
    print("@13", file=output)
    print("M=D", file=output)
    # Set D to stack value by popping
    print("@SP", file=output)
    print("AM=M-1", file=output)
    print("D=M", file=output)

    # Set D to address found in 13
    print("@13", file=output)
    print("A=M", file=output)
    print("M=D", file=output)


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

    command = {
        "push": push_,
        "pop": pop_,
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
    command_ = command.get(split_by_spaces[0], lambda: print("ERROR", file=output))
    command_(str(index), split_by_spaces)
    

output.close()
