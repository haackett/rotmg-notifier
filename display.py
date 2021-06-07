
def display_events(events):
    messages = '```'
    for server in events:
        messages += (str(server) + '\n')
    messages += '```'
    return messages