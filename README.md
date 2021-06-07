# Rotmg 

ROTMG Notifier is a Discord bot that displays in-game information from Realm of the Mad God to a Discord text channel.

## Description

The bot script scrapes realmstock.com 's event notifier for information on the current events, remaining heroes, and players in several realms. This information is then displayed to a text channel of the users choice. This bot can be used to have easy, community access to server information to coordinate O3 runs or find events.

#### Technologies

- Selenium

## How To Use

1. Head over to https://discord.com/developers/ and create a new bot with messaging privellages. Add this bot to your server via the OAUTH2 link. *Save the bot's private token.*

2. Clone this repository into a folder of your choice

3. Create a .env file in the root directory and add the following variables.
	
	
	`privateToken={your bot's private token}` \
	`eventChannelId={the Discord channel id of the channel the bot should post in}`
	
	
4. Build and run the Docker image from the Dockerfile in the repository.


	`cd rotmg-notifier`\
	`sudo docker build --tag rotmg-notifier`\
	`sudo docker run rotmg-notifier`
	
	
	
	
*Event notification services like RealmStock's are made possible through bots, which makes them likely a violation of DECA Games' TOS. I do not advocate you using this service and do not accept any responsibility for its use.*
