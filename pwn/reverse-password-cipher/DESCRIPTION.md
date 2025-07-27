## Challenge Description
This challenge is more complex than the other reversing password challenges. This time a cipher alphabet is used to encipher a plaintext phrase. Your challenge is to identify what cipher alphabet was used to generate the cipher text and discover the plaintext phrase. This phrase is used to retrieve the flag.

## How it Works
Substitution ciphers are one of the oldest ways to encode text. This challenges uses a simple rotation of the alphabet to generate a 'cipher'bet that encodes plaintext to generate ciphertext. This challenge provides a way to generate alphabets to decipher the ciphertext back into plaintext. It also allows you to play with different substitution ciphers and see how different plaintext is encoded into ciphertext.


### Steps To Substitution
First you must have an alphabet to generate text from. This can be the standard 26-letter alphabet taught in the U.S., or it can be expanded to include special characters like '\*', '?', or '\}': the sky is the limit to what constitutes an alphabet! The important thing is that the same alphabet used to generate your plaintext *must* be used in the enciphering and deciphering phases, discussed later.

Lets assume you want to encipher the phrase "hello world!". The letters that *must* constitute your alphabet are: 'd', 'e', 'h', 'l', 'o', 'r', 'w', '!', ' '. Notice how every letter used in the phrase "hello world!" appears exactly once in the alphabet, including spaces. We will use the full alphabet, and add the special characters to the end for simplicity. This results in the alphabet: ```'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','!'```

If we wanted to create a cipher, we can rotate our alphabet by a number to generate a **new** alphabet, the cipherbet, that we can use to generate our ciphertext. Lets say we rotate our alphabet to the right by 2, this would generate the cipherbet ```' ','!','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'```. Notice how the last 2 characters rotate around to the front: this is very important! No letters can be lost otherwise we couldn't encipher them!

With the cipherbet generated, we can generate our ciphertext. Simply line up the two alphabets, and follow the plaintext letter down to find its cipherbet counterpart. In this way, "h" in the alphabet translates to "f" in the cipherbet, "e" to "c", and so on until you get the ciphertext "fcjjmyumpjbz".
```
alphabet:  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','!'
                            |           |
                            2           1
                            |           |
cipherbet: ' ','!','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
```
To go from the ciphertext to the plaintext, you must know the number of rotations used to generate the cipherbet. If you don't, you must guess-and-check until you find the correct cipherbet. Then the process works in reverse. Line up the two alphabets and go from the cipherbet letter to the alphabet letter until you get the plaintext.

## When You're Done
Your goal is to identify how many times the alphabet must be rotated to generate the correct cipherbet, which is then used to decode the ciphertext. The ciphertext is comprised of human-readable text: there will be no mistaking the correct passphrase when it is retrieved. Once you have obtained the plaintext passphrase, enter it into the ```verify.py``` script to retrieve the flag.

## Challenge Steps
1. Open a terminal in the Desktop
2. Navigate to the ```/challenge``` directory (Hint: Type ```cd /challenge``` and press ```Enter```)
3. Use the ```ls``` command to find the challenge file (Hint: it is NOT the DESCRIPTION.md file)
4. To run the challenge, type the filename and press ```Enter```.
5. Submit your flag!