def solution(s):
    return ''.join(' ' + char if char.isupper() else char.strip() for char in s).strip()
