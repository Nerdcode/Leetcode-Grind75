# Valid Anagram

***What is an Anagram?***

A word or a phrase that is made by arranging the letters of another word or phrase in a different order. Example: `Worth` is an anagram of `throw`


# Code Explanation:

- First, we defined a class named Solution.
- Inside the class, there is a method called `isAnagram` that takes two string parameters, `s` and `t`, and returns a boolean value indicating whether s and t
  are anagrams or not.
- The method first creates an empty dictionary called count using `defaultdict(int)`. The defaultdict is a subclass of the built-in dict class that provides a
  default value for a nonexistent key.
- The next step is to count the frequency of each character in string s and store it in the `count` dictionary. This is done using a for loop that iterates over
  each character x in s. The frequency count is incremented by 1 for each occurrence of x in s.
- After counting the characters in s, now we proceeds to decrement the frequency count for each character in string t using another for loop. This is done to
  ensure that both s and t have the same character frequencies. If t contains any additional characters not present in s, the frequency count for those
  characters in count will become negative.
- Finally, we need to check if any character in count has a non-zero frequency. If any character has a non-zero frequency, it means that s and t are not anagrams,
  and it returns False. Otherwise, if all characters have a frequency of zero, the code returns True, indicating that s and t are anagrams.
  
