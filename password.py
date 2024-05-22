import random
while True:   
    pass_length = int(input("Enter the Length :"))
    char_set = input("Do You Want Special characters Present in pass ? :")
    password = ''
    if char_set == "no":
        while len(password) < pass_length:
            rand_lower = random.randint(65,91)
            rand_capital = random.randint(97,123)
            rand_number = random.randint(48,58)
            password = password + chr(rand_lower)+chr(rand_capital)+chr(rand_number)
        random.shuffle(list(password))   
        print(password)
        

    else:
        while len(password) < pass_length:
            char = random.randint(33,127) 
            password = password+chr(char)
        random.shuffle(list(password))
        print(password)


