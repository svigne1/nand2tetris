// push constant 10
@10
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
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
// gt
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@2D.ones
D;JGT
(2D.zeroes)
@0
D=A
@2pushD
0;JMP
(2D.ones)
@0
D=!A
(2pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 23
@23
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 47
@47
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@7D.ones
D;JGT
(7D.zeroes)
@0
D=A
@7pushD
0;JMP
(7D.ones)
@0
D=!A
(7pushD)
@SP
A=M
M=D
@SP
M=M+1
