
##################################################
# postfix_eval_typed
##################################################
def postfix_eval_typed(chaine, type):
    """
    a postfix evaluator, using a parametric type
    that can be either `int`, `float` or `Fraction` or similars
    """
    def divide(a, b):
        if issubclass(type, int):
            return a // b
        else:
            return a / b
    stack = []
    tokens = chaine.split()
    for token in tokens:
        operand = None
        try:
            operand = type(token)
            stack.append(operand)
        except ValueError:
            operator = token
            if len(stack) < 2:
                # error: not enough values to operate on
                return 'error-empty-stack'
            right = stack.pop()
            left = stack.pop()
            if operator == '+':
                stack.append(left + right)
            elif operator == '-':
                stack.append(left - right)
            elif operator == '*':
                stack.append(left * right)
            elif operator == '/':
                stack.append(divide(left, right))
            else:
                # error: unknown op
                return 'error-syntax'
    # we must have exactly one item in the stack
    if len(stack) == 0:
        return 'error-empty-stack'
    elif len(stack) > 1:
        return 'error-unfinished'

    return stack.pop()

