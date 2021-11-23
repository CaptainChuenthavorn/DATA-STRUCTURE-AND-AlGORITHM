class Data():
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return f'({self.key}, {self.value})'


class Hash():
    def __init__(self,size,maxColli):
        self.size=size
        self.maxColli=maxColli
        self.table=[]
        for i in range(size):
            self.table.append(None)
        pass
    
    def make_hash(self,key):
        index = 0
        for char in key:
            index+=ord(char)
        return index%self.size

    def isFull(self):
        sum=0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                sum+=1
        return sum==self.size

    def insert(self,data):
        if self.isFull():
            print("This table is full !!!!!!")
            quit()
        key=data.key
        value=data.value
        round=0
        hashIndex = self.make_hash(key)
        while round<self.maxColli:
            index=(hashIndex+(round**2))%self.size
            if self.table[index] is None:
                self.table[index]=data
                return
            round+=1
            print(f'collision number {round} at {index}')
        print("Max of collisionChain")

    def __str__(self):
        s=''
        for i in range(self.size):
            s+=f'#{i+1}	{self.table[i]}\n'
        s+='---------------------------'
        return s

print(" ***** Fun with hashing *****")
setup,lst =input("Enter Input : ").split('/')
size,maxColli = list(map(int,setup.split()))
lst = lst.split(',')
datalst=[]
for i in lst:
    key,value=i.split()
    datalst.append(Data(key,value))
hash=Hash(size,maxColli)
for data in datalst:
    hash.insert(data)
    print(hash)