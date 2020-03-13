def greet():
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    numbers = ['8', '5', '12', '12', '15', '27', '23', '15', '18', '12', '4']
    greeting = ''
    
    for number in numbers:
        for letter in alfabet:
            if alfabet.find(letter) == int(number)-1:
                greeting += letter.lower()
    
    if greeting == 'hello world!':
        return greetings
    else:
        return 'hello world!'
