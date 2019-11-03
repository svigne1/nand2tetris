from .Converters import * 

# print(,file=args["output"])

def function_(args):
    name = args["remaining_command"][0]
    local_vars = args["remaining_command"][1]

    print("("+ name +")")

    # Save counter in 13
    print("@"+local_vars)
    print("D=A")
    print("@13")
    print("M=D")

    # Start Loop to initialize local vars
    print("("+ name +".initialize_local_vars.begin)")
    
    # Check counter to exit loop
    print("@13")
    print("D=M")
    print("@"+ name +".initialize_local_vars.end")
    print("D;JEQ")

    # If not, reduce counter, set D to 0, pushD & Repeat
    print("@13")
    print("M=M-1")
    print("@0")
    print("D=A")
    pushD(args)
    print("@"+ name +".initialize_local_vars.begin")
    print("0;JMP")
    
    # End Loop
    print("("+ name +".initialize_local_vars.end)")


def return_(args):
    # Fetch return value of callee & set it for caller.
    print("@SP")
    print("A=M-1")
    print("D=M")
    print("@ARG")
    print("A=M")
    print("M=D")

    # Save pop address in 13
    print("@LCL")
    print("D=M")
    print("@13")
    print("M=D")

    # Reset THAT
    print("@13")
    print("M=D")
    print("@THAT")
    print("M=D")


def call_(args):
    fn_name = args["remaining_command"][0]
    arguments = args["remaining_command"][1]

    # Creating unique return address to caller
    # By using line number in vm file + fn_name + .return.address
    print("(line."+ args["index"] + "." + fn_name +".return.address)")

    # Push return address
    print("@line."+ args["index"] + "." + fn_name +".return.address")
    print("D=A")
    pushD(args)

    # Push old LCL
    print("@LCL")
    print("D=M")
    pushD(args)

    # Push old ARG
    print("@ARG")
    print("D=M")
    pushD(args)

    # Push old THIS
    print("@THIS")
    print("D=M")
    pushD(args)

    # Push old THAT
    print("@THAT")
    print("D=M")
    pushD(args)

    # Compute new ARG 
    print("@SP")
    print("D=M")
    print("@5")
    print("D=D-A")
    print("@"+ arguments)
    print("D=D-A")
    
    # Change ARG
    print("@ARG")
    print("M=D")
    
    # Change LCL
    print("@SP")
    print("D=M")
    print("@LCL")
    print("M=D") 
    
    # Jump to callee
    print("@"+fn_name)
    print("0;JMP")


