def read_input():
    # Get the input type choice
    input_type = input().rstrip()

    # Read the pattern and text depending on the input type
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        filename = "06"
        if str(filename[-1]) != "a":
            try:
                with open(f"./tests/06") as f:
                    contents = f.readlines()
            except FileNotFoundError:
                print("File not found")
                return
            except:
                print("Error reading file")
                return
            pattern = contents[0].strip()
            text = contents[1].strip()
        else:
            print("Invalid filename")

    return pattern, text


def print_occurrences(output):
    # Print the positions of the occurrences in the ascending order
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # Set the prime number and the base
    prime = 101
    base = 256

    # Calculate the hash value of the pattern and the first window of the text
    pattern_hash = 0
    text_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        text_hash = (text_hash * base + ord(text[i])) % prime

    # Slide the window of the text over the pattern and compare the hash values
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+len(pattern)]:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = ((text_hash - ord(text[i]) * (base**(len(pattern)-1))) * base + ord(text[i+len(pattern)])) % prime

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
