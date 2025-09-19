title = input()
article = input()
div = []
cmd = input()


while not cmd == 'end of comments':
    div.append(cmd)
    cmd = input()
print(f"<h1>")
print(f"\t{title}")
print(f"</h1>")
print("<article>")
print(f"\t{article}")
print("</article>")
for el in div:
    print("<div>")
    print(f"\t{el}")
    print("</div>")


'''
TASK:
You will receive 3 lines of input. On the first line you will receive a title of an article. On the next line you will 
receive the content of that article. On the next n lines until you receive "end of comments" you will get the comments 
about the article. Print the whole information in html format. The title should be in "h1" tag (<h1></h1>); the content 
in article tag (<article></article>); each comment should be in div tag (<div></div>). For more clarification see the 
example below
'''