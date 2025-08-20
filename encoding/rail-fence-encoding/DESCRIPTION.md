## Challenge Description
In this challenge, you will learn about the Rail Fence (Zigzag) Cipher! The Rail Fence Cipher is a transposition cipher that arranges the plaintext in a zigzag pattern along a specified number of "rails" (rows) before reading it off row by row to create the ciphertext.

### How It Works:

The Rail Fence Cipher works by writing the message in a zigzag pattern across a specified number of rails, then reading the message row by row. The key to this cipher is the number of rails used. The number of rails must be at least 2 and less than the length of the plaintext.

For example, let's encode the word "CYBER" using 3 rails:

```
C . . . R
. Y . E .
. . B . .
```

1. First, we write the message in a zigzag pattern:
   - First letter (C) goes on the first rail
   - Second letter (Y) goes on the second rail
   - Third letter (B) goes on the third rail
   - Fourth letter (E) goes back up to the second rail
   - Fifth letter (R) goes back to the first rail

2. Then, we read the message row by row:
   - First row: C R
   - Second row: Y E
   - Third row: B

So, "CYBER" encoded with 3 rails becomes: `CRYEB`

The Rail Fence Cipher is a simple transposition cipher that doesn't change the letters themselves, only their positions. While it provides some level of obfuscation, it's not considered secure for modern cryptographic purposes as it can be easily broken through pattern analysis.

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encode a secret word using the Rail Fence Cipher and get the flag!

*HINT: It might be useful to open a text file to type out the zigzag pattern and your answer before submitting.*