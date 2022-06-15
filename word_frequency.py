from xml.sax import parseString


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def make_lowercase(read_file):
    lowercase_version = []
    for word in read_file:
        lowercase = word.lower()
        lowercase_version.append(lowercase)
        # print(lowercase)
    # print(lowercase_version)
    return lowercase_version

def remove_punctuation(lowercase_version):
    line_list = []
    for line in lowercase_version:
        no_period = line.replace('.','')
        no_comma = no_period.replace(',','')
        no_apostrophe = no_comma.replace('\'','')
        no_colon = no_apostrophe.replace(':','')
        no_question_mark = no_colon.replace('?','')
        # print(no_question_mark)
        line_list.append(no_question_mark)
        # print(line_list)
    return line_list

def remove_stop_words(line_list):
    for sentence in line_list:
        

def print_word_freq(file):
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()
        #read_file is a string
    
    call_lowercase_function = make_lowercase(read_file)
    remove_punctuation(call_lowercase_function)



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
