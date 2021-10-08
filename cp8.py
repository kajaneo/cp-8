try:
        x = int(input('введите число: ')) 
except ValueError:
        print('введите корректное значение')
else:
    try:
        a = int(input('введите основание системы счисления (2 или 8): ')) 
    except ValueError:
        print('введите коректное значение')
    else:
        if not((a == 8) or (a == 2)):
           print('пожалуйста, внимательно прочитайте строчку выше и введите корректное значение')
        if a == 2:
            if x == 0:
                print('итог: 0')
            if x > 0:
                b = bin(x)[2:]
                b2 = '0' * (8-len(b)) + b
                print('итог: ' + str(b2))    
            if x < 0:
                b = bin(~(-x))[4:]
                b2 = '1' * (7-len(b)) + '0' + b
                print('итог: ' + str(b2))
        if a == 8:
            if x == 0:
                print('итог:0')
            x2 = x
            x = abs(x)
            nX = ''
            while x > 0:
                nX = str(x % a) + nX
                x //= a
            if x2 < 0:
                print('итог: -' + str(nX))
            elif x2 > 0:    
                print('итог: ' + str(nX))
       
                
            
    
