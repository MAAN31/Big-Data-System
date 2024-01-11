# Big-Data-System
## Project Description: Top Ten Words Counter and Plotter

### Overview:
This Python project is designed to analyze a given input text stream and identify the top ten most frequently occurring words. The program performs tokenization, eliminates common English stopwords, and creates a bar-chart plot showcasing the top ten words along with their occurrences.

### Key Steps:

#### 1. Tokenize:
The program reads from standard input (STDIN) and tokenizes words using a customized tokenizer that splits on “[\W+_]" to ensure proper word extraction. Common English stopwords and one-character words are excluded during the tokenization process. The stopwords are sourced from the provided file "stopwords-MySQL.txt."

#### 2. Sort:
The tokenized words are stored in a Python dictionary, and the dictionary is then sorted by word occurrences in descending order. In case of ties, words are sorted alphabetically in ascending order.

#### 3. Plot:
The final step involves generating a bar-chart plot of the top-ten words using the Matplotlib library. The y-axis represents the count (number of occurrences) of each word. The resulting plot provides a visual representation of the frequency distribution of words in the input stream.

### Packages Used:
- `numpy` (imported as `np`): Used for numerical operations.
- `matplotlib.pyplot` (imported as `plot`): Used for creating the bar-chart plot.

### Usage:
The program is designed to be executed from the command line, accepting input from either a redirected file or standard input. Example usage:

```bash
python3 topten.py < input_file.txt
```

or

```bash
cat input_file.txt | python3 topten.py
```

### Notes:
- The program utilizes a simple sorting algorithm for simplicity, and a more efficient algorithm could be implemented for large datasets in a future version.
- This project serves as a starting point and can be extended for more advanced text analysis and visualization tasks.

### Attribution:
The example input file "dracula-1879-TPG.txt" was sourced from "Dracula" by Bram Stoker on The Project Gutenberg website.

### Acknowledgments:
- The tokenization approach is inspired by modular examples, and further improvements may be considered for a more robust tokenizer.
- The bar-chart plotting example is adapted from pythonspot: "Matplotlib for Bar-Chart."
