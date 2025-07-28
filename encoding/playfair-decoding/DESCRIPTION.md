## Challenge Description
In this challenge you will learn about decoding a Playfair cipher.

### How It Works:

To decode the playfair cipher, you need to have the passphrase that was used to encode it so that you can recreate the 5x5 grid. Then, from there, you will take your encoded word, split it up into two-character pairs, and then go through and do the reverse of the steps mentioned in the encoding challenge. 

```
|P|L|Y|F|A|
|I|R|B|C|D|
|E|G|H|K|M|
|N|O|Q|S|T|
|U|V|W|X|Z|

NOTE: There is a keyword PLYFAIR that is used in the box. 
```

For example, decoding the ciphertext `KGFVRV` would look something like this:

- KG -> HE (Notice, we go to the character on the left, instead of the right when decoding.)
- FV -> LX (This case functions the same as encoding.)
- RV -> LO (Notice, we go to the character above instead of below when decoding.)

This gives us the unciphered text `HELXLO`. The extra character `X` is added as a pad during encoding, so the true text is `HELLO`. 

So, `KGFVRV` becomes `HELLO`!

## Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encrypt a secret word and get the flag!
