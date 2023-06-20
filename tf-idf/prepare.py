
# read the index.txt and prepare documents, vocab , idf
import chardet
import re
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc
data=[[]]
for i in range(1,2850):
    filename = 'Leetcode Question Scrapper/Qdata/'+str(i)+'/'+str(i)+'.txt'
    my_encoding = find_encoding(filename)
    with open(filename, 'r', encoding=my_encoding) as f:
        k = f.readlines()
        doc=[]
        for line in k:
            if "Example 1:" in line:
                break
            elif "Example" in line:
                break
            else:
                doc.append(line)
        data.append(doc)
def preprocess(document_text):
    # extract all the words from a document
    words=[]
    for index,lines in enumerate(document_text):
        lines.lower()
        word = re.findall(r'\b[A-Za-z]+\b',lines)
        words.extend(word)
    return words
vocab = {}
documents = []
for index, doc in enumerate(data):
    # read statement and add it to the line and then preprocess
    tokens = preprocess(doc)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# reverse sort the vocab by the values
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

# save the vocab in a text file
with open('tf-idf/vocab.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save the idf values in a text file
with open('tf-idf/idf-values.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

# save the documents in a text file
with open('tf-idf/documents.txt', 'w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))


inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open('tf-idf/inverted-index.txt', 'w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))