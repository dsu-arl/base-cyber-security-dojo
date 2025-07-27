## Challenge Description
This challenge is very similar to ```reversePassword.py``` but with an added twist. You must follow the program's call structure again (remember to pay attention to details) but a new wrinkle is introduced.

## How it Works
Again there are functions that you must analyze to find the password, however the lists containing the characters are occasionally reversed! In Python this is represented by the syntax ```[::-1]```. This is used to reverse the contents of a list; an example is shown below.
```
# The list is first created
myList = list((1, 2, 3))
>>> [1, 2, 3]

# Then the list is reversed
myList[::-1]
>>> [3, 2, 1]

# The revered contents can be stored in a new variable
reversedList = myList[::-1]
reversedList
>>> [3, 2, 1]
```

There are four functions utilized in this program to generate the password. Each function uses some variation of the two lists (```alphabet``` and ```special_char```) to create the password. Once again, attention to detail is the key to solving this challenge. Running the program will output the starting lists.

## When You're Done
When you have finished your analysis, follow the steps in the Challenge Steps section below.

## Challenge Steps
1. Select the "VSCode Workspace" option from the challenge menu.
2. Open a file by pressing ```ctrl```+```o``` and in the text field type ```/challenge/backwardPassword.py```.
3. Read the source code to identify the password.
4. When you have the password open a terminal by pressing ```ctrl```+```~``` and in the terminal type ```cd /challenge```.
5. Run ```python verify``` and enter the password to retrieve the flag.