phone = input("Enter your Number:")
number_dict = {
    "1" : "One", "2": "Two", "3": "Three", "4": "Four"
}
output = ""
for item in phone:
    output = output+ ' '+ number_dict.get(item, "!")
print(output)