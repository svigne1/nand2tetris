@256
D=A
@0
M=D
@Sys.init
0;JMP
// function SimpleFunction.test 2
(SimpleFunction.test)
@2
D=A
@13
M=D
(SimpleFunction.test.initialize_local_vars.begin)
@13
D=M
@SimpleFunction.test.initialize_local_vars.end
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
@SimpleFunction.test.initialize_local_vars.begin
0;JMP
(SimpleFunction.test.initialize_local_vars.end)
// push local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@LCL
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
