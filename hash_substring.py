def read_input():
    input_method = input().strip()

    if input_method == "I":
        pattern = input().strip()
        text = input().strip()
        return pattern, text

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
            return pattern, text
        else:
            print("Invalid filename")
            return


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    prime = 101
    x = 256
    if p_len > t_len:
        return []

    p_hash = sum(ord(pattern[i]) * pow(x, i, prime) for i in range(p_len)) % prime
    t_hash = sum(ord(text[i]) * pow(x, i, prime) for i in range(p_len)) % prime
    x_p = pow(x, p_len - 1, prime)

    for i, char in enumerate(text):
        if i >= p_len:
            t_hash = ((t_hash - ord(text[i - p_len]) * x_p) * x + ord(char)) % prime
        if p_hash == t_hash and pattern == text[i - p_len + 1:i + 1]:
            occurrences.append(i - p_len + 1)

    return occurrences

if __name__ == '__main__':
    read_input()
