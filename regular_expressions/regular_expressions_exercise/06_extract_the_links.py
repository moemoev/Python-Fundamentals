import re

text = input()
pattern = r"(?P<subdomain>w{3}\.)(?P<domainname>[a-zA-Z\d][a-zA-Z\-\d]+[a-zA-Z\d])(?P<domainext>(\.[a-z]+)+)"
valid_links = []

while text:
    match = re.search(pattern, text)
    if match:
        mails = match.groupdict()
        valid_links.append(match['subdomain'] + match['domainname'] + match['domainext'])
    text = input()

for link in valid_links:
    print(link)


'''
TASK:
Write a program which extracts links from a given text. The text will come in the form of strings, each representing a 
sentence. You need to extract only the valid links from it. Example:

"www.internet.com"

                      Sub-Domain			 Domain name		        Domain extension
The Sub-Domain must always be "www". The Domain name can consist of English alphabet letters (uppercase and lowercase), 
digits and dashes ("–"). The Domain extension consists of one or more domain blocks, a domain block consists of a dot 
followed by one or more lowercase English alphabet letters, a Domain extension must have at least one domain block in 
order to be valid. The Sub-Domain and Domain name must be separated by a single dot. Any link that does NOT follow the 
specified above rules should be treated as invalid.
'''