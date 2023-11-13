#HI there
# I am still trting to understand python and everything related to python ()
#I need to let you know that some of these codes has been taken from codewars classess




# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
#The maximum sum subarray problem consists in finding the maximum sum of a contiguous 
#subsequence in an array or list of integers:


 # https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python  

 # Complete the function that accepts a string parameter, 
 # and reverses each word in the string. All spaces in the string should be retained.

def max_sequence(arr):
    max_sum = float()
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum 
#time O(n)- linear The code iterates through the array once, performing constant-time operations within the loop. 
#space O(1) - because the algorithm uses a constant amount of extra space that doesn't increase with the size of the input. 




def reverse_words(text):
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    result = " ".join(reversed_words)
    return result
text = "This is an example!"
output_str = reverse_words(text)
print(output_str)
#time -O(n), join creates a new string by concatenating all the reversed words
#space - O(n), The code uses additional space to store the list of words

# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(s):
    s_lower = s.lower()
    for char in s:
        if s_lower.count(char.lower()) == 1:
            return char
    return ""

#time -  O(n^2) where 'n' is the length of the string.
#space- O(n) due to the storage of the lowercase string.

# and I asked for a help chat gpt for the time and space complexity  