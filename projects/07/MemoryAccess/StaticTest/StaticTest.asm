// push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop static 8
@StaticTest.8
D=A
@13
M=D
@SP
AM=M-1
D=M
@13
A=M
M=D
// pop static 3
@StaticTest.3
D=A
@13
M=D
@SP
AM=M-1
D=M
@13
A=M
M=D
// pop static 1
@StaticTest.1
D=A
@13
M=D
@SP
AM=M-1
D=M
@13
A=M
M=D
// push static 3
@StaticTest.3
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@StaticTest.1
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
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
@14pushToStack
0;JMP
(14return1)
@1
D=A
@14pushToStack
0;JEQ
(14return0)
@0
D=A
@14pushToStack
0;JEQ
(14pushToStack)
@SP
A=M
M=D
@SP
M=M+1
// push static 8
@StaticTest.8
D=A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D+M
@16pushToStack
0;JMP
(16return1)
@1
D=A
@16pushToStack
0;JEQ
(16return0)
@0
D=A
@16pushToStack
0;JEQ
(16pushToStack)
@SP
A=M
M=D
@SP
M=M+1
// push constant 111
@111
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 333
@333
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 888
@888
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 8
@StaticTest.9
@13
M=A
@SP
AM=M-1
D=M
@13
A=M
M=D
// pop static 3
@StaticTest.10
@13
M=A
@SP
AM=M-1
D=M
@13
A=M
M=D
// pop static 1
@StaticTest.11
@13
M=A
@SP
AM=M-1
D=M
@13
A=M
M=D
// push static 3
@StaticTest.12
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@StaticTest.13
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
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
@SP
A=M
M=D
@SP
M=M+1
// push static 8
@StaticTest.15
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// push constant 111
@111
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 333
@333
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 888
@888
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop static 8
@StaticTest.9
@13
M=A
@SP
AM=M-1
D=M
@13
A=M
M=D
// pop static 3
@StaticTest.10
@13
M=A
@SP
AM=M-1
D=M
@13
A=M
M=D
// pop static 1
@StaticTest.11
@13
M=A
@SP
AM=M-1
D=M
@13
A=M
M=D
// push static 3
@StaticTest.12
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@StaticTest.13
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
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
@SP
A=M
M=D
@SP
M=M+1
// push static 8
@StaticTest.15
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
