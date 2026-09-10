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
"cult"

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
"cul"

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
'car'

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
'word'

>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
'inside'

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
'idea'

>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
'outside'
```

## Problem 6: furry_fixes

**A diff_function**
将一个单词变成另一个单词需要改变的字母的数量。不等长，对比等长的前几个字符，最后的结果再加上长度差。

不允许使用循环和列表推导式，要求使用递归。furry_fixes可以是高阶函数。
思路：

    要求使用递归函数，那么首先要知道需要一个什么样的递归函数，这个函数能做什么/功能、参数是什么和返回值是什么：
    我想设计一个递归函数，其作用是从第一个元素开始逐项对比。相同则下一个元素且错配字符数不增加，不相同错配字符数加一然后对比下一个。
    递归函数有三个参数，输入字符串的即将参与对比的索引 idx_e、匹配/样例字符串的即将参与对比的索引 idx_s 和对不上的字符数/错配字符数mismatch。
    
    然后，就需要递推关系（递归调用）：
    上一个函数的值 = 下一个调用函数的值 + 上一个函数中对比结果的值（0 或者 1）

    最后，判断递归的基准条件——什么时候停止：
    第一个条件是题目强制要求的。当错配数量超过limit是就直接 return。
    两边都是字符串，逐项对比，形象于两个指针同频滑动。显然，（至少）一个指针指到底部，意味着到了函数调用尽头了，该针对计算该情况的返回值。
    当entered长度小于source时（idx_e先到达最值），source与entered的长度差就是返回值。同样的道理也适合于entered更长时。

    当这些都有了之后，就可以def递归函数了，furry_fixes的返回值就应该是 参数idx_e=0，idx_s=0， mismatch=0的递归函数。

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
1

>>> furry_fixes("this", "that", big_limit)
2

>>> furry_fixes("one", "two", big_limit)
3

>>> furry_fixes("from", "form", big_limit)
2

>>> furry_fixes("awe", "awesome", big_limit)
4

>>> furry_fixes("awful", "awesome", big_limit)
5

>>> furry_fixes("awful", "awesome", 3) > 3
True

>>> furry_fixes("awful", "awesome", 4) > 4
True

>>> furry_fixes("awful", "awesome", 5) > 5
False
```

## Problem 7: 补全minimum_mewtations()函数

计算 使用三种固定操作 将 entered转换为source 的 最少操作数。

Implement minimum_mewtations, a more advanced diff function that can be used in autocorrect, which returns the minimum number of edit operations needed to transform the entered word into the source word.

There are three kinds of edit operations, with some examples:

    1. Add a letter to entered.
        Adding "k" to "itten" gives us "kitten".
    
    2. Remove a letter from entered.
        Removing "s" from "scat" gives us "cat".
    3. Substitute a letter in entered for another.
        Substituting "z" with "j" in "zaguar" gives us "jaguar".

    Each edit operation increases the difference between two words by 1.

If the number of edits required is greater than limit, then minimum_mewtations should return any number larger than limit (such as limit + 1) and should stop making recursive calls once the limit is reached to save time.

Important: You should not use any helper functions in your implementation of minimum_mewtations. Otherwise the autograder test might fail.

*python3 ok -q 07 -u*
```python
>>> from cats import minimum_mewtations, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> minimum_mewtations("wind", "wind", big_limit)
0

>>> minimum_mewtations("wird", "wiry", big_limit)
1

>>> minimum_mewtations("wird", "bird", big_limit)
1

>>> minimum_mewtations("wird", "wir", big_limit)
1

>>> minimum_mewtations("wird", "bwird", big_limit)
1

>>> minimum_mewtations("speling", "spelling", big_limit)
1

>>> minimum_mewtations("used", "use", big_limit)
1

>>> minimum_mewtations("hash", "ash", big_limit)
1

>>> minimum_mewtations("ash", "hash", big_limit)
1

>>> minimum_mewtations("roses", "arose", big_limit)     # roses -> aroses -> arose
2

>>> minimum_mewtations("tesng", "testing", big_limit)   # tesng -> testng -> testing
2

>>> minimum_mewtations("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
3

>>> minimum_mewtations("", "", big_limit) # nothing to nothing needs no edits
0
```

**补全思路**：不能使用高阶函数

    函数框架已经给好，只是补全代码。补全递归函数的代码重点在于明白递归函数的作用、找出递推关系，完成基准条件和调用条件。

    递归函数的作用题目写得很明白，返回最小操作数。所以直接看递推关系：
    两个函数之间的关系，无非是应用了某种操作后，操作数加一再加上剩下字符串的最小操作数。即 上一个值 = 1或者0 + 下一个值。
    如果相等，自然简单——利用列表推导式，接着进行匹配。
    但是，具体是哪种操作才会使后续最小呢？这很难事先而知。再看代码三种操作都各有一行，属于变量赋值，而不是实现操作entered的函数（否则也就不止一行了）。所以，递归调用以及加一应该在这里完成，最终取三者的最小值返回。
    add的作用是在entered[0]前假设增加一个字符，使得该字符与source[0]匹配。匹配次数加1。因此，add中下一个调用的函数参数应为entered,source[1:],limit-1。
    remove的作用是移除entered的第一个元素，所以下一次从entered的第二个和source的第一个开始对比。也就是：minimum_mewtations(entered[1:], source, limit-1)
    substitute的作用是替换entered的第一个元素，假设替换后使其相等。所以下一次，比较从二者的第二个字符开始。也即：minimum_mewtations(entered[1:], source[1:], limit-1)

    现在只差基准条件：
    当limit逐渐减小，小于0时，说明超过了最大限度，直接返回值。
    当他们长度一样时，到匹配结束，都是空字符串，下一步操作不存在，返回0去累加求操作数的和。
    当他们长度不一样时，到匹配结束，其中一个为空字符串。这时，二者存在长度差。最小的操作数就是增加对应差值数量的字符，即是操作数为长度差的绝对值。返回这一绝对差值即可。

