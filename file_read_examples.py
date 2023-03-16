

# the simplest way to work with a file!
fp = open("text.txt")
print(fp.read())
# read gets all of the text and we want line by line when its a big text
fp.close()

fp = open("text.txt")

# files are iterable!!
for line in fp:
    # print(line, end="")
    # print(line[:-1])
    print(line.rstrip())

# to print the content as it is without spaces between lines
import requests

r = requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt")
# print(r.text)
# print(r.content)

fp = open("dracula.txt", "w")
fp.write(r.text)
