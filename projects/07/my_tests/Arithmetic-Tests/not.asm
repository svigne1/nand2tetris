// push constant 8
@8
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// not
@SP
AM=M-1
D=M
D=!D
@SP
A=M
M=D
@SP
M=M+1
