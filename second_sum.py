LIMIT = 10000000

# Using dictionary to keep a cache of the already solved numbers
cache = {1: 1}
def collatz_count(num):
    if num not in cache:
        if num % 2 == 0:
            cache[num] = 1 + collatz_count(num / 2)
        else:
            cache[num] = 1 + collatz_count(3 * num + 1)
    return cache[num]

# keeping the top two results returns the number of second	
def get_longest(num):
	top_two = [[1,1], [1,1]]
	for x in range(2,num):
		result = collatz_count(x)
		if result > top_two[0][1]:
			top_two[1][0] = top_two[0][0] 
			top_two[1][1] = top_two[0][1]
			top_two[0][0] = x 
			top_two[0][1] = result
		elif result > top_two[1][1]:
			top_two[1][0] = x
			top_two[1][1] = result
	return top_two[1][0]

# sum up the sequence of the given number	
def get_sum(num):
	sum = 0
	while num != 1:
		sum += num 
		if num % 2 == 0:
			num = num / 2
		else: 
			num = num * 3 + 1
	return sum + 1
	
second = get_longest(LIMIT)
print(get_sum(second))
