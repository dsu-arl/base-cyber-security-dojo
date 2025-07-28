## Challenge Description
In this challenge, you will learn about Base64 Encoding!
Base64 is a group of binary-to-text encoding schemes that transforms binary data into a sequence of printable characters, limited to a set of 64 unique characters. More specifically, the source binary data is taken 6 bits at a time, then this group of 6 bits is mapped to one of 64 unique characters.

### How It Works:

Encoding in Base64 is a multi-step process that also involves getting the ascii decimal number for a character, converting that decimal number into binary, and then using a Base64 table to find the character you need. I will walk through these steps in more detail using the word "FORK" which contains all capital letters. 

#### 1. Convert Each Character to their Ascii Number (Base 10)

If you did the ascii cryptography challenge, this should be familiar to you. We want to get the ascii number associated with each letter in the word "FORK". That gets us the following numbers:

```
F = 70
O = 79
R = 82
K = 75
```

#### 2. Convert Those Ascii Numbers to Binary (8-bits)

There are many websites that can convert decimal (base 10) numbers to binary (base 2). You can google "70 in binary" and google will display the results for you. They may give it to you in 7-bits. Which means we need to just add a 0 to the start to make it a total of 8 bits. Converting all of our ascii numbers from the previous steps gives us these binary numbers:

```
70 = 01000110
79 = 01001111
82 = 01010010
75 = 01001011
```

#### 3. Combine Those Binary Numbers

In this step, we want to take our binary numbers from the previous step, and put them into ONE continuous string of numbers. Since each character from the original word "FORK" consists of 8-bits, the total length of this string will be 32-bits.

`01000110010011110101001001001011`

#### 4. Split Into 6-Bit Chunks

Now that we have our long string consisting of 0's and 1's, we want to split them into 6-Bit chunks, as opposed to the original 8-Bit chunks they were in. This will look something like this:

```
010001
100100
111101
010010
010010
11
```

Notice that we have two extra Bits at the end. In this case, we need to pad it out to fit 6-Bits. To do that, we can just add 0's AFTER the two bits that are already there. This should give us something like this:

```
010001
100100
111101
010010
010010
110000
```

#### 5. Convert The 6-Bit Binary

The Base64 6-Bit conversion chart can be found [here](https://en.wikipedia.org/wiki/Base64#Base64_table_from_RFC_4648). Now, all you have to do is match the 6-Bit binary string to the appropriate character.

In this case, these 6-Bit binary numbers come out to:

```
010001 = 'R'
100100 = 'k'
111101 = '9'
010010 = 'S'
010010 = 'S'
110000 = 'w'
```

HOWEVER, remember that we padded '11' with 4 0's in the last step. If we just give someone the string 'Rk9SSw' it won't decode properly because it doesn't account for the padding that we added. To let someone know that we padded our initial data, we need to add an equal sign ('=') for every two zeroes we added. Since we padded our original data with 4 0's, we will add TWO equal signs.

So, "FORK" in base64 comes out to be: `Rk9SSw==`

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encode a secret word in Base64 and get the flag!
