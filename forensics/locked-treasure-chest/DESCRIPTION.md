## Challenge Description
You found a digital treasure chest (`digital_treasure.zip`) that is hiding another zip file inside of it. The flag is contained within the _metadata_ of this inner zipped file (`treasure.zip`). 

#### Metadata
Metadata in ZIP files refers to information _about the files inside the archive_, rather than the file contents themselves. 
This includes things like:

- File names
- File sizes (compressed & uncompressed)
- Compression method
- Timestamps (modification date/time)
- File permissions
- File path (relative inside the archive)
- Comments (added by whoever zipped the file, contains notes like version or author information)

This metadata helps systems know how to extract the files correctly and what to do with them.

You can view metadata with a tool like `zipinfo`. Try running `zipinfo treasure.zip` to see what default information it gives you. From there, run `zipinfo -h` (`-h` for help) to see what flags you can use with `zipinfo` to view more information. Play around with these flags until you find your temporary `FLAG{...}`

## Challenge Steps
1. Navigate to the `/challenge` directory
2. Unzip `digital_treasure.zip` into your home directory (no password needed this time!)
3. In your home directory, use the `zipinfo` tool on `treasure.zip` to find the temporary flag (`FLAG{...}`)
    (Do NOT unzip it! You'll lose the flag!)
4. Run `/challenge/verify` and enter the temporary flag you found
5. Submit your official `pwn.college{...}` flag!
