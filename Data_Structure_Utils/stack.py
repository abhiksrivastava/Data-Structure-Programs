class Stack:
    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        return self.items[-1]

    def size_of_stack(self):
        return len(self.items)

    def check_parenthesis_balance(self,expression):
        open_parenthesis = "([{"
        close_parenthesis = ")]}"

        for bracket in expression:
            if bracket in open_parenthesis:
                self.push(bracket)
            elif bracket in close_parenthesis:
                if self.is_empty():
                    balance = False
                    break
                self.pop()

        if self.is_empty():
            balance = True
        else:
            balance = False

        if balance:
            print(f"The inputted expression : {expression}  is balanced")
        else:
            print(f"The inputted expression : {expression} is not balanced")
