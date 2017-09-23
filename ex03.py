import sys

if len(sys.argv) < 2:
	print ("Give me a number")
else:
	n = sys.argv[1]
	if n < 0:
		sign = -1
		n = n * -1
	else:
		sign = 1
nums = [0]
i = 0
while i < n:
	print i
	if i % 3 == 0 or i % 5 == 0:
		print i
		nums.append(i)
	i += 1
	if i == n:
		break
print("all done")
print (str(sum(nums) * sign))
