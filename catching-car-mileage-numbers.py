def is_interesting(number, awesome_phrases):
    
    if number > 97 and str(number) not in awesome_phrases:
        if intrest(number) or number in awesome_phrases:
            return 2
        elif intrest(number+1) or number+1 in awesome_phrases:
            return 1
        elif intrest(number+2) or number+2 in awesome_phrases:
            return 1
        else:
            return 0
    else:
        return 0


def intrest(num):
    if num > 99:
        n  = str(num)
        inc = True
        dec = True
        if len(n.replace('0','')) <= 1: return True
        if len(n.replace(n[0],'')) == 0: return True
        nn = n if int(n[-1]) != 0 else n[:-1]
        if len(nn) > 2:
            for l in range(len(nn)-1):
                if int(nn[l]) != (int(nn[l+1])-1): inc = False
            if inc: return True
        for s in range(len(n)-1):
            if int(n[s]) != (int(n[s+1])+1): dec = False
        if dec: return True
        if n[::-1] == n: return True
