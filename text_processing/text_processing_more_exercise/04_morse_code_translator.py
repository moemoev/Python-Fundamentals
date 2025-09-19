symbol_by_morsecode = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                       '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                       '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                       '-.--': 'Y',
                       '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                       '--...': '7', '---..': '8', '----.': '9', '-----': '0'}

coded_words = [el for el in input().split("|")]

for word in coded_words:
    for letter in word.split():
        print(f"{symbol_by_morsecode[letter]}", end="")
    print(" ", end="")


'''
TASK:
Write a program that translates messages from Morse code to English (capital letters). Use this page to help you 
(without the numbers). The words will be separated by a space (' '). There will be a '|' character which you should 
replace with a space - ' '.
'''