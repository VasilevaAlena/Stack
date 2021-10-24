CHECK_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALANCED_SEQUENCES = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]

UNBALANCED_SEQUENCES = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):

    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.isEmpty():
            item = self[-1]
            self.__delitem__(-1)
        return item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check_balance(line):
    stack = Stack()
    for item in line:
        if item in CHECK_DICT:
            stack.push(item)
        elif item == CHECK_DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()


if __name__ == '__main__':
    for line in BALANCED_SEQUENCES + UNBALANCED_SEQUENCES:
        if check_balance(line) == True:
            print(f'{line} "Сбалансировано"')
        elif check_balance(line) == False:
            print(f'{line} "Несбалансировано"')

