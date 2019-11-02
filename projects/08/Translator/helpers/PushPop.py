
from .Converters import * 

# Fetch address in A
def local_(args):
    # Base location
    print("@LCL", file=args["output"])
    print("D=M", file=args["output"])
    # Add offset to base location
    print("@" + args["offset"], file=args["output"])
    print("A=D+A", file=args["output"])

# Fetch address in A
def argument_(args):
    # Base location
    print("@ARG", file=args["output"])
    print("D=M", file=args["output"])
    # Add offset to base location
    print("@" + args["offset"], file=args["output"])
    print("A=D+A", file=args["output"])

# Fetch address in A
def this_(args):
    # Base location
    print("@THIS", file=args["output"])
    print("D=M", file=args["output"])
    # Add offset to base location
    print("@" + args["offset"], file=args["output"])
    print("A=D+A", file=args["output"])

# Fetch address in A
def that_(args):
    # Base location
    print("@THAT", file=args["output"])
    print("D=M", file=args["output"])
    # Add offset to base location
    print("@" + args["offset"], file=args["output"])
    print("A=D+A", file=args["output"])

# Fetch address in A
def pointer_(args):
    if(args["offset"] == "0"):
        print("@THIS", file=args["output"])
    if(args["offset"] == "1"):
        print("@THAT", file=args["output"])

# Fetch address in A
def temp_(args):
    # Base location
    print("@5", file=args["output"])
    print("D=A", file=args["output"])
    # Add offset to base location
    print("@" + args["offset"], file=args["output"])
    print("A=D+A", file=args["output"])

# Fetch address in A
# Since A is used as a pointer to a address than as value by everyone else
# Save the value of A in 13 and point A to 13
def constant_(args):
    # Constant
    print("@" + args["offset"], file=args["output"])
    print("D=A", file=args["output"])
    print("@13", file=args["output"])
    print("M=D", file=args["output"])

# Fetch address in A
def static_(args):
    # @Filename.offset
    print("@" + args["filename"] + "." + args["offset"], file=args["output"])


# Every syntax word has a function associated with it which will do the work.
# All functions return by setting the A register.
memory_segments = {
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
def push_(args):

    memory_segment = args["remaining_command"][0]
    args["offset"] = args["remaining_command"][1]

    # Same as command in loop
    memory_segment_ = memory_segments.get(memory_segment, lambda: print("ERROR", file=output))
    memory_segment_(args)
    
    # If Push, put the value(M) of address(A) in D
    print("D=M", file=args["output"])

    # Push D to Stack
    pushD(args)

# Args contain the next keyword & offset
# index is used to name the labels uniquely by subsequent functions.
# Pop modifies the value stored in the memory location stored in A register.
# A register is a pointer here. And the memory it points, is changed using the stack
def pop_(args):
    
    memory_segment = args["remaining_command"][0]
    args["offset"] = args["remaining_command"][1]
    
    # Same as command in loop
    memory_segment_ = memory_segments.get(memory_segment, lambda: print("ERROR", file=args["output"]))
    memory_segment_(args)
    
    # If Pop, save the address (A) in 13
    print("D=A", file=args["output"])
    print("@13", file=args["output"])
    print("M=D", file=args["output"])
    
    # Pop the stack's value into D
    popToD(args)

    # Set D as value in the address found in 13
    print("@13", file=args["output"])
    print("A=M", file=args["output"])
    print("M=D", file=args["output"])

