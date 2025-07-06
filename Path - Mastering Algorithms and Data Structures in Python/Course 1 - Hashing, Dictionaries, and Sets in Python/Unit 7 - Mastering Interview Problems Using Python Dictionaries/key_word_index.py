def keyword_index(docs):
    # implement this
    words_map = {}
    for i, doc in enumerate(docs):
        for word in doc.split():
            if word in words_map:
                if i in words_map[word]:
                    words_map[word][i] += 1
                else:
                    words_map[word].update({i: 1})
            else:
                words_map[word] = {i: 1}
    return words_map


docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
