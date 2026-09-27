class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stackNum = []
        opList = ["+", "-", "*", "/"]  
        result = int(tokens[0])
        for val in tokens:
            if val in opList:
                operand1 = self.stackNum.pop()
                operand2 = self.stackNum.pop()
                eval_string = str(operand2) + val + str(operand1)
                print(eval_string)
                result = int(eval(eval_string))
                self.stackNum.append(result)
            else: 
                self.stackNum.append(val)
        return result