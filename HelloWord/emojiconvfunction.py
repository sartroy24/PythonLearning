def emoji_converter(message):
    output = ""
    emoji_dict = {
    ":)" : "😀",
    ":(" : "🙃"
    }
    words = message.split(" ")
    for word in words:
        output += emoji_dict.get(word, word) + " "
    return output



#print(emoji_converter("Good morning Sarthak :) "))