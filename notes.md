Read text file using 'open' - DONE
    - create function
        - function opens file
        - function then reads file after it is opened
        - function reads file line-by-line


Calculate frequency of words in file

    - remove punctuation - DONE
        - identify what is punctuation (period, comma, apostrophe, colon, semi-colon, parenthesis, excalamation point, asterisk, ampersand, slash, quotation mark)
        - create function
            - function deletes punctuation characters

    - normalize all words to lowercase - DONE
        - include lowercase attribute (.lower)

    - remove "stop words" -- words used so frequently they are ignored
        - what are "stop words"?
            - articles: the, a
            - conjunctions: and, or
            - to be verbs: is, are
            - prepositions: by, to, of, in, on
        - create function
            - function deletes identified strings

    - go through the file word by word and keep a count of how often each word is used
        - create function
            - function counts each word
            - function creates a dictionary with key as the word and value as the count

Run python3 word_frequency.py praise_song_for_the_day.txt

Get printed report
    - create function
        - function prints report
        - function formats report to include key, pipe, value, asterisk

Report looks like this:
     we | 7 *******
   each | 5 *****
     or | 5 *****
   need | 5 *****
   love | 5 *****
  about | 4 ****
 praise | 4 ****
   song | 4 ****
    day | 3 ***
    our | 3 ***