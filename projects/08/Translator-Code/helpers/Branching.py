from .Converters import * 

# print(,file=args["output"])

def label_(args):
    args["label"] = args["remaining_command"][0]
    # Set up the label
    print("(" + args["file_name_fn_name"] + "." + args["label"] +  ")",file=args["output"])


def ifGoto_(args):
    args["label"] = args["remaining_command"][0]

    # Condition is popped to D
    popToD(args)
    
    # Check if D is 1(True) or 0(False)
    # print("@0",file=args["output"])
    # print("A=!A",file=args["output"])
    # print("D=D-A;",file=args["output"])
    print("@" + args["file_name_fn_name"] + "." + args["label"],file=args["output"])
    print("D;JNE",file=args["output"])


def goto_(args):
    args["label"] = args["remaining_command"][0]
    # Unconditional jump
    print("@" + args["file_name_fn_name"] + "." + args["label"],file=args["output"])
    print("0;JMP",file=args["output"])