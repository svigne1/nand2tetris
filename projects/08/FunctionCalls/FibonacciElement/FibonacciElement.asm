// function Main.fibonacci 0
(Main.fibonacci)
@0
D=A
@13
M=D
(Main.fibonacci.initialize_local_vars.begin)
@13
D=M
@Main.fibonacci.initialize_local_vars.end
D;JEQ
@13
M=M-1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@Main.fibonacci.initialize_local_vars.begin
0;JMP
(Main.fibonacci.initialize_local_vars.end)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// lt
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
@line.13.D.ones
D;JLT
(line.13.D.zeroes)
@0
D=A
@line.13.pushD
0;JMP
(line.13.D.ones)
@0
D=!A
(line.13.pushD)
@SP
A=M
M=D
@SP
M=M+1
// if-goto IF_TRUE
@SP
AM=M-1
D=M
@line.14.IF_TRUE
D;JNE
// goto IF_FALSE
@line.15.IF_FALSE
0;JMP
// label IF_TRUE
(line.16.IF_TRUE)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// return
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
M=D
@LCL
D=M
@13
M=D
@13
AM=M-1
D=M
@THAT
M=D
@13
AM=M-1
D=M
@THIS
M=D
@13
AM=M-1
D=M
@ARG
M=D
@13
AM=M-1
D=M
@LCL
M=D
@13
AM=M-1
A=M
0;JMP
// label IF_FALSE
(line.19.IF_FALSE)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@13
M=D
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
// call Main.fibonacci 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@line.23.Main.fibonacci.return.address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@6
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(line.23.Main.fibonacci.return.address)
// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@13
M=D
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
// call Main.fibonacci 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@line.27.Main.fibonacci.return.address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@6
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(line.27.Main.fibonacci.return.address)
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
// return
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
M=D
@LCL
D=M
@13
M=D
@13
AM=M-1
D=M
@THAT
M=D
@13
AM=M-1
D=M
@THIS
M=D
@13
AM=M-1
D=M
@ARG
M=D
@13
AM=M-1
D=M
@LCL
M=D
@13
AM=M-1
A=M
0;JMP
// function Sys.init 0
(Sys.init)
@0
D=A
@13
M=D
(Sys.init.initialize_local_vars.begin)
@13
D=M
@Sys.init.initialize_local_vars.end
D;JEQ
@13
M=M-1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init.initialize_local_vars.begin
0;JMP
(Sys.init.initialize_local_vars.end)
// push constant 4
@4
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@line.12.Main.fibonacci.return.address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@6
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(line.12.Main.fibonacci.return.address)
// label WHILE
(line.13.WHILE)
// goto WHILE
@line.14.WHILE
0;JMP
