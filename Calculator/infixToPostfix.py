# Function to return precedence of operators
def prec(c):
    if c == '!' or c == '~':
        return 6
    elif c == '@' or c == '&' or c == '$':
        return 5
    elif c == '%':
        return 4
    elif c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


# Function to perform infix to postfix conversion
def infixToPostfix(s):
    st = []
    result = ""

    for i in range(len(s)):
        c = s[i]

        if (c >= '0' and c <= '9'):
            result += c

        elif c == '(':
            st.append('(')

        elif c == ')':
            while st[-1] != '(':
                result += st.pop()
            st.pop()

        else:
            while st and (prec(c) < prec(st[-1]) or prec(c) == prec(st[-1])): #if operator is smaller or equal in order
                result += st.pop()
            st.append(c)

    while st:
        result += st.pop()

    return result


exp = "2+(4@2-8)"
print(infixToPostfix(exp))