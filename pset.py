"""
EXERCISE 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

num_vowels = 0

for i in s:
  if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    num_vowels += 1

print("Number of vowels: " + str(num_vowels))

""""
EXERCISE 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

num_bob = 0

for i in range (len(s)):
  if s[i:i+3] == "bob":
    num_bob += 1

print("Number of times bob occurs is: " + str(num_bob))

"""
EXERCISE 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

maxlength = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
	if s[i+1] >= s[i]:
		current += s[i+1]
		if len(current) > maxlength:
			maxlength = len(current)
			longest = current
	else:
		current = s[i+1]
	i += 1
print("The longest substring in alphabetical order is:" + longest)

