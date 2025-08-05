## Challenge Description
You have a huge text file, `haystack.txt`, with a needle (flag) hidden inside. Use `grep` to search for the temporary flag, which looks like `FLAG{...}`. (NOTE: This is not your real flag yet!)

For more information about `grep`, you can head over to the Linux module and do the "Find the password!" challenge. For a quick refresher, `grep` is used like this: `grep {target_string} {file_to_search}`.

## Challenge Steps
1. Start the challenge and open a terminal
2. Navigate to the `/challenge` directory (use `cd /challenge`)
3. Search through the `haystack.txt` file to find the _temporary_ flag (`FLAG{...}`)
4. Once you've found the `FLAG`, run `/challenge/verify`, enter the temporary flag, and receive your official `pwn.college{...}` flag!
