## Challenge Description
In this challenge, you will learn about Base64 decoding!
As with many other forms of cipher or encoding, to decode, just perform the steps in reverse!

### How It Works:

We will start with a base64 encoded string of `Q1VQ`.

#### 1. Convert Characters to 6-Bit

Using the [table](https://en.wikipedia.org/wiki/Base64#Base64_table_from_RFC_4648) linked to in the previous challenge, find the 6-Bit binary string for each character.

For this Base64 encoded string we get the following 6-Bit binary numbers:

```
Q = 010000
1 = 110101
V = 010101
Q = 010000
```

#### 2. Combine Those Binary Numbers

Now, we are to combine these binary numbers into one continuous string of characters, as follows:



#### 3. Split Into 8-Bit Chunks

Now, instead of collecting them into 6-Bits, we will collect them into 8-Bits:

```
01000011
01010101
01010000
```

#### 4. Convert Those Binary Numbers

We now take those three 8-Bit binary numbers, and convert them into three decimal (base 10) numbers. You can use google to do this for you if needed. The numbers we get should be:

```
01000011 = 67
01010101 = 85
01010000 = 80
```

#### 5. Convert The Decimal Numbers

Now, using those three ascii numbers, find the character they correspond to in the ascii chart! Then you should get your word!

```
67 = C
85 = U
80 = P
```

So, decoding `Q1VQ` we get the word `CUP` in all caps!


### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encode a secret word in Base64 and get the flag!
