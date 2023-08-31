class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            data_pop = self.data.pop(-1)
            return data_pop

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def top(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            data_top = self.data[-1]
            return data_top
        

    def print(self):
        print(self.data)

stack = Stack() 
stack.push(1)
stack.push(2)
stack.print()
stack.pop()
stack.print() 
stack.pop()
stack.print()
stack.pop()
