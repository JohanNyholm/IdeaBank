# IdeaBank
A simple command line tool for storing ideas into a google sheet


## Setup
1. Make sure you have Python 2.6 or greater as well as pip installed.

2. Run `$ pip install --upgrade google-api-python-client` in order to install the prerequisites

3. Go to https://developers.google.com/sheets/api/quickstart/python and follow **Step 1** until you have obtained a *client_secret.json* file. Make sure to name it just *client_secret.json*

4. Paste the *client_secret.json* file into the IdeaBank root directory

5. Make sure the file *idea* is executable, for example using chmod.

6. Create an empty sheet in your google drive and copy the URL to your clipboard.

7. Run `$ idea --setup` and paste the URL of the sheet when it is requested.

8. You are now set up!