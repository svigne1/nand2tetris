@261
D=A
@0
M=D
@Sys.init
0;JMP
// push constant 111
@111
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// call Sys.nothing 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@NaN.11.finish.address
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.nothing
0;JMP
(NaN.11.finish.address)
// push constant 222
@222
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 90
@90
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 30
@30
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// call Sys.argument 2
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@NaN.17.finish.address
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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.argument
0;JMP
(NaN.17.finish.address)
// label infinite
(NaN.infinite)
// goto infinite
@NaN.infinite
0;JMP
// function Sys.nothing 0
(Sys.nothing)
@0
D=A
@13
M=D
(Sys.nothing.initialize_local_vars.begin)
@13
D=M
@Sys.nothing.initialize_local_vars.end
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
@Sys.nothing.initialize_local_vars.begin
0;JMP
(Sys.nothing.initialize_local_vars.end)
// push constant 20
@20
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 30
@30
D=A
@13
M=D
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
// return
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A+1
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
// function Sys.argument 0
(Sys.argument)
@0
D=A
@13
M=D
(Sys.argument.initialize_local_vars.begin)
@13
D=M
@Sys.argument.initialize_local_vars.end
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
@Sys.argument.initialize_local_vars.begin
0;JMP
(Sys.argument.initialize_local_vars.end)
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
// push argument 1
@ARG
D=M
@1
A=D+A
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
// return
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A+1
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