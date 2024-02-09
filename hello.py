def get_name(name):
    while name == '':
        if name == '':
            print("I didn't catch your name.\n")
            name = input('What\'s your name?\n')
    
    print(f'Hello there, {name}!')
    for letter in name:
        print(letter,'\n')

get_name(input('What\'s your name? \n'))
