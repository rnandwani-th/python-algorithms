# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Leetcode easy problem 

def plusOne(digits):
	if digits == []:
		return []

	all_nines = True
	for i in range(len(digits)):
		if digits[i] != 9:
			all_nines = False 

	length = len(digits)

	if digits[length-1] != 9:
		digits[length-1] += 1
	else:
		carry = 0
		for i in range(len(digits) - 1 , -1, -1):
			if digits[i] != 9:
				digits[i] += 1
				break
			else:
				digits[i] = 0
				

	if all_nines:
		digits.insert(0,1)
			
	return digits


def test():
	test_1_input = [1,2,3]
	test_2_input = [4,3,2,1]
	test_3_input = [0]
	test_4_input = [9,9]
	test_5_input = [1,4,9,6,5,9]
	test_6_input = [1,4,9,6,9,9]

	test_cases_input = [test_1_input, test_2_input, test_3_input, test_4_input, test_5_input, test_6_input]

	test_1_expected = [1,2,4]
	test_2_expected = [4,3,2,2]
	test_3_expected = [1]
	test_4_expected = [1,0,0]
	test_5_expected = [1,4,9,6,6,0]
	test_6_expected = [1,4,9,7,0,0]

	test_cases_expected = [test_1_expected, test_2_expected, test_3_expected, test_4_expected, test_5_expected, test_6_expected]

	test_1_actual = plusOne(test_1_input)
	test_2_actual = plusOne(test_2_input)
	test_3_actual = plusOne(test_3_input)
	test_4_actual = plusOne(test_4_input)
	test_5_actual = plusOne(test_5_input)
	test_6_actual = plusOne(test_6_input)

	test_cases_actual = [test_1_actual, test_2_actual, test_3_actual, test_4_actual, test_5_actual, test_6_actual]

	try:
		for test in range(len(test_cases_expected)):
			assert test_cases_expected[test] == test_cases_actual[test]
	except AssertionError as e:
		print("\nFAIL", e)


test()





