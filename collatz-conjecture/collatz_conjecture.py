def steps(number):
    count = 0 
    actual_number = 0
    if number <= 0:
        raise ValueError("A idade não pode ser negativa.")
    while number > 1:
        if number % 2 == 0:
           number = number // 2
           count += 1
           
        else:
            number = (number * 3) + 1
            count += 1
            
    return count
