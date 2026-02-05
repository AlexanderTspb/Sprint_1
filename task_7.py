def digit_root(num):
    
    while(num >= 10):
        digits_count = 0
        num_s = num
        while(num_s != 0):
            num_s = num_s // 10
            digits_count += 1
        #print(digits)

        digit = 0
        sum = 0
        for i in reversed(range(0, digits_count)):
            digit = num // pow(10,i)
            sum = sum + digit
            num = num % pow(10,i)
        num = sum
    print(num)

digit_root(4851)
digit_root(97569)
digit_root(889987)
















mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']

colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']

rainbow_dict = {} # создай словарь rainbow_dict

for mn in mnemo:
    for color in colors:
        if mn[0] == color[0]:
            rainbow_dict[mn] = color
