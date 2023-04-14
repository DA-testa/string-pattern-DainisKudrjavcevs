# python3

def keyboard():
    type = input().rstrip()
    if type:
        parents = input().strip().split(" ")
        if parents:
            return type, parents

    return None, None

def file(filename):
    try:
        with open(f"./tests/{filename}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None, None
    except:
        print("Error reading file")
        return None, None
    
    type = contents[0].strip()
    if not type:
        print("Invalid input: n not provided")
        return None, None
    
    parents = contents[1].strip().split(" ")
    if not parents:
        print("Invalid input: parents not provided")
        return None, None
    
    return type, parents

def main():
    height = get_occurrences(type, parents)
    input_method = input().strip()

    if input_method == "I":
        type, parents = keyboard()
        if type and parents:
            height = get_occurrences(type, parents)
            print(int(height))

    elif input_method == "F":
        filename = input().strip()
        if str(filename[-1]) != "a":
            type, parents = file(filename)
            if type and parents:
                height = get_occurrences(type, parents)
                print(int(height))


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


