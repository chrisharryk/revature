# evaluate the expression

def calculator(exp):
    # convert infix to postfix
    stk = []
    postfix = ''
    for x in exp:
        if x.isdigit():
            postfix += x
        elif x in ('*', '/', '-', '+'):
            if not stk or x > stk[-1]:
                stk.append(x)
            else:
                while stk and stk[-1] >= x:
                    postfix += stk[-1]
                    stk.pop()
                stk.append(x)
        elif x == '(':
            stk.append('(')
        elif x == ')':
            while stk and stk[-1] != '(':
                postfix += stk[-1]
                stk.pop()
            stk.pop()
    for x in stk: postfix += x
    
    # evaluating the postfix expression
    stk = []
    ops = '*', '/', '-', '+'
    for x in postfix:
        if x.isdigit():
            stk.append(float(x))
        elif x in ops:
            X, Y = float(stk[-2]), float(stk[-1])
            stk = stk[:-2]
            if x == '+': stk.append(X+Y)
            if x == '-': stk.append(X-Y)
            if x == '/': stk.append(X/Y)
            if x == '*': stk.append(X*Y)

    return stk[0]