// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// INPUT
(INFINITE_LOOP)
@KBD
D=M;         

// CHECK CONDITIONAL
@WHITE
D;JEQ        

// SETS VALUE = 1 & JUMPS TO SET-SCREEN
(BLACK)
D=0      
@VALUE
M=!D    //  M=1, SETS M AS 000000001. SO, WE NEED TO SET D=000000000 AND USE !D
@SETSCREEN
0;JMP

// SETS VALUE = 0 & JUMPS TO SET-SCREEN
(WHITE)      
@VALUE
M=0
@SETSCREEN
0;JMP

// SETS SCREEN WITH START VALUE
(SETSCREEN)
    // FIRST INDEX IS @SCREEN
    @SCREEN
    D=A 
    @FIRST
    M=D

    // LAST INDEX IS @KBD
    @KBD
    D=A
    @LAST
    M=D

    // SET COUNTER TO FIRST & START LOOP
    @FIRST
    D=M
    @POINTER
    M=D

    // START LOOP
    (LOOP)
        @VALUE
        D=M
        @POINTER
        A=M
        M=D
        @POINTER
        M=M+1
        // SUBTRACT POINTER & LAST TO CHECK IF IT IS 0, WHICH MEANS END HAS BEEN REACHED.
        D=M
        @LAST
        D=D-M
    @INFINITE_LOOP
    D;JEQ
    @LOOP
    0;JMP
    