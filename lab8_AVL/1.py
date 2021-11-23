import operator
class Node:
    def __init__(self,prob,symbol,left=None,right=None):
        self.prob=prob
        self.symbol=symbol
        self.left=left
        self.right=right
        self.code=''

def bubblemin(lst):
    #len(lst) -1 เพราะกันindex error
    for first in range(len(lst)-1):
        for i in range(len(lst)-first-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst

def sort_string_by_ascii(data):
    #sort ascii
    data = [str(x) for x in data]
    #print(data)
    #data = [int(x) for ord(x) in data]
    newdata=[]
    for i in data:
        #print(ord(i),i)
        newdata.append(ord(i))
    #print(newdata)
    bubblemin(newdata)
    #print(newdata)
    newdata2=[]
    for i in newdata:
        newdata2.append(chr(i))
    return newdata2
#calculate frequency of each symbol in data
def cal_probability(data):
    data=sort_string_by_ascii(data)
    symbols=dict()
    for element in data:
        if symbols.get(element)==None:
            symbols[element]=1
        else:
            symbols[element]+=1
    
    print('sorted :',symbols)
    return symbols
#print code symbol by traversal in tree
codes=dict()
def cal_code(node,val=''):
    newVal = val + str(node.code)
    if node.right:
        #if left is not empty
        cal_code(node.left,newVal)
    if node.left:
        cal_code(node.right,newVal)
    if not node.left and not node.right:
        #if child empty
        codes[node.symbol]=newVal
    return codes

#obtain encoded output
def output_encoded(data,coding):
    encoding_output=[]
    for c in data:
        #print before input
        #print(coding[c],end='')
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string

def Total_gain(data,coding):
    before_compression = len(data)*8
    after_compression = 0
    symbols=coding.keys()
    for symbol in symbols:
        count=data.count(symbol)
        after_compression += count*len(coding[symbol])
    print("space usage before compression (in bits):",before_compression)
    print("space usage after compression (in bits):",after_compression)

def Huffman_Encoding(data):
    #calculate dict of each symbol
    symbol_with_probs=cal_probability(data)
    #get symbol
    symbols = symbol_with_probs.keys()
    #get frequency
    probabilities = symbol_with_probs.values()
    print("symbols: ",symbols)
    print("probabilities: ",probabilities)

    nodes=[]
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol),symbol))
    
    while len(nodes)>1:
        nodes=sorted(nodes,key=lambda x:x.prob)
        for i in nodes:
            
            print(i.prob,end=' ')
        print()
        for i in nodes:
            
            print(i.symbol,end=' ')
        '''if nodes[1].symbol=='*':
            left = nodes[1]
            right = nodes[0]
        else:
            left = nodes[0]
            right = nodes[1]'''
        '''if nodes[1].symbol =='*' and nodes[0].symbol!='*':
            left = nodes[1]
            right = nodes[0]
        else:'''
        
        #print('\n key',nodes[0].symbol,nodes[0].prob,',',nodes[1].symbol,nodes[1].prob,end=' ')
        if nodes[0].prob < nodes[1].prob:
            print(' first loop')
            left = nodes[0]
            right = nodes[1]
        elif nodes[0].prob == nodes[1].prob:
            print(' second loop')
            left = nodes[0]
            right = nodes[1]
        else:
            print(' third loop')
            left = nodes[1]
            right = nodes[0]
        print("left : ",left.symbol,"right : ",right.symbol)
        left.code = 0
        right.code = 1
        newNode = Node(right.prob+left.prob,left.symbol+right.symbol,left,right)
        #newNode = Node(left.prob+right.prob,left.symbol+right.symbol,left,right)
        nodes.remove(left)
        nodes.remove(right)
        
        nodes.append(newNode) 
    Huffman_Encoding=cal_code(nodes[0])
    inv_Huffman_Encoding = dict(reversed(list(Huffman_Encoding.items())))
    print(inv_Huffman_Encoding)
    #Total_gain(data,Huffman_Encoding)
    printBST(nodes[0])
    encoded_output = output_encoded(data,Huffman_Encoding)
    print("Encoded! :",encoded_output)
    return encoded_output,nodes[0]


def printBST(node,level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.symbol)
        printBST(node.left, level + 1)

data=input("Enter Input : ")

encoded_output,nodes=Huffman_Encoding(data)

