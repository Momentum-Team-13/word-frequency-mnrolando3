from xml.sax import parseString


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]
def make_lowercase(file):
    lowercase_version = []
    for letter in file:
        lowercase = letter.lower()
        lowercase_version.append(lowercase)
        # print(lowercase)
    # print(lowercase_version)
    return lowercase_version

def remove_punctuation(file):
    line_list = []
    for line in file:
        no_period = line.replace('.','')
        no_comma = no_period.replace(',','')
        no_apostrophe = no_comma.replace('\'','')
        no_colon = no_apostrophe.replace(':','')
        no_question_mark = no_colon.replace('?','')
        # print(no_question_mark)
        line_list.append(no_question_mark)
        # print(line_list)
    return line_list

def make_dictionary(file):
    word_count_dict = {}
    word_list = []
    for line in file:
        for word in line.split():
            # print("wordz", word)
            # words = word_count.keys[]
            word_list.append(word)
        # print("list", word_list)
    for word in word_list:
        word_count_dict[word] = word_list.count(word)
    # print("dict", word_count_dict)
    return word_count_dict

def remove_stop_words(file_dictionary):
    new_dictionary = file_dictionary.copy()
    for key in file_dictionary.keys():
        if key in STOP_WORDS:
            del new_dictionary[key]
    # print(new_dictionary)
    return new_dictionary

def print_word_freq(file):
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()
        #read_file is a string
    
    call_lowercase_function = make_lowercase(read_file)
    no_punctuation_version = remove_punctuation(call_lowercase_function)
    # print(no_punctuation_version)
    call_dictionary_function = make_dictionary(no_punctuation_version)
    no_stop_words_version = remove_stop_words(call_dictionary_function)
    
    sorted_dictionary = sorted(no_stop_words_version.items(), key=lambda x:x[1], reverse=True)
    # print("Sorted", sorted_dictionary)
    for item in sorted_dictionary:
        print(f'{item[0]:15} | {item[1]}')

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
