def func(string):
    sub_arr = string.split() 
    # в строке 4 подстроки, из них 3,и 1м =>  len(sub) - up
    upper = 0
    
    for sub in sub_arr:
        
        up_simbol = 0
        low_simbol = 0
        for s in sub: # буквы 
            if s.isupper() == True:
                up_simbol += 1
            if s.islower() == True:
                low_simbol += 1

        if up_simbol > low_simbol: # больше больших
            upper += 1
            
    percent = int(upper / len(sub_arr) * 100) 
    return percent

print(func('NDp Lka nuR vtE'), "%")