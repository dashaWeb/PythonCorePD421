
while True:
    user = int(input('''
            [1] - Трикутник зафарбованний з правої сторони зверху
            [2] - Трикутник зафарбованний з лівої сторони знизу
            [3] - Трикутник зафарбованний зверху по центру
            [4] -  Трикутник зафарбованний знизу по центру
            [5] - Трикутникі зафарбовані і зверху і зниз
            [6] - два трикутника з ліва і з права
            [7] - Трикутник з лівої сторни
            [8] - Трикутник з правої сторни
            [9] - Трикутник з лівої сторони зверху
            [10] - Трикутник з правої сторони знизу
                Зробіть свій вибір ---> '''))
    line = 6

    if user == 1:
        i = 0
        while i < line:
            print('   ' * i + ' * ' * (line-i))
            i+=1

    elif  user ==2:
        i =1 
        while i < line:
            j =1
            while j < line:
                if i >=j:
                    print(' * ', end='')
                else:
                    print('   ', end ='')
                j +=1
            print()
            i+=1

           
    elif user ==3:
        i=0
        j = line //2
        while i <=j:
            print('   ' * i+ ' * ' * (2 * (j-i) + 1))
            i +=1

    elif user ==4:
        i =0
        j = line //2
        while i <=j:
            print('   '* (j-i) + ' * ' *(2 * i +1))
            i +=1
    
    elif user == 5:

        i = j
        while i >= 0:
            print('   ' * (line // 2 - i) + ' * ' * (2 * i + 1))
            i -= 1
        i = 1
        while i <= j:
            print('   ' * (line // 2 - i) + ' * ' * (2 * i + 1))
            i += 1
        

    elif user == 6:
        
        # i=1
        # j=8
        # line = 5
        # while line > 0:
        #     line-=1
        #     print('*'*i+' '*j+'*'*i)
        #     i+=1
        #     j -=2
        # i =4
        # j =2
        # while line < 4:
        #     line+=1
        #     print('*'*i+' '*j+'*'*i)
        #     i-=1
        #     j+=2

        line = 9
        i=1
        j=8
        middle = line //2
        while line >0:
            line-=1
            if line > middle:
                print('*'*i+' '*j+'*'*i)
                i+=1
                j-=2
            else:
                print('*'*i+' '*j+'*'*i)
                i-=1
                j+=2

            if line == middle:
                i = middle
                j =2
        
    elif user == 7:
        i =1
        j =8
        line =9
        middle = line //2
        while line >0:
            line-=1
            if line > middle :
                print(' * '*i)
                i+=1
                j-=2
            else:
                print(' * ' * i)
                i-=1
                j+=2



    elif user == 8:
        i =1
        j =8
        line =9
        
        middle = line //2
        while line >0:
            line-=1
            if line > middle :
                print('   '* (j//2)+ ' * '*i)
                i+=1
                j-=2
            else:
                print('   ' * (j//2) +' * ' *i)
                i-=1
                j+=2
            if line == middle:
                i = middle
                j=2

    elif user == 9:
        line =9
        i =0
        while i < line:
            j =0
            while j<line:
                if j<line -i:
                    print(' * ', end ='')
                else:
                    print('   ', end='')
                j+=1
            print()
            i+=1

    elif user == 10:
        line =9
        i =1
        while i < line:
            j =1
            while j < line:
                if i + j >=line:
                    print(' * ', end ='')
                else:
                    print('   ', end ='')
                j+=1
            print()
            i+=1


    user_1 = int(input('''
        Ти хочеш ще виводити фігури?          
            
        [1] - Так 
        [2] - Ні
            
        Зробіть свій вибір ---> '''))
    if user ==2:
        print('Дякую за використання програми!! ')
        break