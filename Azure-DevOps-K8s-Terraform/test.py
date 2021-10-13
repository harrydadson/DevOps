'''
1 free book with every purchase of 5 or more books
2 free books with every purchase of 8 or more books
regular customers 1 free book with purchase of >= 7
                    2 free books with >= 12
'''

isPremiumCustomer = False
free_book = 0
nbooksPurchased = None

if (isPremiumCustomer == True):
    if (nbooksPurchased >= 5 and nbooksPurchased < 8):
        free_book =1 
    elif (nbooksPurchased >= 8):
        free_book = 2 
elif (isPremiumCustomer == False):
    if (nbooksPurchased >= 7 and nbooksPurchased < 12):
        free_book = 1
    elif (nbooksPurchased >= 12):
        free_book = 2


# if nbooksPurchased > 4:
#     if isPremiumCustomer:
#         freeBooks = 1
#         if nbooksPurchased > 7:
#             freeBooks = 2
#         else:
#             freeBooks = 0
#             if nbooksPurchased > 6:
#                 freeBooks = 1
#             if nbooksPurchased > 11:
#                 freeBooks = 2

# else: 
#     freeBooks = 0