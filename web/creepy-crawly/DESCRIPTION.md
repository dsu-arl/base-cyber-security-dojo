## Challenge Description
YOU'LL NEVER FIND THE FLAG IN MY WEB OF SPIDERS!!!!! AHAHAHAHAHAA

### How It Works:
For this challenge you'll be using a slightly older version of Burp because it has some useful web crawling capabilities that moved to Professional edition in newer versions. The general idea of how the Burp UI works is the same -- it will just look slightly different.

After getting Burp and the challenge page up and running (via `/challenge/burp.sh` and `/challenge/verify`), navigate to the page at `127.0.0.1:5000`.

This challenge will require you to use the Spider tool to automatically map out all of the links of the site. While there is a tab for Spider on Burp, the simplest way to use the tool is to open the challenge homepage, then right click on it in the Burp sitemap from the "Target" tab and click "spider this host". 

Newer versions of Burp Community only support passive crawling, which is why we are using an older version.

## Challenge Steps
1. Navigate to the `/challenge` directory
2. Run `./verify`
3. Find a way to print the flag!