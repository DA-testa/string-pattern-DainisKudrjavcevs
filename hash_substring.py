def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    prime = 10 ** 9 + 7
    x = 1
    for i in range(p_len):
        x = (x * 263) % prime
    p_hash = 0
    t_hash = 0
    x_pow_p = (x ** (p_len - 1)) % prime
    
    occurrences = []
    for i in range(p_len):
        p_hash = (p_hash * 263 + ord(pattern[i])) % prime
        t_hash = (t_hash * 263 + ord(text[i])) % prime
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * x_pow_p) % prime
            t_hash = (t_hash * 263 + ord(text[i+p_len])) % prime
            t_hash = (t_hash + prime) % prime
    return occurrences

def main():
    input_method = input().strip()

    if input_method == "I":
        pattern = input().strip()
        text = input().strip()
        occurrences = get_occurrences(pattern, text)
        print_occurrences(occurrences)

    elif input_method == "F":
        filename = input().strip()
        if str(filename[-1]) != "a":
            try:
                with open(f"./tests/{filename}") as f:
                    contents = f.readlines()
            except FileNotFoundError:
                print("File not found")
                return
            except:
                print("Error reading file")
                return
            pattern = contents[0].strip()
            text = contents[1].strip()
            occurrences = get_occurrences(pattern, text)
            print_occurrences(occurrences)

if __name__ == '__main__':
    main()