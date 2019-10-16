// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// INITIALIZATION
@COUNTER
M=0
@SUM
M=0

// IF R1 = 0, RETURN
@R1
D=M
@RETURN
D;JEQ

(LOOP)
@R0
D=M
@SUM
M=D+M
@COUNTER
M=M+1
D=M
@R1
D=D-M;
@RETURN
D;JEQ
@LOOP
0;JMP


(RETURN)
@SUM
D=M
@R2
M=D

(INFINITE_LOOP)
@INFINITE_LOOP
0;JMP
