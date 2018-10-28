A =[2,4,6,8]
target = 10
def two_sum(A,target):
    for i in range(len(A)-1):
        for j in range((i+1),len(A)):
            if A[i]+A[j]==target:
                print(A[i],A[j])
    return True   
        
two_sum(A, target)          

