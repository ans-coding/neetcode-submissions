class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        temp0 = 1
        temp1 = 1
        for token in tokens:
            print(num_stack)
            print(token)
            if token.isdigit():
                num_stack.append(int(token))
                continue
            elif token == "+":
                temp0 = num_stack.pop()
                temp1 = num_stack.pop()
                num_stack.append(temp1+temp0)
            elif token == "-":
                temp0 = num_stack.pop()
                temp1 = num_stack.pop()
                num_stack.append(temp1-temp0)
            elif len(token)>1 and token[0] == "-":
                num_stack.append(int(token))
                continue
            elif token == "*":
                temp0 = num_stack.pop()
                temp1 = num_stack.pop()
                num_stack.append(temp1*temp0)
            elif token == "/":
                temp0 = num_stack.pop()
                temp1 = num_stack.pop()
                print(temp1)
                print(temp0)
                num_stack.append(int(temp1/temp0))
        return num_stack[0]