# Projects: Cats

Computer Aided Typing Software

In this project, you will write a program that measures typing speed.
Additionally, you will implement typing autocorrect, which is a feature that attempts to correct the spelling of a word after a user types it.

# Phase 1：Typing
## Problem1: Pick

pick()函数返回的是 满足select函数的序列 的 第k项元素。

Implement pick. This function selects which paragraph the user will type for the typing test. It takes three parameters:

    paragraphs: a list of potential paragraphs (strings)
    select: a function that evaluates a paragraph and returns True if it meets certain criteria, and False otherwise
    k: a non-negative integer representing the index of the desired paragraph among those that meet the criteria

The pick function returns the kth paragraph from paragraphs for which the select function returns True. If no such paragraph exists (because k is greater than or equal to the number of qualifying paragraphs), then pick returns an empty string.

Hint: Don't worry about the specific implementation of the select function. Just assume it takes a paragraph as input and returns True orFalse. Reminder: Indexing starts at 0. If k is 0, we want to pick the first qualifying paragraph.

```python
# 输入 python3 ok -q 01 -u
>>> from cats import pick
>>> ps = ['short', 'really long', 'tiny']
>>> s = lambda p: len(p) <= 5
>>> pick(ps, s, 0) # remember to put quotes ('') around strings!
'short'
>>> pick(ps, s, 1)
'tiny'
>>> pick(ps, s, 2)
''
```

## Problem2: about()

about是一个高阶函数，他返回的函数作用是：判断keywords是否在一段字符串中。

Implement the about function, which takes a list of words called keywords. It returns a function that, when given a paragraph, checks whether the paragraph contains any of the words in keywords.
The returned function will return True if any of the words in the keywords list are found in the paragraph and False otherwise.
Hint: Use the split, lower, and remove_punctuation functions in utils.py.

Once about is implemented, we can use the function it returns as the select argument in pick.
```python
>>> from cats import about
>>> from cats import pick
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A paragraph about cats.')
False

>>> dogs('A paragraph about dogs.')
True

>>> dogs('Release the Hounds!')
True

>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
True

>>> dogs('Do gs and ho unds don\'t count')
False

>>> dogs("AdogsParagraph")
False

```

## problem 3：accuracy - percentage of words entered correctly

精确度评分函数。评分规则：

    如果输入大于样例，超出的部分全算错误
    如果输入小于等于样例，则一一匹配，对的上的计分。 length/100 * coorrect_count
    如果二者其中之一为空，另一为非空，则为0.0分。

Implement accuracy, which takes both a entered paragraph and a source paragraph.
It returns the percentage of words in entered that exactly match the corresponding words in source.
Case and punctuation must match as well. "Corresponding" means that each word in entered must appear in the same position as the matching word in source.
In other words, the first word in entered must match the first word in source, the second word in entered must match the second word in source, and so on.

A word in this context is any sequence of characters separated from other words by whitespace. Therefore, treat sequences like "dog;" as a single word.

In the actual typing test, entered represents what the player has typed, and source is the paragraph they are attempting to replicate.

    If entered is longer than source, then the extra words in entered that have no corresponding word in source are all incorrect.
    If entered is shorter than source and all the words in entered correspond to source so far, then the accuracy is 100.0.
    If entered is empty and source is empty, then the accuracy is 100.0.
    If entered is empty but source is not empty, then the accuracy is 0.0.
    If entered is not empty but source is empty, then the accuracy is 0.0.

```python
>>> from cats import accuracy
>>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
100.0

>>> accuracy("a b c", "a b c")
100.0

>>> accuracy("a  b  c  d", "b  a  c  d")
50.0

>>> accuracy("a b", "c d e")
0.0

>>> accuracy("Cat", "cat") # the function is case-sensitive
0.0

>>> accuracy("a b c d", "a d")
25.0

>>> accuracy("abc", " ")
0.0

>>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
100.0

>>> accuracy("abc", "")
0.0

>>> accuracy("", "abc")
0.0

>>> accuracy("a b c d", "b c d")
0.0

>>> accuracy("cats.", "cats") # punctuation counts
0.0

>>> accuracy("", "") # Returns 100.0
100.0
```

## Problem 4：wpm()

**wpm: word per minutes, 计算打字速度**，包括空格，不包括引号。

Implement wpm, which computes the words per minute, a measure of typing speed, given a string entered and the amount of elapsed time in seconds. Despite its name, words per minute is not based on the number of words typed, but instead the number of groups of 5 characters, so that a typing test is not biased by the length of words.

The formula for words per minute is calculated by dividing the total number of characters typed (including spaces) by 5 (the average word length) and then dividing the result by the elapsed time in minutes.

For example, the string "I am glad!" contains ten characters (not including the quotation marks). The words per minute calculation uses 2 as the number of words entered (because 10 / 5 = 2). If someone typed this string in 30 seconds (half a minute), their speed would be 4 words per minute.

*python3 ok -q 04 -u*
```python
>>> from cats import wpm
>>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
20.0

>>> wpm("a b c", 20)
3.0

>>> wpm("", 10)
0.0
```

# Phase 2：Autocorrect
## Problem 5: auotocorrect()

Implement autocorrect, which takes a entered_word, a word_list, a diff_function, and a limit.
The goal of autocorrect is to return the word in word_list that is closest to the provided entered_word, as determined by diff_function.

Specifically, autocorrect does the following:

    If the entered_word is contained inside the word_list, autocorrect returns that word.
    Otherwise, autocorrect returns the word from word_list that has the lowest difference from the provided entered_word. This difference is the number returned by the diff_function.
    However, if the lowest difference between entered_word and any of the words in word_list is greater than limit, then entered_word is returned instead. In other words, limit sets a maximum threshold on how severe a typo can be for it to still be corrected.

Assume that entered_word and all elements of word_list are lowercase and have no punctuation.

A diff function takes in three arguments. The first is the entered_word, the second is the source word (in this case, a word from word_list), and the third argument is the limit.
The output of the diff function, which is a number, represents the amount of difference between the two strings.

*python3 ok -q 05 -u*
```python
>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
? "cult"

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
? "cul"

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
? 'car'

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
? 'word'

>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
? 'inside'

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
? 'idea'

>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
? 'outside'
```

## Problem 6: furry_fixes

**A diff_function**
将一个单词变成另一个单词需要改变的字母的数量。不等长，对比等长的前几个字符，最后的结果再加上长度差。

This function takes in two strings and returns the minimum number of characters that must be changed in the entered word in order to transform it into the source word.
If the strings are not of equal length, the difference in lengths is added to the total change count.
Important: You may not use while, for, or list comprehensions in your implementation. Use recursion.
If the number of characters that must change is greater than limit, then furry_fixes should return any number larger than limit and should minimize the amount of computation needed to do so.

*python3 ok -q 06 -u*
```python
>>> from cats import furry_fixes, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> furry_fixes("car", "cad", big_limit)
? 1

>>> furry_fixes("this", "that", big_limit)
? 2

>>> furry_fixes("one", "two", big_limit)
? 3

>>> furry_fixes("from", "form", big_limit)
? 2

>>> furry_fixes("awe", "awesome", big_limit)
? 4

>>> furry_fixes("awful", "awesome", big_limit)
? 5

>>> furry_fixes("awful", "awesome", 3) > 3
? True

>>> furry_fixes("awful", "awesome", 4) > 4
? True

>>> furry_fixes("awful", "awesome", 5) > 5
? False
```