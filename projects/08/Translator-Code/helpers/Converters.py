
def pushD(args):
    # Push D into Stack
    print("@SP", file=args["output"])
    print("A=M", file=args["output"])
    print("M=D", file=args["output"])
    # Increment
    print("@SP", file=args["output"])
    print("M=M+1", file=args["output"])

def popToD(args):
    print("@SP", file=args["output"])
    print("AM=M-1", file=args["output"])
    print("D=M", file=args["output"])

# Pop happens in the order of the name -> M first, D second.
# So y = M, x = D
def popToMD(args):
    
    popToD(args)
    
    # Save y in 13
    print("@13", file=args["output"])
    print("M=D", file=args["output"])

    popToD(args)

    # Now, x in D, & y in M
    print("@13", file=args["output"])


# Filename + Function_name + line_number
# Line Number is not unique across files. Function name is extra.
def fn_name_with_line_number(args):
    return args["fn_name"] + "." + args["index"]