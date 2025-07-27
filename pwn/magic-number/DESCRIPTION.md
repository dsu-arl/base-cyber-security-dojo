## Challenge Description
This challenge contains four different numbers that are randomly chosen as the 'secret' number. Each execution of the program chooses a different one of the four as the 'secret' number. The goal of this challenge is to enter the correct 'secret' number and retrieve the token. There are several techniques you can use to get the correct number(s), which one you learn is up to you!

## How it Works
Run the program ```magic_numbers``` and you will see the prompt ```Please guess the number between 1 and 1000:```. Enter a number and you will either have guessed correctly or incorrectly! Guessing correctly will result in a token printing to the screen that you must use to retrieve the token. And remember, each time you run the program it will select a different number! So be persistent! You could have the right number, but it wasn't selected this time.

### Strings
One of the easiest ways to retrieve information from a program in Linux is to use the command line tool ```strings```. This command analyzes the program and prints all of the strings to the screen: but beware! What a computer thinks is a string isn't always what humans think of as strings. To use this command you must provide the program to retrieve strings from: ```strings magic_numbers``` for example. This challenge not only contains four different numbers, but it also contains strings that represent those numbers. For example, if the four numbers were ```0, 1, 2, 3``` there would be four strings ```zero, one, two thee``` in the output from ```strings```. But there are lots of other 'strings' in the program too, so it will take some time to find the correct values.

### GNU Debugger
One of the more challenging, but precise, ways to solve this challenge is to use a debugger. Debuggers are very sophisticated and complex tools that allow people to see *exactly* how a program makes decisions. Using debuggers requires a level of knowledge that is not within the scope of this training, but can with a little know-how quickly find the solution. GDB is a debugger available in Linux that can inspect ```magic_numbers``` and find the exact function call that selects and returns one of the 'secret' numbers. A very basic introduction can be found [here](web.eecs.umich.edu/~sugih/pointers/summary.html).

Debuggers are very powerful tools. Using a debugger you can look at the code for the entire program, not just the code executing. In this way, you could find the token that is displayed when you enter the correct number, even if you didn't!

## When You're Done
You are done when the ```magic_numbers``` program emits a string; there will be no mistaking what is the correct string. When you've received it, copy the string and run ```python verify``` and paste the value at the prompt. You will receive a flag that you will use in pwn.college to complete the challenge.

## Challenge Steps
1. Open a terminal in the Desktop
2. Navigate to the ```/challenge``` directory (Hint: Type ```cd /challenge``` and press ```Enter```)
3. Use the ```ls``` command to find the challenge file (Hint: it is NOT the DESCRIPTION.md file)
4. To run the challenge, type the filename and press ```Enter```!
5. Submit your flag!