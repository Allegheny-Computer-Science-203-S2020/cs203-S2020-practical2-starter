"""Compute term frequencies for an input file using a cookbook style."""

# TODO: Add the missing import statements
# TODO: Make sure that you understand the purpose of these import statements

# TODO: Add all of the missing code to this file, ensuring that it
# runs correctly and produces the expected output for both input files

# TODO: Think carefully about how you would write an automated test
# case for each of the functions in this module. Ask these questions:
# --> For a given input, what is the output of this function?
# --> How can I know that the function's output is, in fact, correct?

# The shared mutable data
words = []
word_freqs = []


def read_file(path_to_file):
    """Take a path to a file and assign file contents to the global data."""
    global data
    with open(path_to_file) as data_file:
        data = data + list(data_file.read())


def filter_chars_and_normalize():
    """Replace all non-alphanumeric chars in data with white space."""
    # pylint: disable=global-statement
    global data
    # pylint: disable=consider-using-enumerate
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = " "
        else:
            data[i] = data[i].lower()


def scan():
    """Scan data for words, filling the global variable words."""
    # pylint: disable=global-statement
    global data
    global words
    data_str = "".join(data)
    words = words + data_str.split()


def remove_stop_words():
    """Remove the stop words from the data file as we don't count them."""
    # pylint: disable=global-statement
    global words
    with open("stopwords/stop_words.txt") as stop_file:
        stop_words = stop_file.read().split(",")
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    # pylint: disable=consider-using-enumerate
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)


def frequencies():
    """Create a list of pairs associating words with frequencies."""
    # pylint: disable=global-statement
    global words
    global word_freqs
    # iterate through all of the words
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])


def sort():
    """Sort word_freqs by frequency."""
    # pylint: disable=global-statement
    global word_freqs
    word_freqs.sort(key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    # perform all steps using separate functions
    read_file(sys.argv[1])
    filter_chars_and_normalize()
    scan()
    # TODO: Add the missing function call
    frequencies()
    # TODO: sort the computed frequencies
    # TODO: display the word frequency table
