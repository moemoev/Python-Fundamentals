gifts_to_buy = input().split(" ")

command = str(input()).split(" ")
while 'No' not in command and 'Money' not in command:
    # check if {gift} is in list, while there are any, replace them with 'None' by first finding the index
    if 'OutOfStock' in command:
        while command[1] in gifts_to_buy:
            index = gifts_to_buy.index(command[1])
            gifts_to_buy[index] = 'None'
    # check if index is in range, then replace by indexing
    elif 'Required' in command and int(command[2]) in range(len(gifts_to_buy)):
        gifts_to_buy[int(command[2])] = command[1]
    # exchange at the end by eezy pop/append
    elif 'JustInCase' in command:
        gifts_to_buy.pop()
        gifts_to_buy.append(command[1])
    command.clear()
    command = str(input()).split(" ")

for index in range(len(gifts_to_buy)):
    if gifts_to_buy[index] == 'None':
        continue
    print(f"{gifts_to_buy[index]}", end=" ")



'''
TASK:
As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts 
you plan on buying on a single line, separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
"OutOfStock {gift}"
Find the gifts with this name in your collection, if there are any, and change their values to "None".  
"Required {gift} {index}"
Replace the value of the current gift on the given index with this gift if the index is valid. 
"JustInCase {gift}"
Replace the value of your last gift with this one. 
In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the 
following format:
'''