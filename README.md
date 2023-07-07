## NLPParser

NLPParser is a command-line application that performs natural language processing (NLP) parsing, specifically for determining the structure of a sentence. Parsing is a crucial task in NLP as it helps computers understand the meaning of a sentence and extract information from it. NLPParser focuses on extracting noun phrases from sentences to gain insights into the main subject or topic of the sentence.

### Technology Stacks

NLPParser is implemented in Python and leverages the following:

- **Python**: The application is developed using Python, a versatile and widely-used programming language.
- **NLTK**: The Natural Language Toolkit (NLTK) library is utilized for tokenization and parsing tasks.
- **Sys**: The `sys` module is used for handling command-line arguments and input.
- **Re**: The `re` module provides regular expression pattern matching, used for pre-processing.

### Functionality

1. **Preprocess**: The application preprocesses the input sentence by converting it to lowercase and removing any words that do not contain at least one alphabetic character.

2. **Parsing**: NLPParser attempts to parse the preprocessed sentence using a context-free grammar. It constructs a parse tree representing the sentence's structure.

3. **Noun Phrase Chunking**: The application identifies noun phrase chunks in the parse tree. A noun phrase chunk is defined as a subtree labeled as "NP" that does not contain any other noun phrases as subtrees.

4. **Display Results**: The application prints the parse tree for the sentence and extracts the identified noun phrase chunks, providing insight into the main subjects or topics of the sentence.

### Usage

To use NLPParser, execute the following command:


- `filename` (optional) is the path to a file containing the input sentence. If not provided, the application prompts the user to enter a sentence.

The application processes the sentence, attempts to parse it, and displays the parse tree along with the identified noun phrase chunks.

NLPParser is a valuable tool for extracting key information and understanding the structure of sentences using NLP techniques.
