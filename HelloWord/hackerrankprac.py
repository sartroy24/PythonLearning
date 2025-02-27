import textwrap
string = input("Enter String:")
max_width = int(input("Enter width:"))
# output = ''
# for i in range(0, len(string), 4):
#     output = output + '\n' + string[i : i+4]
#     # print(string[i : i+4])
#
# print(output)
s_wrap_list = textwrap.wrap(string, 4)
print('\n'.join(s_wrap_list))