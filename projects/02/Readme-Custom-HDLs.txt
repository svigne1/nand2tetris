I have added helper files in this project

1. Or16Way which uses Or8Way internally...
    - I am not able to use a sub-bus of out pin, or intermediate pin in Or8Way function
    - So, i am writing a new class, where the intermediate pin becomes a input pin, whose sub-bus i can take !
    - I am ORing together all the bits, to find out whether the output is all zeroes or not
2. IsNegative
    - Same problem, i was not able to check outPin's 15th bit, since it was an intermediate pin, nor out's 15th bit, 
    since it was the output bit. So, i created a class, to make it OR, and then take the sub-bus of the input pin.