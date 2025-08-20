## Challenge Description
You’re a hacker who discovered a strange binary file, `secret.bin`, that looks like a piece of computer code. 
It’s hiding a flag in hexadecimal text!

The `.bin` file extension tells us this file is a _binary_ file - it's meant for computers to read!
This challenge has two parts. The first involves using a tool called `strings` that looks for human-readable text in binary files.
Use it like this: `strings filename.bin`

Unfortunately, you'll have to do a bit more work to find the temporary `FLAG{...}`. 
You'll need to scroll through the output from `strings` until you find this content: "Binary file FLAG starts here: ... Flag ends".
Everything in between is your flag, but it is in hexadecimal format. You'll need to convert it back into English!
The tools on this machine are limited, one good option is to copy the hex flag to the GUI clipboard, and use that to copy it to your laptop's web browser. 
Go to a tool like cyberchef.com, paste that hex in, and use the Hex Decoder to get the temporary `FLAG{...}

## Challenge Steps
1. Navigate to `/home/ubuntu/Code-Cracker`
2. Use `strings` and a tool like cyberchef.com to extract the hex and translate it into the temporary `FLAG{...}`
3. Run `/challenge/verify` and enter the temporary flag to get your official `pwn.college{...}` flag!
