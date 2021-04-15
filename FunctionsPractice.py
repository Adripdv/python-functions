# def lesser_of_two_evens(a,b):
#   if a % 2 == 0 and b % 2 == 0:
#     # Both numbers are even
#     if a < b:
#       result = a
#     else:
#       result = b 
#   else:
#     #one or both numbers are odd!
#     if a > b:
#       result = a
#     else:
#       result = b

#   return result

# lesser_of_two_evens(2,4)

#===

# def lesser_of_two_evens(a,b):
#   if a % 2 == 0 and b % 2 == 0:
#     # Both numbers are even
#     print(min(a,b))
#   else:
#     #one or both numbers are odd!
#     print(max(a,b))

# # lesser_of_two_evens(2,4)
# lesser_of_two_evens(7,4)

#==================================================
# def animal_crackers(text):
#   wordlist = text.split()
#   # wordlist = text.lower().split()
#   print(wordlist[0][0] == wordlist[1][0])
# #   print(wordlist)

# animal_crackers('Levelheadded Llama')
# # animal_crackers('Crazy Kangaroo')
# animal_crackers('Crazy cat')

#==================================================
# def makes_twenty(n1,n2):
#     if n1 + n2 == 20:
#         print(True)
#     elif n1 == 20:
#         print(True)
#     elif n2 == 20:
#         print(True)
#     else:
#         print(False)

#==

# def makes_twenty(n1,n2):
#     print((n1 + n2) == 20 or n1 == 20 or n2 == 20)
#     #     print(True)
#     # else:
#     #     print(False)

# makes_twenty(20,30)
# makes_twenty(12,18)
# makes_twenty(2,3)

#==================================================
# def old_macdonald(name):
    
#     #Solution 1
#     # first_letter = name[0]
#     # inbetween = name[1:3]
#     # fourth_letter = name[3]
#     # rest = name[4:]
#     # print(first_letter.upper() + inbetween +  fourth_letter.upper() + rest)
    
##=== Solution 2 (capitalize method to upper case first letter or carachter)
    
#     first_half = name[:3]
#     second_half = name[3:]
#     print(first_half.capitalize() + second_half.capitalize())
    
# old_macdonald('macdonald')

#==================================================

# def master_yoda(text):
#     wordlist = text.split()
#     reverse_word_list = wordlist[::-1]
#     print(' '.join(reverse_word_list))

# master_yoda('I am home')
# master_yoda('We are ready')

#==================================================
# def almost_there(n):
#     # absolute value 
#     print(abs(100-n) <= 10) or (abs(200-n) <= 10)

# almost_there(90)
# almost_there(104)
# almost_there(150)
# almost_there(209)

