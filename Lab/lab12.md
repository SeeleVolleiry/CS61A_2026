# Final Review

# Mutable Trees
## Q1: Delete

这题是补全Delete函数的代码。

Implement delete, which takes a Tree t and removes all non-root nodes labeled x.
The parent of each remaining node is its nearest ancestor that was not removed. The root node is never removed, even if its label is x.

易混淆处为参数t属于Tree类的实例，没有branches()方法
# Recursion and Tree Recursion
## Q2: Subsequences

同样补全函数代码

A subsequence of a sequence s is a subset of elements from s, in the same order they appear in s.

Write a function that takes in a list and returns all possible subsequences of that list. The subsequences should be returned as a list of lists, where each nested list is a subsequence of the original input.

解题思路：

    先看insert_into_all：
        题目假定嵌套列表是列表的列表，即只有一层嵌套。因此，可以直接以一层for循环，对每个元素的开头插入一个item。
        因为Link类没有insert方法所以只能用+拼接
        该函数要求返回一个新列表，这是注意点，可以使用列表推推导式。
    subseqs函数是递归函数，通过观察测试用例和结合题目要求要先写insert_into_all，能发现：
        子列表 = s[0] insert_into_all s[1:] + s[1:]的子列表
        这就是递推关系。

## Q3: Non_Decreasing Subsequences

补全函数代码：该函数生成参数序列的子序列，并且子序列中元素从左到右要满足非下降条件。

树形递归在于每次递归调用时不是只调用一次，而是调用两次甚至多次：
    
    递推关系中不是一个大问题包含一个小问题和另一部分“常量”，而是一个多大问题包含几个不同走向的同级小问题。
    例如二分：满足某个条件/需要某个因素-调用一次，不满足/不需要某个因素-调用一次

We want to write a function that takes a list and returns a list of lists, where each individual list is a subsequence of the original input.

However, we have a condition: we only want the subsequences for which consecutive elements are nondecreasing. For example, [1, 3, 2] is a subsequence of [1, 3, 2, 4], but since 2 < 3, this subsequence would not be included in our result.

You may assume that the list passed in as s contains only nonnegative elements.

You may use the insert_into_all helper function.

# Mutability
## Q4: Common Players

转换字典，重新划分键值对。/字典反转

Implement the function common_players. The common_players function takes in a roster dictionary that maps players to their teams, and returns a new dictionary that maps teams to a list of players on that team.
The order of player names in the list does not matter.

解题思路： 要求返回一个新字典

    字典的键、值遍历：字典的items方法。
    遍历旧字典：值没在新字典出现过就把值作为新的键，该值对应的键作为值；如果值出现过：在新字典对应的键下添加该值的键。

# Generator
## Q5: Stair Ways

n阶的楼梯，每次只走1步或者2步。有哪些走法？用有1、2组成的嵌套列表来表示，每个元素是一种走法的列表。

解题思路：提示让我们用递归思维来思考和解决问题

# OOP：Object-Oriented Programming
## Q6: Player




## Q7: Game




## Q8: New Players (optional)




# Linked List
## Q9: Two List （Linked LIsts）

two_list函数接收两个参数，二者都为List。第一个List参数是要放入新建Link类的值，第二个List参数是对应位置上第一个参数值出现的次数。

解题思路：
    
    两个参数List都要遍历取出对应值：一者决定添加哪个值，一者决定被添加值的添加次数。
    第一想法是两层循环。第一层循环，若是正向从index=0到index=-1，要有一个rest跟踪。这似乎有点麻烦。所以，用元素角标选择倒序取出vals中的元素。
    第二层循环管理次数。同样需要倒序，按照索引取出。


# Scheme/Tail Recursion
## Q10: Accumulate

函数的作用是对每项使用merger（一个双参数函数，对两个参数执行要求的运算，如加减乘除）。该数列的第一项为start，其余项为term(1)到term(n)。
这首先想到的就是利用递归。

可以先假定递归函数就是accumulate。下一步是寻找递推关系：accumulate(merger start n term) = accumulate（merger start n-1 term） + term(n)。
最后则是基准条件。什么时候停止？假设n=1的时候停止，数列还有term(1)和start两项，可以选择返回 (merger start term(1));也可以选择n=0时返回start。
具体如何选择，根据实际的代码反馈来调整。

Fill in the definition for the procedure accumulate, which joins the first n natural numbers (ie. 1 to n, inclusive) according to the following parameters:

    merger: a function of two arguments
    start: a number with which we start joining
    n: the number of natural numbers to join
    term: a function of one argument that computes the nth term of a sequence

*python3 ok -q accumulate -u*
```scheme
scm> (load-all ".")
scm> (define (identity x) x)
scm> (accumulate * 1 5 identity)
? 120
-- OK! --

scm> (accumulate * 2 4 identity)
? 48
-- OK! --


scm> (load-all ".")
scm> (define (square x) (* x x))
? square
-- OK! --

scm> (accumulate + 0 5 square)
? 55
-- OK! --

scm> (accumulate + 5 5 square)
? 60
-- OK! --

scm> (accumulate + 2 3 square)
? 16
-- OK! --
```

## Q11: Tail Recursive Accumulate (optional)

将Q10的递归函数改为尾递归形式的递归函数。如果Q10已经是尾递归函数，则直接复制。

解题思路：
尾递归是在最后一次递归时，需要计算的结果已经计算好了。后面只需要用return给上一层，return后不再进行任何操作/计算。
因此，需要有一个变量存储累计计算的结果，到最后一层（基准条件）直接返回这一变量即可。
多了这一个变量追踪结果，我们可以考虑accumulate-tail作为一个高阶函数，内部编写一个辅助函数来实现具体的尾递归。

    首先，需要确定辅助函数tail-helper的作用是什么。如上所述：返回追踪累计结果的值
    其次，需要哪些参数？
    再者，如何操作已有的结果得到下一个结果？如何递归调用，开始下一次操作？ 
        纯函数式 Scheme 里不能用`begin` "先算再存" ，累积器的值必须通过参数传递。
    最后，什么时候停止递归？