def duplicate_encode(word):
    new_word = ''
    word = word.lower()
    
    for i in word:
        if word.count(i) > 1:
            new_word+=')'
        else:
            new_word+='('
            
    return new_word
