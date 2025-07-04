def evaluate_postfix_inverse(expression):
    # implement this
    stack = []
    for element in expression.split(' '):
        if element.isdigit():
            stack.append(int(element))

        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if element == '+': stack.append(operand2 + operand1)
            elif element == '-': stack.append(operand2 - operand1)
            elif element == '*': stack.append(operand2 * operand1)
            elif element == '/': stack.append(operand2 / operand1)

    return stack[0]

print(evaluate_postfix_inverse("2 3 -"))  # Expected output: 1
print(evaluate_postfix_inverse("2 3 +"))  # Expected output: 5
print(evaluate_postfix_inverse("6 3 *"))  # Expected output: 18