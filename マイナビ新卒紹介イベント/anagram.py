
MAX = 26

def targetstring(str1, str2):

	l1 = len(str1)
	l2 = len(str2)

	if (l1 != l2):
		return False

	map = [0] * MAX


	for i in range (l1):
		map[ord(str1[i]) - ord('a')] += 1


	for i in range(l2) :
		map[ord(str2[i]) - ord('a')] -= 1

		
		if (map[ord(str2[i]) - ord('a')] < 0):
			return False

	return True

# Driver Code
if __name__ == "__main__":

	str1 = input()
	str2 = input()
	if (targetstring(str1, str2)):
		print("OK")
	else:
		print("NG")

