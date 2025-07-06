def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"

    # implement this
    results = []
    strength = {
        'length': False,
        'digit': False,
        'lowercase': False,
        'uppercase': False,
        'special_char': False
    }
    for password in passwords:
        result = strength.copy()
        if len(password) >= 8:
            result['length'] = True
        if any(char.isdigit() for char in password):
            result['digit'] = True
        if any(char.islower() for char in password):
            result['lowercase'] = True
        if any(char.isupper() for char in password):
            result['uppercase'] = True
        if any(char in special_characters for char in password):
            result['special_char'] = True
        results.append(result)
    return results

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
