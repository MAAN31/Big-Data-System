import re
import matplotlib.pyplot as plt

def tokenize(input_text):
    words = re.split(r'[\W_]+', input_text.lower())
    return [word for word in words if word and word not in stopwords]

def eliminate_stopwords(stopwords_file):
    with open(stopwords_file, 'r') as file:
        return set(file.read().split())

def count_words(words):
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def plot_top_ten(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    top_ten = sorted_words[:10]

    words, counts = zip(*top_ten)

    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Top Ten Words')
    plt.show()

if __name__ == "__main__":
    stopwords = eliminate_stopwords('stopwords-MySQL.txt')

    # Read from standard input or a file
    import sys
    input_text = sys.stdin.read()

    words = tokenize(input_text)
    word_count = count_words(words)

    plot_top_ten(word_count)
