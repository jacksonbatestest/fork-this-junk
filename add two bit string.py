# Python3 program for above approach 

# adds the two-bit strings and return the result 

# Helper method: given two unequal sized bit strings, 
# converts them to same length by adding leading 0s 
# in the smaller string. Returns the the new length 
def makeEqualLength(str1, str2): 

	len1 = len(str1)	 # Length of string 1 
	len2 = len(str2)	 # length of string 2 
	if len1 < len2: 
		str1 = (len2 - len1) * '0' + str1 
		len1 = len2 
	elif len2 < len1: 
		str2 = (len1 - len2) * '0' + str2 
		len2 = len1 
	return len1, str1, str2 

def addBitStrings( first, second ): 
	result = '' # To store the sum bits 

	# make the lengths same before adding 
	length, first, second = makeEqualLength(first, second) 

	carry = 0 # initialize carry as 0 

	# Add all bits one by one 
	for i in range(length - 1, -1, -1): 
		firstBit = int(first[i]) 
		secondBit = int(second[i]) 

		# boolean expression for sum of 3 bits 
		sum = (firstBit ^ secondBit ^ carry) + 48
		result = chr(sum) + result 

		# boolean expression for 3 bits addition 
		carry = (firstBit & secondBit) | \ 
				(secondBit & carry) | \ 
				(firstBit & carry) 

		# if overflow, then add a leading 1 
	if carry == 1: 
		result = '1' + result 
	return result 

# Driver Code 
if __name__ == '__main__': 
	str1 = '1100011'
	str2 = '10'
	print('Sum is', addBitStrings(str1, str2)) 
	
# This code is contributed by farhan
