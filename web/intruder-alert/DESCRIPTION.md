## Challenge Description
We know the page is insecure to XSS, but it shouldn't matter since it's so annoying to figure out which spot the vulnerability is in.

### How It Works:
Now that you have a basic knowledge of Burp, let's take a look at the Intruder tool.

After getting Burp and the challenge page up and running (via `/challenge/burp.sh` and `/challenge/verify`), navigate to the page at `127.0.0.1:5000` and test out the form.

After sending a request to the `tryXSS` endpoint, you can view it in Burp via the `Proxy->HTTP History` window or in the `Target` window. Right click on the request and hit `Send to Intruder`. Afterwards, the Intruder tab should be highlighted -- after clicking on it, you'll be able to see the same request.

BurpSuite's Intruder tool is meant to automate testing of paylaods within different locations of a request. While configuring Intruder, the `§§` symbols that can be added via the buttons signify where payloads will be placed. There are a few different types of attacks that can be set as well -- `Sniper` is the default, and Burp has straightforward explanations of each one built into the dropdown menu.

Payloads can be configured in the right-hand side of the Intruder page. For this challenge, a simple payload list has been given. You can find it at `/challenge/payloads`.

After starting the attack, Burp will notify you that the Community edition is limited, then provide a window with information about each request and response. After the attack is complete, you can try to find requests that triggered vulnerabilities by sorting through the response lengths and looking for abnormalities. Be careful when submitting your answer for the challenge -- any incorrect answer will shuffle the vulnerability around, requiring you to run the attack again!

## Challenge Steps
1. Start the challenge and use the "GUI Desktop Workspace" option
2. Navigate to the `/challenge` directory
3. Run `./verify`
4. Open a new terminal tab/window and open Burp with `./burp.sh`
5. Open the web browser and navigate to `127.0.0.1:5000` by typing it into the URL bar
6. Use Burp to obtain the flag!