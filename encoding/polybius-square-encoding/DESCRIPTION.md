## Challenge Description
In this challenge, you will learn about **Polybius Square Encoding**! The Polybius Square is a simple substitution cipher that uses a 5x5 grid to encode letters by mapping each one to a pair of numbers based on its row and column position. Traditionally used for secure communication, it’s an engaging way to transform text into numerical codes.

### How It Works:
The Polybius Square is a 5x5 grid containing the letters of the alphabet (with I and J typically sharing a cell due to the 25-cell limit). Each letter is represented by two numbers: the first for its row and the second for its column.

**Polybius Square Table:**
```
   1  2  3  4  5
1  A  B  C  D  E
2  F  G  H I/J K
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
```

For example, to encode the word "HELLO":
- H (row 2, column 3) → 23
- E (row 1, column 5) → 15
- L (row 3, column 1) → 31
- L (row 3, column 1) → 31
- O (row 3, column 4) → 34

So, "HELLO" in Polybius Square encoding is: `23 15 31 31 34`

**Note:** Since I and J share the same cell (2,4), they both encode to 24. During decoding, context or convention (e.g., assuming J if rare) may be used to disambiguate.

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encode a secret word using the Polybius Square and get the flag!