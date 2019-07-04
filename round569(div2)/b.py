n = int(input())
nums = list(map(int,input().split()))
size = len(nums)
least_neg = nums[0] if nums[0]<0 else -nums[0]-1
least_neg_p = 0
if size%2 !=0:
    for i in range(0,len(nums)):
        if nums[i]>=0:
            neg = -nums[i]-1
        else:
            neg = nums [i]
        if (neg < least_neg and neg!=-1):
            least_neg_p = i
            least_neg = neg
for i in range(0,len(nums)):
    if size%2!=0 and i ==least_neg_p:
        if nums[i]<0:
            print(-nums[i]-1,end=" ")
        else:
            print(nums[i], end=" ")
    else:
        print((-nums[i]-1) if nums[i]>=0 else nums[i], end=" " )