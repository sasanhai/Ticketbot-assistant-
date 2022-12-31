import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

tickets = {}



def create_ticket(user):
    # Get the next available ticket ID
    ticket_id = max(tickets.keys()) + 1 if tickets else 1
  
    tickets[ticket_id] = {
        'user': user,
        'status': 'open',
        'channel': None
    }
    return ticket_id


def view_ticket(ticket_id):
    if ticket_id in tickets:
        return tickets[ticket_id]
    else:
        return None


def close_ticket(ticket_id):
    if ticket_id in tickets:
        tickets[ticket_id]['status'] = 'closed'


def save_tickets():
    with open('tickets.txt', 'w') as f:
        for ticket_id, ticket in tickets.items():
            f.write(f'{ticket_id},{ticket["user"].id},{ticket["status"]}\n')


def load_tickets():
    global tickets
    tickets = {}
    with open('tickets.txt', 'r') as f:
        for line in f:
            ticket_id, user_id, status = line.strip().split(',')
            tickets[int(ticket_id)] = {
                'user': client.get_user(int(user_id)),
                'status': status,
                'channel': None
            }


@client.event
async def on_ready():
    # Load the tickets from the file
    load_tickets()


@client.event
async def on_message(message):

    command_channel_id = 1058353682711846962  # Replace this with the ID of your command channel

    if message.channel.id == command_channel_id:
     words = message.content.split()
    if len(words) > 0 and words[0] == '!newticket':
        ticket_id = create_ticket(message.author)
        ticket_channel = await message.guild.create_text_channel(f'ticket-{ticket_id}')
        tickets[ticket_id]['channel'] = ticket_channel
        await ticket_channel.send(f'Your ticket has been created with ID {ticket_id}')
        await message.delete()

        save_tickets()
    elif len(words) > 1 and words[0] == '!viewticket':
        ticket_id = int(words[1])
        ticket = view_ticket(ticket_id)
        if ticket is not None:
            await message.channel.send(f'Ticket {ticket_id}: {ticket["user"]} ({ticket["status"]})')
        else:
            await message.channel.send(f'Ticket {ticket_id} not found')
    elif len(words) > 1 and words[0] == '!closeticket':
        ticket_id = int(words[1])
        close_ticket(ticket_id)
        await message.channel.send(f'Ticket {ticket_id} has been closed')

client.run('TOKEN')
