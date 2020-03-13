def spin_words(sentence):
    list = []
    words = sentence.split(' ')
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        list.append(word)
        
    return ' '.join(list)
