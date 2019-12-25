class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def compare_prec(oper1,oper2):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    if prec[oper1]<prec[oper2]:
        return True
    else:
        return False
def do_math(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=="/":
        if op2==0:
            return None
        else:
            return op1/op2
    elif op=="+":
        return op1+op2
    else:
        return op1-op2

import jieba
def infix_evaluator(infix_expr):
    infix_list=jieba.lcut(infix_expr)

    operators_stack=Stack() #操作符
    operands_stack=Stack()  #操作数
    for token in infix_list:
        if token in(" ".join([str(i) for i in range(100)])):
            operands_stack.push(eval(token))
        elif token == "(":
            operators_stack.push(token)
        elif token == ")":
            while operators_stack.peek()!="(":
                op=operators_stack.pop()
                op2=operands_stack.pop()
                op1=operands_stack.pop()
                result=do_math(op,op1,op2)
                if result is None:
                    return "Divisor can not be zero"
                operands_stack.push(result)
            operators_stack.pop()
        elif token in "+-*/":
            if operators_stack.is_empty():
                operators_stack.push(token)
            else:
                if operators_stack.peek()!="(":
                    if compare_prec(token,operators_stack.peek()):
                        op=operators_stack.pop()
                        op2=operands_stack.pop()
                        op1=operands_stack.pop()
                        result=do_math(op,op1,op2)
                        if result is None:
                            return "Divisor can not be zero"
                        operands_stack.push(result)

                operators_stack.push(token)

        else:
            return "expression is wrong"
    while operands_stack.size()>1:
        op=operators_stack.pop()
        op2=operands_stack.pop()
        op1=operands_stack.pop()
        result=do_math(op,op1,op2)
        operands_stack.push(result)
    return operands_stack.pop()
if __name__ == "__main__":
    in_string = input("please input your expression:")   #输入运算表达式
    print( infix_evaluator(in_string) )



