# Given an unsorted integer array nums, find the smallest missing positive integer.
# Leetcode hard problem

def firstMissingPositive(nums):
	smallest = 1
	while True:
		if smallest in nums:
			smallest += 1
		else:
			break 
	return smallest 



def main():
	test_1_input = [1,2,0]
	test_1_expected = 3

	test_2_input = [3,4,-1,1]
	test_2_expected = 2

	test_3_input = [7,8,9,11,12]
	test_3_expected = 1


	test_1_actual = firstMissingPositive(test_1_input)
	test_2_actual = firstMissingPositive(test_2_input)
	test_3_actual = firstMissingPositive(test_3_input)

	assert test_1_expected == test_1_actual and test_2_actual == test_2_expected and test_3_actual == test_3_expected


main()
