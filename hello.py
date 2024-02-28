def get_name(name):
    while name == '':
        if name == '':
            print("I didn't catch your name.\n")
            name = input('What\'s your name?\n')
    
    print(f'Hello there, {name}!')

if __name__ == "__main__":
    get_name(input('What\'s your name? \n'))