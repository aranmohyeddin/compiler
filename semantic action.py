name = 'if'
inp = 'dummy'

class Stack:
    def __init__(self):
        self.list = []

    def push(self, a):
        self.list.append(a)

    def pop(self, i):
        self.list = self.list[:-i]

    def top(self):
        return len(self.list) - 1


stack = Stack()

PB = []
i = 0

class Operator():
    def __init__(self, name, arg1, arg2, arg3):
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3


def findaddr(inp):
    pass


def gettemp():
    pass


if name == 'pid':
     p = findaddr(inp)
     stack.push(p)

if name == 'add':
    t = gettemp()
    PB[i] = Operator("add", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('',t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'sub':
    t = gettemp()
    PB[i] = Operator("sub", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'mult':
    t = gettemp()
    PB[i] = Operator("mult", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'equal':
    t = gettemp()
    PB[i] = Operator("eq", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'less':
    t = gettemp()
    PB[i] = Operator("lt", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'not':
    t = gettemp()
    PB[i] = Operator("lt", ('', stack.list[stack.top()]), ('', t), None)
    i = i + 1
    stack.pop(1)
    stack.push(t)

if name == 'assign':
    PB[i] = Operator("assign", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), None)
    i = i + 1
    stack.pop(2)

if name == 'save':
    stack.push(i)
    i = i +1

if name == 'while':
    PB[stack.list[stack.top()]] = Operator("jpf", ('', stack.list[stack.top() - 1]), ('#', i + 1), None)
    PB[i] = Operator("jp", ('', stack.list[stack.top() - 2]), None, None)
    i = i + 1
    stack.pop(3)


if name == 'jpf_save':
    PB[stack.list[stack.top()]] = Operator('jpf', ('', stack.list[stack.top() - 1]), ('#', i + 1), None)
    stack.pop(2)
    stack.push(i)
    i = i + 1

if name == 'jp':
    PB[stack.list[stack.top()]] = Operator('jp', ('#', i), None, None)
    stack.pop(1)
    i = i + 1

if name == 'jp2':
    PB[stack.list[stack.top() - 1]] = Operator('jp', ('#', i), None, None)
    s = stack.list[-1]
    stack.pop(2)
    stack.push(s)
    i = i + 1

if name == 'jpf':
    PB[stack.list[stack.top()]] = Operator('jpf', ('', stack.list[stack.top() - 1]), ('#', i), None)
    stack.pop(2)

