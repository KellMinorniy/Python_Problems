import re

def find_longest_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    cleaned_content = re.sub(r'[^\w\s]', '', content)
    
    words = cleaned_content.split()
    
    max_length = max(len(word) for word in words)
    
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

if __name__ == "__main__":
    filename = 'example.txt'
    longest_words = find_longest_words(filename)
    
    for word in longest_words:
        print(word)