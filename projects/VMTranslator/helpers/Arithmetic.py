from .Converters import * 

# This creates 3 labels
# One that returns 0 as output for False (D.zeroes)
# One that returns 1 as output for True (D.ones)
# One that acts as a if-else, preventing both labels from running together (pushD)
# input_filename_with_line_number is added to the labels for uniqueness.

def prepareBoolean(args):
    
    unique_key = fn_name_with_line_number(args)

    # D.zeroes -> Sets D as sixteen 0s.. 0000000000000000 (0) & exits to pushD
    print("(" + unique_key + ".D.zeroes)", file=args["output"])
    print("@0", file=args["output"])
    print("D=A", file=args["output"])
    print("@" + unique_key + ".pushD", file=args["output"])
    print("0;JMP", file=args["output"])
    
    # D.ones -> Sets D as sixteen 1s... 1111111111111111 (-1) & exits to pushD
    print("(" + unique_key + ".D.ones)", file=args["output"])
    # !0 = 1111111111111111
    print("@0", file=args["output"])
    print("D=!A", file=args["output"])
    # No need to jump to pushD, pushD is what that comes next.
    
    # PushD -> Pushed D into Stack
    print("(" + unique_key + ".pushD)", file=args["output"])
    pushD(args)

# Pops 2 things, So, pop y to M and x to D
def add_(args):
    popToMD(args)
    print("D=D+M", file=args["output"])
    pushD(args)

# Pops 2 things, So, pop y to M and x to D
def sub_(args):
    popToMD(args)
    print("D=D-M", file=args["output"])
    pushD(args)

# Pops 2 things, So, pop y to M and x to D
def and_(args):
    popToMD(args)
    print("D=D&M", file=args["output"])
    pushD(args)

# Pops 2 things, So, pop y to M and x to D
def or_(args):
    popToMD(args)
    print("D=D|M", file=args["output"])
    pushD(args)

# Pops only 1 thing, So, pop y to D
def neg_(args):
    popToD(args)
    print("D=-D", file=args["output"])
    pushD(args)

# Pops only 1 thing, So, pop y to D
def not_(args):
    popToD(args)
    print("D=!D", file=args["output"])
    pushD(args)

# Pops 2 things, So, pop y to M and x to D
def eq_(args):
    popToMD(args)
    print("D=D-M", file=args["output"])
    # If 0, x & y are equal, jump to D.ones
    print("@" + fn_name_with_line_number(args) + ".D.ones", file=args["output"])
    print("D;JEQ", file=args["output"])
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(args)
    
# Pops 2 things, So, pop y to M and x to D
def gt_(args):
    popToMD(args)
    print("D=D-M", file=args["output"])
    # If 0, x & y are equal, jump to D.ones
    print("@" + fn_name_with_line_number(args) + ".D.ones", file=args["output"])
    print("D;JGT", file=args["output"])
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(args)

# Pops 2 things, So, pop y to M and x to D
def lt_(args):
    popToMD(args)
    print("D=D-M", file=args["output"])
    # If 0, x & y are equal, jump to D.ones
    print("@" + fn_name_with_line_number(args) + ".D.ones", file=args["output"])
    print("D;JLT", file=args["output"])
    # D.zeroes comes first in prepareBoolean
    # So, if jump to D.ones doesn't happen above,
    # it will auto-proceed to D.zeroes
    prepareBoolean(args)
