## Challenge Description
You’re a spy who found a picture of a suspicous dog, `suspicious_doggo.jpg`, but it’s hiding a secret message! 
You will need to use the `steghide` tool to find the flag hidden in this image file.

Step one is to find a passphrase hidden in the `secret.txt` file. 
When data is embedded in a file, it sometimes uses a password to protect that hidden data. 
You will need to search through `secret.txt` to find the password used to embed data in `suspicious_doggo.jpg`.
(Hint: search for the filename!)

#### steghide
`steghide` is a command-line tool used for _steganography_, which means hiding data within other files.
With this tool, you can embed or extract hidden data from a file. For our purposes, you will only need to _extract_ secret data.

If you run `steghide --help`, you will see all of the different options available. 
Listed below are the most helpful options for this challenge:
- `--extract`: used to extract secret information from a file - saves it to a file
- `-p {passphrase}`: lets you enter the password needed to extract the data correctly (the password you found in `secret.txt`)
- `-sf {filename}`: lets you choose the "stego file", the file with hidden data in it
- `-xf {filepath/filename}`: lets you choose where the extracted file is saved to

All together, it will look something like: 

`steghide --extract -p {password} -sf {suspicious_file} -xf /home/hacker/temp_flag.txt`

**Important**: use `-xf` to change the output file to `/home/hacker/temp_flag.txt`. Just trust us, it will make your life easier.
This output file contains your temporary `FLAG{...}`!

## Challenge Steps
1. Navigate to the `/home/ubuntu/Secret-Message-in-Photo` directory
2. Find the password in `secret.txt`
3. Use `steghide` and the password you found to extract the hidden data from `suspicious_doggo.jpg` and save it to `/home/hacker/temp_flag.txt`
4. Move back to your home directory (`cd`), and run `cat temp_file.txt` to find your temporary `FLAG{..}`
5. Run `/challenge/verify`, enter your temp flag, and receive your official `pwn.college{...}` flag!
