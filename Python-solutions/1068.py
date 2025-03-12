# Balanço de Parênteses I

# Copilot's solution
def check_expression(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'incorrect'
            stack.pop()
    if stack:
        return 'incorrect'
    return 'correct'
  
while True:
  try:
    expression = input()
    print(check_expression(expression))
  except EOFError:
    break



# My solution

# def check_expression(exp):
#   stack = []
  
#   for s in exp:
#     if s == '(': 
#       stack.append(s)
#     elif s == ')':
#       stack.pop()
      
#   return "correct" if len(stack) == 0 else "incorrect"

# expression = input()
# print(check_expression(expression))


# My solution is't the best because it doesn't consider edge cases,
# like if the stack is empty and the closing parenthesis is found.
