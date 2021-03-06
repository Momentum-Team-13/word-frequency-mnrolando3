import string
# from xml.sax import parseString


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]
# list of stop words that need to be removed from file


def make_lowercase(file):
    lowercase_version = []
    for line in file:
        lowercase = line.lower()
        lowercase_version.append(lowercase)
    return lowercase_version
# function that takes file and, for every piece of the file it establishes a variable for each piece's lowercase
# Then, appends that to a list that is returned.


def remove_punctuation(file):
    line_list = []
    for line in file:
        no_punctuation = line.translate(str.maketrans('','',string.punctuation))
        line_list.append(no_punctuation)
    return line_list
# function that takes file and, for every piece of the file, it establishes a variable that translates the piece into a string
# then, makes a translation table where each empty string is mapped onto an empty string and puncuation is replaced with None.
# Then, the function appends the variable to a list that is returned.


def make_dictionary(file):
    word_count_dict = {}
    word_list = []
    for line in file:
        for word in line.split():
            print("wordz", word)
            # words = word_count.keys[]
            word_list.append(word)
        print("list", word_list)
    for word in word_list:
        word_count_dict[word] = word_list.count(word)
    # print("dict", word_count_dict)
    return word_count_dict
# function that takes file and creates an empty dictionary and empty list
# Then, with a nested loop, it interates through each piece of the file
# for each subpiece in the split pieces, it appends that to the list
# Then, for each item in the list, add it to the dictionary with count as value
# The dictionary is returned


def remove_stop_words(file_dictionary):
    new_dictionary = file_dictionary.copy()
    for key in file_dictionary:
        if key in STOP_WORDS:
            del new_dictionary[key]
    # print(new_dictionary)
    return new_dictionary
# function takes dictionary and establishes a copy as a new dictionary
# then, for each piece in the dictionary, if it is in the list of stop words
# delete the piece from the new dictionary
# return the new dictionary.


def print_word_freq(file):
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()
        # read_file is a string of the file selected to open
    print(read_file)

    call_lowercase_function = make_lowercase(read_file)
    # establishes var to call make_lowercase function on read_file

    no_punctuation_version = remove_punctuation(call_lowercase_function)
    # establishes var to call remove_punctuation function on previous var

    call_dictionary_function = make_dictionary(no_punctuation_version)
    # establishes var to call make_dictionary function on previous var

    no_stop_words_version = remove_stop_words(call_dictionary_function)
    # establishes var to call remove_stop_words function on previous var

    alphabetized_dictionary = sorted(no_stop_words_version.items(), key=lambda x:x[0], reverse=False)
    # establishes a var of the sorted the items of the previous var
    # sorts on the first piece of the item in descending order

    sorted_dictionary = sorted(alphabetized_dictionary, key=lambda x: x[1], reverse = True)
    # establishes a variable of the sorted items of the previous variable
    # sorts on the second piece of the item in ascending order

    for item in sorted_dictionary:
        print(f'{item[0]:15} | {item[1]} {"*" * item[1]}')
    # for each piece in the previous variable, print an f-string
    # 1st item with 15 spaces, pipe, 2nd item, asterisk multiplied by 2nd item


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
