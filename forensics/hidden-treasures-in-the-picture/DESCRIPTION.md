## Challenge Description
You're a digital archaeologist exploring a mysterious image, `treasure.jpg`, rumored to hide a valuable flag. 
To keep it safe, this flag has been split into four separate pieces.
Your goal is to find these four pieces and reunite them!

The pieces of the flag will look like this: `Part 1: ...`, `Part 2: ...`, `Part 3: ...`, `Part 4: ...`
Keep track of each part as you find it, then put them all together like this: `FLAG{part1+part2+part3+part4`
You'll need to use this temporary flag to unlock your official `pwn.college` flag!

## Challenge Steps
1. Navigate to the `/home/ubuntu/Hidden-Treasure-in-Picture` directory
2. Use the tools you've learned so far to find the 4 parts! (`steghide`, `exiftool`, `binwalk`, `strings`, and `grep` may come in handy)
    Note: Make sure to use `-xf /home/hacker/extracted.txt` when using `steghide`!
3. Put the 4 parts together to find your temporary `FLAG{...}`
4. Run `/challenge/verify`, enter your temporary flag, and receive your official `pwn.college{...}` flag!
