string = 'abcdefcdghjcd'
sub_string = 'cd'

lstring = list(string)
lsub_string = list(sub_string)
print(len([True for index in range(len(lstring)) if lstring[index:len(lsub_string)+index] == lsub_string]))



# refered solution
# import re
# a = raw_input()
# b = raw_input()
# match = re.findall('(?='+b+')',a)
# print len(match)











# pointer = sub_pointer = counter = temp = 0
# length = len(string)
# sub_length = len(sub_string) 

# while pointer < length-1 :
#     if string[pointer] == sub_string[sub_pointer]:
#         temp = pointer
#         pointer = 0
#         sub_list =[]
#         while sub_pointer < sub_length and temp+pointer<length:
#             if string[temp+pointer] == sub_string[sub_pointer]:
#                 sub_list.append(sub_string[sub_pointer])
#                 pointer += 1
#                 sub_pointer += 1
#             else:
#                 sub_pointer += 1
#             if ''.join(sub_list) == sub_string:
#                 counter += 1
#                 sub_list.clear()
#         pointer = temp +1
#         sub_pointer = 0
#     else:
#         pointer += 1

# print(f"counter : {counter}")

