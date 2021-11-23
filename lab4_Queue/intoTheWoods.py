class Stack():

    def __init__(self, *ls):
        self.items = [x for x in ls]

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


inp = input("Enter Input : ").replace(",", " ").split()
comS = Stack()
infoS = Stack()
s = Stack()
visible = Stack()
for x in inp:
    if x in "ABS":
        comS.push(x)
    elif x.isnumeric():
        infoS.push(int(x))
infoS.items.reverse()
for x in comS.items:
    if x == "A":
        s.push(infoS.pop())
    elif x == "B":
        visible.items.clear()
        if s.size() != 0:
            t = s.pop()
            temp = [t]
            visible.push(t)
            for i in range(s.size()):
                num = s.pop()
                temp.append(num)
                if num > visible.peek():
                    visible.push(num)
            temp.reverse()
            s.items = [nu for nu in temp]
            print(visible.size())
        else:
            print(0)
    elif x == "S":
        for i in range(s.size()):
            if s.items[i] % 2 == 1:
                s.items[i] = s.items[i] + 2
            else:
                s.items[i] = s.items[i] - 1
                if s.items[i] < 1:
                    s.items[i] = 1