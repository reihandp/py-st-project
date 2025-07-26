
data = input('Input name: ')

format_save = int(input('Input format: '))
match format_save:
    case 1: 
        format_save = '.jpg'
    case 2:
        format_save = '.png'


print(data + format_save)