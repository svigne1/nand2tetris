
def push_D_to_Stack(output):
    print("@SP", file=output)
    print("A=M", file=output)
    print("M=D", file=output)
    print("@SP", file=output)
    print("M=M+1", file=output)


help = {
    "popToD": popToD
}
