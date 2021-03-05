n, B = list(map(int, input().strip().split()))
T = 0

# your code here

#Finding the sum to be multiplied by T
totalValues = 0
powerValue = n-1

for i in range(1,n+1):
  if i % 2 ==0:
    baseValue = 2**i + 1
  else:
    baseValue = 3**i +1
  totalValues += baseValue**powerValue
  powerValue -=1

# Finding T
for T in range (1,10001):
  if (totalValues * T > B):
    break

if (T* totalValues <= B):
  T = -1

if (T>10000) or (T<1):
  T = -1
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements

print(T)
