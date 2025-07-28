## Challenge Description
In this challenge, you will **decode** a word using the Polybius Square! As a reminder, the Polybius Square is a 5x5 grid that maps each letter to a pair of numbers based on its row and column position. Your task is to take a sequence of number pairs and convert them back to the original letters to reveal the secret word.

### Polybius Square Table:
```
   1  2  3  4  5
1  A  B  C  D  E
2  F  G  H I/J K
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
```

For example, to decode the Polybius values `23 15 31 31 34`, we find the corresponding letters in the Polybius Square:
- 23 → H (row 2, column 3)
- 15 → E (row 1, column 5)
- 31 → L (row 3, column 1)
- 31 → L (row 3, column 1)
- 34 → O (row 3, column 4)

So, the decoded message is: `HELLO`

**Note:** Since I and J share the same cell (24), you may encounter ambiguity. For this challenge, assume the decoded letter is I unless context suggests otherwise.

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions to decode a secret Polybius Square message and get the flag!
