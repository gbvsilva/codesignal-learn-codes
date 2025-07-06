from collections import defaultdict

def find_anagram_words(list_1, list_2):
    # implement this
    mapping1 = defaultdict(list)
    for word in list_1:
        sorted_tuple = tuple(sorted(word))
        mapping1[sorted_tuple].append(word)
    mapping2 = defaultdict(list)
    for word in list_2:
        sorted_tuple = tuple(sorted(word))
        mapping2[sorted_tuple].append(word)
    common_tuples = set(mapping1.keys()) & set(mapping2.keys())
    output = set()
    for anagram_tuple in common_tuples:
        for word1 in mapping1[anagram_tuple]:
            for word2 in mapping2[anagram_tuple]:
                output.add(word1)
    return list(output)


print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []
