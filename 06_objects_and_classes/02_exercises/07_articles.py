class Article:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_author: str):
        self.author = new_author

    def rename(self, new_title: str):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


# article = Article(
#     "Highest Recorded Temperature",
#     "Temperatures across Europe are unprecedented, according to scientists.",
#     "Ben Turner"
# )
# article.edit(
#     "Syracuse, a city on the coast of the Italian island of Sicily, registered temperatures of 48.8 degrees Celsius"
# )
# article.rename(
#     "Temperature in Italy"
# )
# article.change_author(
#     "B. T."
# )
# print(article)


'''
TASK:
Create a class Article. The __init__ method should accept 3 arguments: title, content, author. The class should also 
have 4 methods:
edit(new_content) - changes the old content to the new one
change_author(new_author) - changes the old author with the new one
rename(new_title) - changes the old title with the new one
__repr__() - returns the following string "{title} - {content}: {author}"
'''
