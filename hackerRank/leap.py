def is_leap(year):
    leap = False
    if year % 4 == 0:
        
        if year % 100 == 0: 
            if year % 400 == 0:
                return True
            else:
                return False
        
        return True
    
    return leap

print(is_leap(2100))