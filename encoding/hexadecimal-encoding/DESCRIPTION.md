## Challenge Description
In this challenge, you will learn about Hexadecimal Encoding!
Hexadecimal is a different way to represent numbers. Our typical way of representing numbers is called base-10. This uses the numbers 0-9, which is ten digits in total. Hexadecimal uses 0-f, which is 16 digits in total. It goes 0-9, and then a-f. To represent the number 5 in hexadecimal, it would still just be 0x5. To represent the number 11 in hexadecimal, it would be the character 0xb. To represent the number 405 in hexadecimal, it would be 0x195. Notice that with hexadecimal, you put '0x' in front of the number to denote the fact you are using hexadecimal counting. Since, hexadecimal uses characters in it's digits, the hex number 0xdeadbeef is a valid number which equates to our base-10 number 3735928559.

### How It Works:

Hexadecimal encoding works the same as ASCII encoding. Each hex number is assocaited with a character.

Hex Table (note the '0x' has been ommited for space):
```
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55 56 57 58 59 5A

a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 78 79 7A
```

Another way you could encode Hex is by converting the Hex digit, into its base-10 decimal digit, and then use the ascii table found in the ascii challenge.


### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encode a secret word in Base64 and get the flag!
