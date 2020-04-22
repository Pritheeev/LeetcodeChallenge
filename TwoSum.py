
#question name: Two Sum

nums = list(input().split(','))
nums[0] = nums[0].replace('[','')
nums[len(nums)-1] = nums[len(nums)-1].replace(']','')
for i in range(len(nums)):
    nums[i] = int(nums[i])
target = int(input())
for i in range (len(nums)):
    for j in range (len(nums)):
        if(nums[i]+nums[j]==target):
            print ([i,j])
