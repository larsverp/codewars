def pig_it(text):
    new_sentence = ''
    punc = ['!', '.', ',', '?']
    words = text.split(' ')
    for word in words:
        if word not in punc:
            new_sentence+= word[1:]+word[0]+'ay '
        else:
            new_sentence = new_sentence+word+' '
    return new_sentence[:-1]
