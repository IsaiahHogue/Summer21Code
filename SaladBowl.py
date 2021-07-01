import nltk
import random
import sys

# Gets user input and returns a list of two texts
def get_texts():
    files = ["File 1:", "File 2:"]
    file_texts = []
    for file in files:
        print("Enter file name or raw text for", file)
        file_text = process_file(sys.stdin.readline())
        file_texts.append(file_text)
    return file_texts

# Reads String file which represnts user input
# Handles either raw text input or file name input
def process_file(file):
    try:
        f = open(file.strip())
        text = ""
        for line in f.readlines():
            text += line
        return_info = nltk.sent_tokenize(text)
        f.close()
        return return_info
    except:
        return nltk.sent_tokenize(file)

# Returns list input sents with tag insirted alonside each element in a tupple
def tag_sents(sents, tag):
    for i in range(0, len(sents)):
        sents[i] = (sents[i], tag)
    
# Ranomdly merges lists text1 and text2, returns mixed list
def merge(text1, text2):
    salad = []
    while(text1 != [] and text2 !=  []):
        if(random.random() > .5):
            salad.append(text1.pop(0))
        else:
            salad.append(text2.pop(0))
    salad.extend(text1)
    salad.extend(text2)
    return (salad)

# Prints salad to String destination with sent tags
def do_output(salad, destintion=""):
    if(destintion == ""):
        print("Enter output destination:")
        destintion = sys.stdin.readline().strip()
    try:
        f = open(destintion)
        for sent in salad:
            print(sent, f)
    except:
        for sent in salad:
            print(sent)           

# Prints salad to String destination without sent tags
def do_output_hidden(salad, destintion=""):
    if(destintion == ""):
        print("Enter output destination:")
        destintion = sys.stdin.readline().strip()
    try:
        f = open(destintion)
        for sent in salad:
            print(sent[0], f)
    except:
        for sent in salad:
            print(sent[0])            

def main():
    texts = get_texts()
    tag_sents(texts[0], "One")
    tag_sents(texts[1], "Two")
    salad = merge(texts[0], texts[1])
    do_output(salad)

if __name__ == "__main__":
  main()