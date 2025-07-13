import os
import string
import json

# root dir has folders for each book, themselves with .txt file readings
root_dir = "AUDIOPATH"

# scan for files
file_paths = []
for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.txt'):
                # Join the root path and file name to get the full file path
                full_file_path = os.path.join(root, file)
                file_paths.append(full_file_path)

# load wordlist into program list
words = []
with open("wordlist30k.txt", 'r') as wordf:
    for word in wordf:
        words.append(word.strip())

def generatephon():
    phondict = {}
    for readingpath in file_paths:
        print(f'!!! now testing {readingpath}')

        # load text file contents
        with open(readingpath, 'r', encoding='utf-8') as sample:
            fcontents = sample.read().split()
        
        # scan for words not in 10k dictionary
        for word in fcontents:
            if word.lower().rstrip(string.punctuation) not in words: # checks against dict
                # it is important that it checks lowered word without punc
                if (word not in phondict) and (not word[0].isnumeric()):
                    phondict[word] = word

    print(len(phondict))
    # dump into file for manual spellings
    with open("dict.txt", 'w') as out:
        json.dump(phondict, out, indent=4)


def replacephon():
    with open("dict.txt", "r") as dictionary:
        finaldict = json.load(dictionary)

    for readingpath in file_paths:
        print(f'!!! now replacing for {readingpath}')
        with open(readingpath, 'r', encoding='utf-8') as reading:
            contents = reading.read().split()
            for ind in range(len(contents)):
                if contents[ind] in finaldict:
                    print(f'replacing "{contents[ind]}" with "{finaldict[contents[ind]]}"')
                    contents[ind] = finaldict[contents[ind]]
            out = ' '.join(contents)
        with open(readingpath, 'w', encoding='utf-8') as writing:
            writing.write(out)

generatephon()
# replacephon()