class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        #to account for situations where tokens is length 1
        result = int(tokens[0])
        opList = ["+", "-", "*", "/"]
        for val in tokens:
            if val in opList:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                # the reason operand2 is first is because we want
                # the current total value to be multiplied/divided/etc.
                # by most recent number(which is at the top of the stack)
                eval_string = str(operand2) + val + str(operand1)
                result = int(eval(eval_string))
                self.stack.append(result)
            else:
                self.stack.append(val)
        return result