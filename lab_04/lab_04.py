def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token in ['+', '-', '*', '/', '^']

def infix_to_rpn(infix_expression):
    output = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for token in infix_expression:
        if is_number(token):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        elif is_operator(token):
            while operators and is_operator(operators[-1]) and precedence[operators[-1]] >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output

def evaluate_rpn(rpn_expression):
    stack = []
    for token in rpn_expression:
        if is_number(token):
            stack.append(float(token))
        elif is_operator(token):
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Ділення на нуль неможливе")
                stack.append(operand1 / operand2)
            elif token == '^':
                stack.append(operand1 ** operand2)
    return stack[0]

def main():
    try:
        infix_expression = input("Введіть математичний вираз: ").split()
        rpn_expression = infix_to_rpn(infix_expression)
        result = evaluate_rpn(rpn_expression)
        print("Результат обчислення:", result)
    except Exception as e:
        print("Помилка обробки виразу:", e)

if __name__ == "__main__":
    main()