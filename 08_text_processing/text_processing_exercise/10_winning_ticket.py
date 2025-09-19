tickets = [el.strip() for el in input().split(", ")]
winning_symbols = ['@', '#', '$', '^']
ticket_name = []
ticket_symbol = []
ticket_symcount = []


def is_ticket_valid(symbols: str):
    if not len(symbols) == 20:
        return False
    return True


# check if at least 6 times same symbol is in both halfs, not checked for consecutive yet
def dominating_symbol_exists(l_list: list, r_list: list):
    for symbol in winning_symbols:
        if 6 <= min(l_list.count(symbol), r_list.count(symbol)):
            # insert dominating symbol in dict and count of dom symbol in other dict
            ticket_symbol.append(symbol)
            ticket_symcount.append(min(l_list.count(symbol), r_list.count(symbol)))
            return True
    return False


# verrify if the dominating symbol is consecutive in both halfs of the ticket
def dominating_symbol_consecutive(l_list: list, r_list: list):
    dom_symbol = ticket_symbol[len(ticket_symbol) - 1]
    count_dom_symbol = ticket_symcount[len(ticket_symcount) - 1]
    for count in range(count_dom_symbol, 5, -1):
        if dom_symbol * count in "".join(l_list) and dom_symbol * count in "".join(r_list):
            ticket_symcount[len(ticket_symcount) - 1] = count
            return True
    return False


for ticket in tickets:
    ticket_name.append(ticket)
    if not is_ticket_valid(ticket):
        ticket_symbol.append('invalid ticket')
        ticket_symcount.append(0)
        continue
    ticket_chars = [el for el in ticket]
    l_half, r_half = ticket_chars[:10:], ticket_chars[10::]
    if not dominating_symbol_exists(l_half, r_half):
        ticket_symbol.append('no match')
        ticket_symcount.append(0)
        continue
    if not dominating_symbol_consecutive(l_half, r_half):
        ticket_symbol[len(ticket_symbol) - 1] = 'no match'
        ticket_symcount[len(ticket_symcount) - 1] = 0
        continue

for i in range(len(ticket_name)):
    if 6 <= ticket_symcount[i] < 10:
        print(f'ticket "{ticket_name[i]}" - {ticket_symcount[i]}{ticket_symbol[i]}')
    elif ticket_symcount[i] == 10:
        print(f'ticket "{ticket_name[i]}" - {ticket_symcount[i]}{ticket_symbol[i]} Jackpot!')
    elif ticket_symbol[i] == 'no match':
        print(f'ticket "{ticket_name[i]}" - {ticket_symbol[i]}')
    elif ticket_symbol[i] == 'invalid ticket':
        print(f"invalid ticket")


'''
TASK:
Lottery is exciting. What is not, is checking a million tickets for winnings only by hand. So, you are given the task to 
create a program which automatically checks if a ticket is a winner. 
You are given a collection of tickets separated by commas and spaces. You need to check every one of them if it has a 
winning combination of symbols.
A valid ticket should have exactly 20 characters. The winning symbols are '@', '#', '$' and '^'. But in order for a 
ticket to be a winner the symbol should uninterruptedly repeat for at least 6 times in both the tickets left half and 
the tickets right half. 
For example, a valid winning ticket should be something like this: 
"Cash$$$$$$Ca$$$$$$sh" 
The left half "Cash$$$$$$" contains "$$$$$$", which is also contained in the tickets right half "Ca$$$$$$sh". A winning 
ticket should contain symbols repeating up to 10 times in both halves, which is considered a Jackpot 
(for example: "$$$$$$$$$$$$$$$$$$$$").
'''