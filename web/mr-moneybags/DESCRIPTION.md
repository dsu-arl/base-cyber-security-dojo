## Challenge Description
Unpopular opinion: Mr. Moneybags has too much money. Can you use the feedback form to convince him to donate to charity? 

### How It Works:
#### CSRF Vulnerabilities
Cross-Site Request Forgery (CSRF) vulnerabilities involve forcing a user to make a request from their browser that results in unwanted actions and may bypass same-origin security policies. They often occcur as a consequence of the sole use of session tokens to check which user is accessing an endopoint. CSRF payloads can be triggered in many ways, from phishing links to XSS payloads that redirect to the vulnerable endpoint. A simple example of a CSRF vulnerability could be an endpoint like `http://example.com/deleteAccount?auto-confirm=true` that only validates the user based on a session cookie. An XSS payload redirecting to that URL would cause any logged on user to delete their account if triggered on their machine.

(Note: POST requests can also be vulnerable to CSRF, but they might require slightly more complex payloads to trigger!)

## Challenge Steps
1. Start the challenge and use the "GUI Desktop Workspace" option
2. Navigate to the `/challenge` directory
3. Run `./verify` and `./run-moneybags`
4. Open the web browser and navigate to `http://127.0.0.1:5000` by typing it into the URL bar. This is the page for the feedback form.
5. Open the web browser and navigate to `http://127.0.0.1:5555` by typing it into the URL bar. This is the page Moneybags uses for banking and checking feedback.
6. The flag will be given at `http://127.0.0.1:5555/` once Moneybags has donated all his money to charity.