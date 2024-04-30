class CheckBrackets:
    def __init__(self):
        self.stack = []
        self.indexStack = []

    def check(self, items):
        open_brackets = ["(", "{", "["]
        close_brackets = [")", "}", "]"]
        for i in range(len(items)):
            current = items[i]
            if current in open_brackets:
                self.stack.append(current)
                self.indexStack.append(i)
            elif current in close_brackets:
                if len(self.stack) > 0 and open_brackets[close_brackets.index(current)]==self.stack[len(self.stack)-1]:
                    self.stack.pop()
                    self.indexStack.pop()
                else:
                    return i+1
        if len(self.stack)==0:
            return "Success"
        else:
            return self.indexStack[0]+1


str_to_read = str(open('input.txt', 'r').readline())

print(CheckBrackets().check(str_to_read))


