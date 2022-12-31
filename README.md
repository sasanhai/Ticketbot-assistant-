# Ticketbot-assistant-
Ticketbot (assistant)
- To create a ticket, the user can use the command !newticket and the bot will create a new channel with the ticket ID and the username of the creator.
- The bot will then send a message asking for a keyword (either "Skrill" or "USDT"). Depending on the keyword, the bot will send a specific message in response.(coming soon)
- The user can view their open tickets by using the command !viewticket and providing the ticket ID. If the ticket is still open, the bot will display the ticket details.

- To close a ticket, the user can use the command !closeticket and provide the ticket ID. The bot will then close the ticket and remove the corresponding channel.

- Additionally, the bot will only respond to commands in a specific channel, to ensure that tickets are managed efficiently.

- In addition to the above functionality, the bot stores all the ticket information in a text file so that the information is not lost when the bot is restarted. This allows the bot to keep track of all the tickets that have been created and their current status.
