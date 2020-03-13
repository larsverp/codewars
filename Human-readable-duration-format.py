def format_duration(seconds):
    if seconds == 0:
        return 'now'
    list = []

    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365
    
    seconds = seconds - (minutes * 60)
    minutes = minutes - (hours * 60)
    hours = hours - (days * 24)
    days = days - (years * 365)
    
    
    if years >= 1:
        list.append(str(years)+' years' if years > 1 else str(years)+' year')
    else:
        year = ''
    if days >= 1:
        list.append(str(days)+' days' if days > 1 else str(days)+' day')
    else:
        day = ''
    if hours >= 1:
        list.append(str(hours)+' hours' if hours > 1 else str(hours)+' hour')
    else:
        hour = ''
    if minutes >= 1:
        list.append(str(minutes)+' minutes' if minutes > 1 else str(minutes)+' minute')
    else:
        minute = ''
    if seconds >= 1:
        list.append(str(seconds)+' seconds' if seconds > 1 else str(seconds)+' second')
    else:
        second = ''    
    
    if len(list) > 1:
        for item in range(1, len(list)):
            list[item] = ', '+list[item]
        list[-1] = ' and '+list[-1][2:]
        
    return ('').join(list)
