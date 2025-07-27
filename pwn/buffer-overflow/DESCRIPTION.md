## Challenge Description
Software vulnerabilities are everywhere! Don't let the futuristic date of 2025 mislead you; headlines abound of software vulnerabliities plaguing even the most advanced companies. This challenge will introduce you to the humble buffer overflow, but don't let its simplicty fool you! It is the bread and butter of even sophisticated attacks used today.

## How it Works
Run the program ```buffer_overflow``` and follow the prompts. You will need to enter a very specific number of characters to cause the buffer overflow to occur. This program is written so that once you reach the correct number of characters, it will automatically trigger the vulnerability: no debuggers necessary for this one! In "the real world" entering the correct number of characters would only be the first step, then you'd have to find the memory address you want to go to; but that is a challenge for a different day.

## When You're Done
You are done when the ```buffer_overflow``` program emits a string; there will be no mistaking what is the correct string. When you've received it, copy the string and run ```python verify``` and paste the value at the prompt. You will receive a flag that you will use in pwn.college to complete the challenge.

## Challenge Steps
1. Open a terminal in the Desktop
2. Navigate to the ```/challenge``` directory (Hint: Type ```cd /challenge``` and press ```Enter```)
3. Use the ```ls``` command to find the challenge file (Hint: it is NOT the DESCRIPTION.md file)
4. To run the challenge, type the filename and press ```Enter```!
5. Submit your flag!