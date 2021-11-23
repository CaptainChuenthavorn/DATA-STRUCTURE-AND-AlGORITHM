class Hash():
    def __init__(self,table_size,maxColli,threshold):
        self.size=table_size
        self.maxColli=maxColli
        self.table=[]
        for i in range(size):
            self.table.append(None)
        self.member=[]
        self.threshold = threshold
        
    def next_prime(self,n):
        return self.find_prime(n,2*n)
    
    def find_prime(self,min,max):
        for c in range(min,max):
            for i in range(2,c):
                if c%i==0:
                    break
            else:
                #print('we get prime',c)
                return c
        return None

    def is_empty(self,idx):
        return self.table[idx]==None
    def rehash(self):
        self.size = self.next_prime(self.size*2)
        self.table=[None]*self.size
        for x in self.member:
            retry=0
            first_idx= x %self.size
            while retry<self.maxColli:
                idx=(first_idx+retry**2)%self.size
                if self.is_empty(idx):
                    self.table[idx]=x
                    break
                retry+=1
                print(f'collision number {retry} at {idx}')
            
    def insert(self,value):
        print("Add :",value)
        self.member.append(value) 
        retry=0
        first_idx= value%self.size
        while retry<self.maxColli:
            idx=(first_idx+retry**2)%self.size
            if self.is_empty(idx):
                if(len(self.member))*100/self.size>self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehash()
                    return
                else:
                    self.table[idx]=value
                    return
            retry+=1
            print(f'collision number {retry} at {idx}')
        print("****** Max collision - Rehash !!! ******")
        self.rehash()
    
    def _print(self):
        for i in range(self.size):
            print("#"+str(i+1)+"	"+str(self.table[i]))
        print("----------------------------------------")

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

    def __str__(self):
        s=''
        for i in range(self.size):
            s+=f'#{i+1}	{self.table[i]}\n'
        s+='---------------------------'
        return s

print(" ***** Rehashing *****")
inp =input("Enter Input : ").split('/')
size,maxColli,threshold = int(inp[0].split()[0]),int(inp[0].split()[1]),int(inp[0].split()[2]),
member = list(map(int,inp[1].split()))

h=Hash(size,maxColli,threshold)
print("Initial Table :")
h._print()
for i in member:
    h.insert(i)
    h._print()