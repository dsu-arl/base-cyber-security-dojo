## Challenge Description
In this challenge, you will learn about decoding messages using the Rail Fence (Zigzag) Cipher! As a reminder, the Rail Fence Cipher is a transposition cipher that arranges the plaintext in a zigzag pattern along a specified number of "rails" (rows) before reading it off row by row to create the ciphertext. Now, you'll learn how to reverse this process to decode messages.

### How It Works:

To decode a Rail Fence Cipher message, we need to reconstruct the zigzag pattern using the number of rails and the ciphertext. The key to this cipher is the number of rails used. The number of rails must be at least 2 and less than the length of the ciphertext.

#### Determining the Number of Rails:
When you're given a ciphertext without knowing the number of rails, you can try different numbers of rails until you find one that produces a readable message. Here's how to approach it:

1. Start with 2 rails and work your way up
2. For each number of rails:
   - Calculate how many letters should be in each row
   - For a message of length L and R rails:
     - First row: L ÷ (2R-2) letters (rounded up)
     - Middle rows: 2 × (L ÷ (2R-2)) letters
     - Last row: L ÷ (2R-2) letters (rounded down)
3. Try reconstructing the message with these calculations
4. The correct number of rails will produce a readable message

For example, with a 5-letter message "CRYEB":
- With 2 rails: First row gets 3 letters, second row gets 2 letters
- With 3 rails: First row gets 2 letters, second row gets 2 letters, third row gets 1 letter
- With 4 rails: First row gets 2 letters, middle rows get 1 letter each, last row gets 1 letter

For example, let's decode the ciphertext "CRYEB" using 3 rails:

1. First, we need to determine the pattern of the zigzag:
```
C . . . R
. Y . E .
. . B . .
```

2. Then, we fill in the letters from the ciphertext in the correct positions:
   - First row: C R
   - Second row: Y E
   - Third row: B

3. Finally, we read the message by following the zigzag pattern:
   - Start at the top left (C)
   - Move diagonally down to the second row (Y)
   - Move diagonally down to the third row (B)
   - Move diagonally up to the second row (E)
   - Move diagonally up to the first row (R)

So, "CRYEB" decoded with 3 rails becomes: `CYBER`

The Rail Fence Cipher is a simple transposition cipher that doesn't change the letters themselves, only their positions. While it provides some level of obfuscation, it's not considered secure for modern cryptographic purposes as it can be easily broken through pattern analysis.

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to decode a secret word using the Rail Fence Cipher and get the flag!

*HINT: It might be useful to open a text file to draw out the zigzag pattern and your answer before submitting.*
