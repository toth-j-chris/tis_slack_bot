# tis_slack_bot
## Steps to Install
CLI commands are preceded by a '$'
### Clone this repo to a local directory
> $ git clone https://github.com/toth-j-chris/tis_slack_bot.git
### Get dependencies
1. Change directories to where you cloned the repo
> $ cd tis_slack_bot
2. (Optional) Create a virtual environment
> $ python3 -m venv ./venv
3. (If you did step 2) Activate the virtual environment
> $ source venv/bin/activate
4. Install the dependencies with pip
> $ pip install slack_bolt python-dotenv requests
### Create a file called ".env" in the root of the cloned project
> $ cd tis_slack_bot\n
> $ touch .env
### Create a Slack workspace to install the app in
1. [Create a Slack account](https://slack.com/signin#/signin)
2. Click on "Create a Workspace"
3. Follow the prompts until you are in the workspace that you created
### Create a Slack app in your workspace
1. Go to this URL: https://api.slack.com/apps?new_app=1&ref=bolt_start_hub
2. In the "Create an app" modal, click "From Scratch"
3. Give the app a name, and add it to the workspace you created in the previous step
4. Click "Create App"
### Generate a Bot token
1. After creating your app, you should be taken to it's config on the "Basic Information" page
2. Click "OAuth & Permissions" in the left sidebar
3. Scroll down to "Scopes" and click "Add an OAuth Scope" under "Bot Token Scopes"
4. Add the "channels:history" and "chat:write" scopes 
5. Scroll back to the top of the OAuth and Permissions page and click the "Install to Workspace" button
6. Click "Allow" when prompted to install to your workspace with the permissions required.
7. When redirected back to the OAuth page, there should now be a Bot User OAuth Token at the top
8. Copy the token and add the following line to your .env file created earlier, replacing [Bot User OAuth Token] with your token. It's important that you use the same variable name
> SLACK_BOT_TOKEN=[Bot User OAuth Token]
### Generate an App Token
1. While still in your App's config, click "Basic Information" in the left sidebar 
2. Scroll down to "App-Level Tokens" and click "Generate Token and Scopes"
3. Give the token a name like "socket-mode-token" and add the "connections:write" scope
4. Click generate, then copy the token that is generated
5. Add the token to you .env file like so, replacing [App-Level Token] with your token
> SLACK_APP_TOKEN=[App-Level Token]
### Enable Socket Mode
1. Click "Socket Mode" in the left sidebar
2. Toggle "Enable Socket Mode" on under the "Connect using Socket Mode" section
### Subscribe your app to Events
1. Click "Event Subscriptions" in the left sidebar
2. Toggle "Enable Events" on
3. Expand the "Subscribe to bot events" tab
4. Click "Add Bot User Event" and select "message.channels"
### Generate a Virustotal API Key
1. Go to https://www.virustotal.com/gui/sign-in
2. Create an account or sign into an existing account
3. Click your profile name in the top right and select "API Key" from the dropdown menu
4. Copy the API key on this page and add it to your .env file like so, replacing [Virustotal API Key] with your key
> VIRUSTOTAL_API_KEY=[Virustotal API Key]
### Add the App to a channel
1. Go back to your slack workspace and you should now see your app under the "Apps" section of the left sidebar
2. Find a channel that you would like to add the app to and type "@[App Name]", replacing [App Name] with the name of your app
3. Click "Add to Channel" in the popup
### Run the App
1. Change directories to the cloned directory
> $ cd tis_slack_bot
2. Activate the virtual environment (if it was deactivated before, or if in a new shell session)
> $ source venv/bin/activate
3. Run the application
> $ python src/main.py
### Test it out
1. In your slack workspace, go to the channel that you added the bot to
2. Send a message that includes a valid ipv4 address, or multiple, in dot-decimal notation (e.g. "1.1.1.1", "127.0.0.1")
3. The bot will reply to your message with some data about the address, from Virustotal
### Additional reference material
1. More info about creating and configuring the app can be found here: https://api.slack.com/start/building/bolt-python
2. More info about Socket Mode can be found here: https://api.slack.com/apis/connections/socket
3. This was built and tested using python 3.8.10. Later versions should work, but are not strictly supported