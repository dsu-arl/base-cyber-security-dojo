## Challenge Description
You are a security analyst tasked with investigating a network breach. A packet capture (PCAP) file, rogue_user.pcap, has been provided, containing evidence of an attacker’s activity on a compromised system. Your objective is to analyze the network traffic using Wireshark to identify the rogue user account created by the attacker and the password set for this account.

#### Hints
1. Start by examining the Protocol Hierarchy in Wireshark to identify protocols likely to carry command-line activity.
2. Look for TCP streams containing "Data" that might indicate remote shell access.
3. Focus on commands like adduser or interactions with system files such as /etc/shadow.
4. Pay attention to TCP streams with commands and their outputs to find the user creation details.


## Challenge Steps
1. Navigate to the `/home/ubuntu/` directory
2. Open the rogue_user.pcap file using wireshark
3. Run `/challenge/verify` and enter the username and password you found.
4. Enter the username and password in this format: username:password.
5. Submit your official `pwn.college{...}` flag!