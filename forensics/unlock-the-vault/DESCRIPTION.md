## Challenge Description
You're a treasure hunter who found a locked vault! A file named `vault.zip` has been placed in your `/challenge` directory. Your goal is to unlock this vault and find the treasure (flag) inside!

#### Zip files
You may have noticed the `.zip` file extension. This file has been "zipped", or compressed.
"Zipping" files together is a way to gather them all and squish them together so they take up less space. There could be just one file, or several that have been zipped together.

To unzip a `.zip` file, you can typically use this command: `unzip filename.zip`

This normally works with no problem. However, in our virtual machine, you will not have permission to unzip this file within the `/challenge` directory. You will need to add the `-d` _destination_ flag to the `unzip` command. This tells the computer to place the extracted files into a different directory - you'll want to use your home directory `/home/hacker`. It will look something like this: `unzip filename.zip -d /path/to/destination`

This will open up that zipped file, and give you the full information that was compressed inside. If you run `ls` in your home directory after `unzip`, you should see some new files that weren't there before!

Unfortunately, this vault is also locked with a password - in order to unzip it, you will need to find that password (you'll get a prompt to enter the password when you run `unzip`).

## Challenge Steps
1. Navigate to the `/challenge` directory, run `ls` to view all of the challenge files
2. Use `grep` to search the `vault_clue.txt` file for the *password* (For help with `grep`, check out the previous challenge, or go to the Linux Module -> "Find the password!")
3. Use the password you found to unzip `vault.zip` into your home directory `/home/hacker` (note that it will not look like you are typing a password, but you are! Just type it and press Enter)
4. You should now have a `vault.txt` file, in your home directory. This file contains a temporary flag: `FLAG{...}` (use `cat` to view the flag)
5. Run `/challenge/verify` and enter the temporary flag from `vault.txt`, and you will receive your offical `pwn.college` flag!

