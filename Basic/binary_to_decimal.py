def binary_to_decimal(b_num, value=0):
	for i in range(len(b_num)):
		digit = b_num.pop()
		if digit == '1':
			value = value + pow(2, i)
	return value

b_num = list(input())
print(binary_to_decimal(b_num))
print(binary_to_decimal(b_num))
print(binary_to_decimal(b_num))
print(binary_to_decimal(b_num))
print(binary_to_decimal(b_num))
print(binary_to_decimal(b_num))
