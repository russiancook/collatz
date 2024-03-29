cache = {1: 1}
def collatz_count(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + collatz_count(n / 2)
        else:
            cache[n] = 1 + collatz_count(3 * n + 1)
    return cache[n]
	
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
		
def get_sum(num):
	sum = 0
	while num != 1:
		sum += num 
		if num % 2 == 0:
			num = num / 2
		else: 
			num = num * 3 + 1
	return sum + 1
	
second = get_longest(10000000)
print(get_sum(second))
