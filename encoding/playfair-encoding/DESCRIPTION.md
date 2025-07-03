## Challenge Description
In this challenge you will learn about the Playfair cipher!
The Playfair cipher is a manual symmetric encryption technique. It was invented by a man named Charles Wheatstone in 1854, but is named after Lord Playfair, because he promoted its use. 

### How It Works:

The Playfair cipher uses a 5x5 box, where each box contains a letter of the alphabet. Since there are 26 letters in the alphabet, the letter "J" is dropped, and "I" is used to represent both itself, and a "J". You will also choose a passphrase, and this special passphrase will take up the first few boxes, and then the rest will be filled in with the remaining alphabet, in order. 

Here is an example of what that 5x5 box would looke like with the passphrase: `PLYFAIR`

```
|P|L|Y|F|A|
|I|R|B|C|D|
|E|G|H|K|M|
|N|O|Q|S|T|
|U|V|W|X|Z|

NOTE: There is a keyword PLYFAIR that is used in the box. 
```

Using this box, I will walk through encrypting the word: `HELLO`.

*First*, divide the word you wish to encrypt into pairs of two characters. There are two cases we must look out for, though.
1. If our word has a double letter that would be paired together, you have to split them up and add a junk character in to finish the pair. (HALL would be split into HA, LX, LX)
2. If our word has an uneven amount of numbers, then the last pair will automatically get a "Z" to finish the pair. (BYE would be split into BY, EZ)

Following these guidlines, our word `HELLO` should be split like this: `HE`, `LX`, `LO`.

*Second*, we now utilize our 5x5 box to create a ciphered text. We will take each pair from the previous step, and identify where they exist on the grid. Based on their position we will do either 1 of 3 things:

1. If they are located in the same column, then each character will become the character that is under it. If the character is at the bottom, then you wrap around to the top. For example, if you were locating the character pair `AT` in the grid above, you will notice they are in the same column. This means that "A" would become "D", and "T" would become "Z". So, `AT` becomes `DZ`.

2. If they are located in the same row, then each character will become the character that is to the right of it. If your character is all the way right, then wrap around to the left side. For example, if you were locating the character pair `EM` in the grid above, you will notice they are in the same row. This means that "E" would become "G", and "M" would wrap around and become "E". So, `EM` becomes `GE`.

3. If they are NOT in the same row, and NOT in the same column, then you will make a rectangle with the squares. For example, if you were locating the character pair `WI` then to make a rectangle, the characters `B` and `U` will be selected. Then, the original characters become the added character that shares a row with it. So, "W" will become "U", and "I" will become "B". 

Putting these principles together, let's encrypt `HELLO`. 

```
HE will become KG
LX will become FV
LO will become RV
```

So, `HELLO` becomes `KGFVRV`

## Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encrypt a secret word and get the flag!
