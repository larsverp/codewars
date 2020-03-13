def solution(string,markers):
    lines = string.split('\n')
    
    for line in range(len(lines)):
        for marker in markers:
            if lines[line].find(marker) != -1:
                lines[line] = lines[line][:lines[line].find(marker)]
        lines[line] = lines[line].rstrip()
    return ('\n').join(lines)
