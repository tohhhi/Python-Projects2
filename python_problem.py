


# def rowSumOddNumbers(n, c):

#     numbers = []

#     for i in range(1, n):
#         if i % 2 == 1:
#             numbers.append(i)

    
#     if c:
#         print(numbers)





listoflists = []
a_list = []
for i in range(0,10):
    a_list.append(i)
    if len(a_list)>3:
        a_list.remove(a_list[0])
        listoflists.append((list(a_list), a_list[0]))

        print (listoflists)

    
    
    
    # if c == 1:
    #     print(numbers[0])

    # if c == 2:
    #     print(numbers[1] + numbers[2])

    

    
    

    


# rowSumOddNumbers(100, 1)




# def test():
    
#     numbers = []

#     for i in range(1,100):
#         numbers.append(i)

    
#     print(numbers[0])
    


# test()