Back in 2011, version 2.3.4 of an FTP (File Transfer Protocol) server called **vsFTPd (Very Secure FTP Daemon)** was discovered to have a serious security vulnerability — a backdoor that allowed an attacker to gain full control of the server.

This vulnerability was introduced when a malicious version of vsFTPd 2.3.4 was uploaded to the official distribution site. The backdoor allowed unauthorized remote command execution by simply appending ":)" (a smiley face) to the end of the username field when logging in. If an attacker used this trick, they could instantly open a root shell, giving them the highest level of control over the system.

In this challenge, you will exploit this vulnerability in a controlled environment to understand how it works. Run `/challenge/verify` to get your instructions.
