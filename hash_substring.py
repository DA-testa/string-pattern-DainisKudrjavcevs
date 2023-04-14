# python3

def read_input():
    type = input().rstrip()
    if type == "I":
        return (input().rstrip(), input().rstrip)
    else:
        with open ('tests.txt', 'r') as f:
            return (f.readline().rstrip(), f.readline().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_garums = len(pattern)
    t_garums = len(text)
    kopa = 10 ** 9 + 7
    x=1
    for i in range(p_garums):
        x = (x * 263) % kopa
    p_hash = 0
    t_hash = 0
    
    occurrences  = []
    for i in range(p_garums):
        p_hash = (p_hash * 263 + ord(pattern[i])) % kopa
        t_hash = (t_hash * 263 + ord(text[i])) % kopa
    for i in range(t_garums - p_garums + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_garums]:
                occurrences.append(i)
        if i < t_garums - p_garums:
            t_hash = (t_hash - ord(text[i]) * x) % kopa
            t_hash = (t_hash * 263 + ord(text[i+p_garums])) % kopa
            t_hash = (t_hash + kopa) % kopa
    return occurrences 

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

