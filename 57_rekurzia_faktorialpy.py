import os,time
print("This is the factorial application")
while True:
    try:
        number = int(input("Vlož číslo pre výpočet faktoriálu > "))   
        def factorial_function(number):
            x = 1
            for i in range(1,number+1):
                x = x*i
                if i == number:
                    return x
                else:
                    pass
    except:
        print("Zadal si zlú hodnotu, musíš zadať číslo!!!")            
            
    print(f'Faktorial cisla {number} je {factorial_function(number)}.')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


a = 12
