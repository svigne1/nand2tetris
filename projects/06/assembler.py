
import sys

# File Argument
if(len(sys.argv) != 2):
    sys.exit("Pass the file to assemble as command line argument. Don't pass any other arguments")

asm_file = sys.argv[1]

# Read file
f = open(asm_file, "r")

def decimal2Binary(number):
    if(number > 1):
        return decimal2Binary(number // 2) + str(number % 2)
    else:
        return str(number)

def binary16(binary):
    if(len(binary) >= 16):
        return binary
    else:
        return binary16("0"+binary)

symbols = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}
computation = {
    "0":"101010",  
    "1":"111111",  
    "-1":"111010",   
    "D":"001100",  
    "A":"110000",  
    "!D":"001101",   
    "!A":"110001",   
    "-D":"001111",   
    "-A":"110011",   
    "D+1":"011111",   
    "A+1":"110111",   
    "D-1":"001110",   
    "A-1":"110010",   
    # Duplicates - D+A = A+D
    "D+A":"000010",    
    "A+D":"000010",   
    "D-A":"010011",   
    "A-D":"000111",
    # Duplicates - D&A = A&D
    "D&A":"000000",
    "A&D":"000000",   
    # Duplicates - D|A = D|A
    "D|A":"010101",
    "A|D":"010101", 
}

"""
    Ignore
    1. Tabs before a line of code
    2. Some space.. after that comments
    3. Space in a label name is wrong and shud be caught
    4. For other things, syntax error should be raised.

    I want to save the processed result of 1st pass for use in 2nd pass
""" 

code = []

# First Pass
for line in f:
    """
        Removing Comments 
        Split only by the 1st occurence of //
        +ve example:- "123//456//789" gets split into ["123", "456//789"]
        -ve example:- "123456789" gets split into ["123456789"]
        So, always take the 0th argument of the result, and ignore the others.
    """
    no_comments = line.split("//", 1)[0]
    
    # Whitespace
    no_spaces = no_comments.strip()
    if(no_spaces == ""):
        continue

    # Labels
    labels = no_spaces.split("(", 1)
    if (len(labels) == 2):
        # ERROR: labels[0] must be empty string
        content = labels[1].split(")", 1)
        # ERROR: content[1] must be empty string
        # ERROR: content[0] should be a word, not a number. And that word also cant start with a number.
        name = content[0]
        value = len(code)
        symbols[name] = value
        continue

    code.append(labels[0])

"""
    End of First Pass
     - All comments will be removed everywhere..
     - All whitespaces will be omitted
     - Only code we will have
     - And, all symbols would have been recorded
"""

RAM_index = 16

# Second Pass
for index, line in enumerate(code):
    
    instruction = line.split("@", 1)
    binary = "nothing"
    msg = ""
    
    if(len(instruction) == 2):
        # A-Instruction
        # ERROR: instruction[0] must be empty string
        if(instruction[1].isdigit()):
            # Address/Value
            binary = binary16(decimal2Binary(int(instruction[1])))
        elif(instruction[1] in symbols):
            # Label
            binary = binary16(decimal2Binary(symbols[instruction[1]]))
        else:
            # Variable
            symbols[instruction[1]] = RAM_index
            binary = binary16(decimal2Binary(RAM_index))
            RAM_index = RAM_index + 1
    else:
        # C-Instruction

        d1 = "0" # A
        d2 = "0" # D
        d3 = "0" # M
        j1 = "0" # <
        j2 = "0" # =
        j3 = "0" # >

        assignment = instruction[0].split("=", 1)
        if(len(assignment) == 2):
            if "A" in assignment[0]:
                d1 = "1"
            if "D" in assignment[0]:
                d2 = "1"
            if "M" in assignment[0]:
                d3 = "1"
            assignment[0] = assignment[1]
        
        jump = assignment[0].split(";", 1)
        if(len(jump) == 2):
            if "L" in jump[1]:
                j1 = "1"
            if "E" in jump[1]:
                j2 = "1"
            if "G" in jump[1]:
                j3 = "1"
            if "JNE" == jump[1]:
                j1 = "1"
                j2 = "0"
                j3 = "1"
            if "JMP" == jump[1]:
                j1 = "1"
                j2 = "1"
                j3 = "1"
        
        command = jump[0]

        a_bit = "0" 
        if "M" in command:
            a_bit = "1"
        
        command = command.replace("M", "A")
        operation = a_bit + computation[command]
        binary = "111" + operation + d1 + d2 + d3 + j1 + j2 + j3
    
    print(binary)

print("If you want to save the output. Then in bash, pipe the output to a file and delete this line, check last comment in code, to see how its done.")

"""
    python3 assembler.py pong/Pong.asm > pong/Pong.hack
    python3 assembler.py add/Add.asm > add/Add.hack
    python3 assembler.py max/Max.asm > max/Max.hack
    python3 assembler.py rect/Rect.asm > rect/Rect.hack
"""

