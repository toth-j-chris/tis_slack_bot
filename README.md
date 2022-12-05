# tis_slack_bot
## (!WIP!) Steps to Install
### Clone this repo to a local directory
git clone https://github.com/toth-j-chris/tis_slack_bot.git
### Get dependencies
1. Change directories to where you cloned the repo
> cd tis_slack_bot
2. (Optional) Create a virtual environment
> python3 -m venv ./venv
3. (If you did step 2) Activate the virtual environment
> source venv/bin/activate
4. Install the dependencies with pip
> pip install slack_bolt python-dotenv requests
### Create a file called ".env" 
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