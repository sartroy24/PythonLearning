message = input(">")
words = message.split(" ")
emoji_dict = {
    ":)" : "😀",
    ":(" : "🙃"
}
output = ""
for word in words:
    output += emoji_dict.get(word, word) + " "
print(output)