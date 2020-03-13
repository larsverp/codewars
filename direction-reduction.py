def dirReduc(arr):
    dir = ''
    list = []
    directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
    exclude = ['NS', 'SN', 'EW', 'WE']
    not_done = True
    
    for i in arr:
        dir+=(i[0])
    
    while not_done:
        not_done = False
        for j in range(len(dir)):
            if dir[j:j+2] in exclude:
                dir = dir[:j]+dir[j+2:]
                not_done = True
    
    for letter in dir:
        for i in directions: 
            if i.startswith(letter):
                list.append(i)
    
    return list    