# Phase 3：Multiplayer
## Problem 8：report_progress

计算单词数的正确率：从第一个元素开始匹配，直到出现第一个不相符的元素。返回计算出的正确率。

Implement report_progress, which is called every time the user finishes typing a word. It takes a list of the words entered so far, a list of the words in the source text, the user's user_id, and an upload function that is used to upload a progress report to the multiplayer server. 

Your progress is a ratio of the words in the source that you have entered correctly, up to the first incorrect word, divided by the number of source words. 
For instance, this example has a progress of 0.25:

    report_progress(["Hello", "ths", "is"], ["Hello", "this", "is", "wrong"], ...)

*python3 ok -q 08 -u*
```python
>>> from cats import report_progress
>>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
>>> entered = ['I', 'have', 'begun']
>>> source = ['I', 'have', 'begun', 'to', 'type']
>>> print_progress({'id': 1, 'progress': 0.6})
ID: 1 Progress: 0.6

>>> report_progress(entered, source, 1, print_progress) # print_progress is called on the report
(line 1) ID: 1 Progress: 0.6
(line 2) 0.6

>>> report_progress(['I', 'begun'], source, 2, print_progress)
(line 1) ID: 2 Progress: 0.2
(line 2) 0.2

>>> report_progress(['I', 'hve', 'begun', 'to', 'type'], source, 3, print_progress)
(line 1) ID: 3 Progress: 0.2
(line 2) 0.2  
```


## Problem 9：time_per_word()

返回一个字典{'words': words_list, 'times': times_list}

Implement time_per_word, which takes in two arguments:

    words: a list of words that players are typing.
    timestamps_per_player: a list of lists where each inner list contains the timestamps indicating when each player finished typing each word in words.

The function should return a dictionary with the following structure:

    'words': The list of words that the players are typing.
    'times': A list of lists times that stores the durations it took each player to type each word. Specifically, the value at times[i][j]should indicate how long it took player i to type the word at words[j]. This would be the difference between when the player finished typing words[j] and when the player finished typing words[j-1]. For words[0], this would be the difference between when the player finished typing words[0] and when the player started typing.
    Timestamps found in the parameter timestamps_per_player are cumulative and always increasing, while the values in times are differences between consecutive timestamps for each player.

Here's an example: If timestamps_per_player = [[1, 3, 5], [2, 5, 6]], then times would be [[2, 2], [3, 1]].
This is because the first player finished typing each word at timestamps 1, 3, and 5, while the second player finished typing each word at timestamps 2, 5, and 6.
So the differences in timestamps are (3-1), (5-3) for the first player and (5-2), (6-5) for the second player. The first value of each list within timestamps_per_player represents the initial starting time for each player.

*python3 ok -q 09 -u*
```python
>>> from cats import *
>>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
>>> words = ['This', 'is', 'fun']
>>> words_and_times = time_per_word(words, p)
>>> words, times = words_and_times['words'], words_and_times['times']
>>> words
['This', 'is', 'fun']

>>> times
[ [3, 2, 1], [4, 2, 3] ]

>>> p = [[0, 2, 3], [2, 4, 7]]
>>> words, times = words_and_times['words'], words_and_times['times']
>>> words
['hello', 'world']

>>> words[1]
'world'

>>> times
[ [2, 1], [2, 3] ]

>>>times[0][1]
1
```

## Problem 10：fastest_words()

Implement fastest_words, which returns which words each player entered fastest. This function is called once all players have finished typing. *It takes in a dictionary returned by time_per_word.*

*The fastest_words function returns a list of lists of words, one list for each player.* 

    The index of the nested list denotes the player. 
    The list for each player contains the words they entered faster than all the other players.
    In the case of a tie, the player with the smallest index is considered to be the one who entered it the fastest.

For example, consider two players who typed Just have fun. Player 0 typed 'fun' the fastest (3 seconds), Player 1 typed 'Just' the fastest (4 seconds), and they tied on the word 'have' (both took 1 second). In this case, Player 0 is considered the fastest for 'have' because their index is smaller.

    player_0 = [5, 1, 3]
    player_1 = [4, 1, 6]
    fastest_words({'words': ['Just', 'have', 'fun'], 'times': [player_0, player_1]})
    [['have', 'fun'], ['Just']]

Use the helper function get_time (provided) to get an individual time from times. It provides helpful error messages when you try to access a time that doesn't exist.

def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
Important: Make sure your implementation does not mutate the given player input lists. For the example above, calling fastest_words on [player_0, player_1] should not mutate player_0 or player_1.

There might not always be two players, so generalize this function in a way that will allow it to handle an indeterminate number of players.

*python3 ok -q 10 -u*
```python
>>> from cats import fastest_words, get_time
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 2]
>>> get_time([p0, p1], 0, 1)
2

>>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})
[ ['What',], ['great', 'luck'] ]

>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 3]
>>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})  # with a tie, choose the first player
[ ['What','luck'], ['great'] ]  

>>> p2 = [4, 3, 1]
>>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1, p2]})
[ ['What'], ['great'], ['luck'] ] 
```