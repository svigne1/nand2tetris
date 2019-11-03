from .Converters import * 

# print(,file=args["output"], file=args["output"])

def call_(args):
    fn_name = args["remaining_command"][0]
    arguments = args["remaining_command"][1]

    args["currently_parsing_function"] = fn_name
    unique_key = args["input_filename_with_function"](args)
    # dummy_spacing
    # When there are 0 arguments. Return address & ARG point to the same address
    # As a result, When the function returns, return value becomes the return address.
    # To prevent this, we are introducing a dummy_spacing between ARG & return address.
    print("@0", file=args["output"])
    print("D=A", file=args["output"])
    pushD(args)

    # Push return address
    print("@"+ unique_key + ".finish.address", file=args["output"])
    print("D=A", file=args["output"])
    pushD(args)

    # Push old LCL
    print("@LCL", file=args["output"])
    print("D=M", file=args["output"])
    pushD(args)

    # Push old ARG
    print("@ARG", file=args["output"])
    print("D=M", file=args["output"])
    pushD(args)

    # Push old THIS
    print("@THIS", file=args["output"])
    print("D=M", file=args["output"])
    pushD(args)

    # Push old THAT
    print("@THAT", file=args["output"])
    print("D=M", file=args["output"])
    pushD(args)

    # Compute new ARG 
    print("@SP", file=args["output"])
    print("D=M", file=args["output"])
    # dummy_spacing, return, lcl, arg, this, that
    print("@6", file=args["output"])
    print("D=D-A", file=args["output"])
    print("@"+ arguments, file=args["output"])
    print("D=D-A", file=args["output"])
    
    # Change ARG
    print("@ARG", file=args["output"])
    print("M=D", file=args["output"])
    
    # Change LCL
    print("@SP", file=args["output"])
    print("D=M", file=args["output"])
    print("@LCL", file=args["output"])
    print("M=D", file=args["output"])
    
    # Jump to callee
    print("@"+fn_name, file=args["output"])
    print("0;JMP", file=args["output"])

    # Creating unique return address to caller after all of the call statements
    # By using line number in vm file + fn_name + .return.address
    print("("+ unique_key + ".finish.address)", file=args["output"])

def function_(args):
    name = args["remaining_command"][0]
    local_vars = args["remaining_command"][1]

    args["currently_parsing_function"] = name

    # For Function as well as labels inside function
    unique_key = args["input_filename_with_function"](args)

    print("("+ unique_key +")", file=args["output"])

    # Save counter in 13
    print("@"+local_vars, file=args["output"])
    print("D=A", file=args["output"])
    print("@13", file=args["output"])
    print("M=D", file=args["output"])

    # Start Loop to initialize local vars
    print("("+ unique_key +".initialize_local_vars.begin)", file=args["output"])
    
    # Check counter to exit loop
    print("@13", file=args["output"])
    print("D=M", file=args["output"])
    print("@"+ unique_key +".initialize_local_vars.end", file=args["output"])
    print("D;JEQ", file=args["output"])

    # If not, reduce counter, set D to 0, pushD & Repeat
    print("@13", file=args["output"])
    print("M=M-1", file=args["output"])
    print("@0", file=args["output"])
    print("D=A", file=args["output"])
    pushD(args)
    print("@"+ unique_key +".initialize_local_vars.begin", file=args["output"])
    print("0;JMP", file=args["output"])
    
    # End Loop
    print("("+ unique_key +".initialize_local_vars.end)", file=args["output"])


def return_(args):

    args["currently_parsing_function"] = "NaN"

    # Fetch return value of callee & set it for caller.
    print("@SP", file=args["output"])
    print("A=M-1", file=args["output"])
    print("D=M", file=args["output"])
    print("@ARG", file=args["output"])
    print("A=M", file=args["output"])
    print("M=D", file=args["output"])

    # Set SP to ARG
    print("D=A", file=args["output"])
    print("@SP", file=args["output"])
    print("M=D", file=args["output"])

    # Save pop address in 13
    print("@LCL", file=args["output"])
    print("D=M", file=args["output"])
    print("@13", file=args["output"])
    print("M=D", file=args["output"])

    # Reset THAT
    print("@13", file=args["output"])
    print("AM=M-1", file=args["output"])
    print("D=M", file=args["output"])
    print("@THAT", file=args["output"])
    print("M=D", file=args["output"])

    # Reset THIS
    print("@13", file=args["output"])
    print("AM=M-1", file=args["output"])
    print("D=M", file=args["output"])
    print("@THIS", file=args["output"])
    print("M=D", file=args["output"])
    
    # Reset ARG
    print("@13", file=args["output"])
    print("AM=M-1", file=args["output"])
    print("D=M", file=args["output"])
    print("@ARG", file=args["output"])
    print("M=D", file=args["output"])

    # Reset LCL
    print("@13", file=args["output"])
    print("AM=M-1", file=args["output"])
    print("D=M", file=args["output"])
    print("@LCL", file=args["output"])
    print("M=D", file=args["output"])

    # Return
    print("@13", file=args["output"])
    print("AM=M-1", file=args["output"])
    print("A=M", file=args["output"])
    print("0;JMP", file=args["output"])

