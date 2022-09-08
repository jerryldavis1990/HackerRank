inputstr=input("Enter a string ")
subseq=input("Enter a subsequence ")
N=len(inputstr)
n=0
count=0
for i in range(N):
    if subseq in inputstr:
        idx = inputstr.index(subseq)
        count=count+1
        n=idx+len(subseq)-1
        inputstr=inputstr[n:]
print(count)


