// push constant 17
@17
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// eq
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
@9D.ones
D;JEQ
(9D.zeroes)
@0
D=A
@9pushD
0;JMP
(9D.ones)
@0
D=!A
(9pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// eq
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
@12D.ones
D;JEQ
(12D.zeroes)
@0
D=A
@12pushD
0;JMP
(12D.ones)
@0
D=!A
(12pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// eq
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
@15D.ones
D;JEQ
(15D.zeroes)
@0
D=A
@15pushD
0;JMP
(15D.ones)
@0
D=!A
(15pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
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
@18D.ones
D;JLT
(18D.zeroes)
@0
D=A
@18pushD
0;JMP
(18D.ones)
@0
D=!A
(18pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
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
@21D.ones
D;JLT
(21D.zeroes)
@0
D=A
@21pushD
0;JMP
(21D.ones)
@0
D=!A
(21pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
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
@24D.ones
D;JLT
(24D.zeroes)
@0
D=A
@24pushD
0;JMP
(24D.ones)
@0
D=!A
(24pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
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
@27D.ones
D;JGT
(27D.zeroes)
@0
D=A
@27pushD
0;JMP
(27D.ones)
@0
D=!A
(27pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
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
@30D.ones
D;JGT
(30D.zeroes)
@0
D=A
@30pushD
0;JMP
(30D.ones)
@0
D=!A
(30pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
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
@33D.ones
D;JGT
(33D.zeroes)
@0
D=A
@33pushD
0;JMP
(33D.ones)
@0
D=!A
(33pushD)
@SP
A=M
M=D
@SP
M=M+1
// push constant 57
@57
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
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
// push constant 112
@112
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
// neg
@SP
AM=M-1
D=M
D=-D
@SP
A=M
M=D
@SP
M=M+1
// and
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D&M
@SP
A=M
M=D
@SP
M=M+1
// push constant 82
@82
D=A
@13
M=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D|M
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
