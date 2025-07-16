## Challenge Description
For this one I'll just give you the flag. All you have to do is ask nicely.

### How It Works:
This challenge serves as an intro to PortSwigger's Burp Suite tool. Burp is a web hacking tool with many features, such as:
- The ability to intercept and modify HTML requests/responses
- Automated site mapping/crawling
- Features for fuzzing request parameters, attack payloads, etc
- Compatibility with additional extensions

The machine given has already been set up with a browser configured to use Burp. Normally, you would need to go into the browser's proxy settings and set up a proxy for `127.0.0.1:8080` to direct traffic through the tool. As stated before, this has already been done for you!

First, get the challenge page running via `/challenge/verify`. Afterwards, open a new terminal tab/window and launch Burp with the command `/challenge/burp.sh`. Click the default selections (highlighted in orange) until you get to the main Burp menu. Then, click on the `Proxy` tab. You won't need to leave this tab to complete the challenge. 

Turn on Intercept in the top left -- this will catch each request and response sent from/to your browser and hold them in Burp until you forward them manually. Before being forwarded, they can be modified as well! Simply type into the text of the request inside of Burp before forwarding. If you just want to navigate the web without dealing with forwarding every request, turn Intercept off. Note that messages can still be seen in the "HTTP History" sub-tab of Proxy. 

With Burp running, you now have all the required knowledge to open and complete the challenge at `127.0.0.1:5000`! Note that you will need to open the browser the normal way -- the "Open Browser" button in Burp doesn't work in this environment.

## Challenge Steps
1. Start the challenge and use the "GUI Desktop Workspace" option
2. Navigate to the `/challenge` directory
3. Run `./verify`
4. Open a new terminal tab/window and open Burp with `./burp.sh`
5. Open the web browser and navigate to `127.0.0.1:5000` by typing it into the URL bar
6. Use Burp to obtain the flag!
