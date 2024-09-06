def check_parentheses(expression):
    arr = []
    for i in expression:
        if i in "([{":
            arr.append(i)
        elif i in ")]}":
            if not arr:
                print("Unbalanced")
                break
            if (i == ')' and arr[-1] == '(') or (i == ']' and arr[-1] == '[') or (i == '}' and arr[-1] == '{'):
                arr.pop()
            else:
                print("Unbalanced")
                break
    else:
        if not arr:
            print("Balanced")
        else:
            print("Unbalanced")


expression = input("Enter your Expression: ")
check_parentheses(expression)