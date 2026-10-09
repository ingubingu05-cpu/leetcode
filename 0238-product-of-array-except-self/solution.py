class Solution(object):
    def productExceptSelf(self, nums):
        n= len(nums)
        lmul=1 #left multiplier for the left array multiplication
        rmul=1 # multiplier for right side multiplixation

        l=[0]*n
        r=[0]* n #arrays of size with 0s

        for i in range(n):  #i does positive index l->r
            j = -i - 1   # j does negative index, r->l
            
            l[i]=lmul 
            r[j]=rmul

            lmul *= nums[i]   #updating multipliers like i*=2 bla bla
            rmul *= nums[j]
        answer=[]
        for i in range(n):
            answer.append(l[i]*r[i])
        return answer