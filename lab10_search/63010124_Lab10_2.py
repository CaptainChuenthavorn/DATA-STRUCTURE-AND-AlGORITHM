def FirstGreatValue(arr,k):
    for i,x in enumerate(arr):
        if x>k:
            return x
    return 'No First Greater Value'
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in k:
    print(FirstGreatValue(sorted(arr),i))
