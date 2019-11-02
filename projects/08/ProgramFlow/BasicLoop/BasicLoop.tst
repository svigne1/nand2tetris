// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/08/ProgramFlow/BasicLoop/BasicLoop.tst

load BasicLoop.asm,
output-file BasicLoop.out,
compare-to BasicLoop.cmp,
output-list RAM[0]%D1.6.1 RAM[256]%D1.6.1;

set RAM[0] 256, // 256 changed to 16, for visibility
set RAM[1] 300, // 300 changed to 16 (Temp is not used)
set RAM[2] 400, // 400 changed to 8 (That many local variables are not there)
set RAM[400] 3, // Changed from 400 to 8, since argument segment has been changed above

repeat 600 {
  ticktock;
}

output;
