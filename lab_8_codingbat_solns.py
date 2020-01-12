def first_last6(nums):
  if nums[0] == 6 or nums[len(nums) - 1] == 6:
    return True
  else:
    return False
  
def common_end(a, b):
  if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
    return True
  else:
    return False
  
def sum3(nums):
  sum = nums[0] + nums[1] + nums[2]
  return sum

def rotate_left3(nums):
  a = nums[0]
  b = nums[1]
  c = nums[2]
  nums = [b, c, a]
  return nums


def reverse3(nums):
  a = nums[0]
  b = nums[1]
  c = nums[2]
  nums = [c, b, a]
  return nums



def max_end3(nums):
  if nums[0]>nums[2]:
    nums[1] = nums[0]
    nums[2] = nums[0]
  else:
    nums[0] = nums[2]
    nums[1] = nums[2]
  return nums



def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    return nums[0]
  else:
    return nums[0] + nums[1]
  
  
  
def middle_way(a, b):
  lst=[a[1], b[1]]
  return lst  



def make_ends(nums):
  a = nums[0]
  b = nums[len(nums) - 1]
  lst = [a, b]
  return lst




def has23(nums):
  if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False




def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
    return True
  else:
    return False





def make_pi():
  pi = [3, 1, 4]
  return pi



def count_evens(nums):
  count = 0
  for i in range(0, len(nums)):
    if nums[i]%2 == 0:
      count = count + 1
  return count



def big_diff(nums):
  max = nums[0]
  min = nums[0]
  for num in nums:
    if num > max:
      max = num
    if num < min:
      min = num
  return max - min 



def has22(nums):
  checker = False
  for i in range(0, len(nums) - 1 ):
    if nums[i] == 2 and nums[i+1] == 2:
      checker = True
      i = len(nums) - 1
  if checker == True:
    return True
  else:
    return False
  
  
  
def centered_average(nums):
  adder = 0
  average = 0
  for i in range(0, len(nums)):
    adder = adder + nums[i]
  adder = adder - max(nums) - min(nums)
  average  = adder // (len(nums) - 2)
  return average
  