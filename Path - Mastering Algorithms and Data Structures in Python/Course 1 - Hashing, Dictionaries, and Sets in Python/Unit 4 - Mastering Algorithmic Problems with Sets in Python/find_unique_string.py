def find_unique_string(words):
    # implement this
    seen, dups = set(), set()
    for word in words:
        if word in seen:
            dups.add(word)
        seen.add(word)
    for word in words:
        if word not in dups:
            return f"'{word}'"
    return "''"

print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''
