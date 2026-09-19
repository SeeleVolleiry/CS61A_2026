# Lab08: Linked Lists

A linked list is either a Link instance or Link.empty (which represents an empty linked list).
A instance of Link has two instance attributes, first and rest.
The rest attribute of a Link instance should always be a linked list: either another Link instance or Link.empty.
To check if a linked list is empty, compare it to Link.empty. Since there is only ever one empty list, we can use is to compare, but == would work too.
You can mutate a Link object s in two ways:

    Change the first element with s.first = ...
    Change the rest of the elements with s.rest = ...
    You can make a new Link object by calling Link:

You can make a new Link object by calling Link:

    Link(4) makes a linked list of length 1 containing 4.
    Link(4, s) makes a linked list that starts with 4 followed by the elements of linked list s.

# Q1: WWWPD: Linked Lists

Read over the Link class. Make sure you understand the doctests.
Use Ok to test your knowledge with the following "What Would Python Display?" questions.
Enter Function if you believe the answer is function, Error if it errors, and Nothing if nothing is displayed.

If you get stuck, try drawing out the box-and-pointer diagram for the linked list on a piece of paper or loading the Link class into the interpreter with python3 -i lab07.py.

*python3 ok -q link -u*
```python
---------------------------------------------------------------------
What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab08 import *
>>> link = Link(1000)
>>> link.first
? 1000
-- OK! --

>>> link.rest is Link.empty
? True
-- OK! --

>>> link = Link(1000, 2000)
? Error
-- OK! --

>>> link = Link(1000, Link())
? Error
-- OK! --

---------------------------------------------------------------------
What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab08 import *
>>> link = Link(1, Link(2, Link(3)))
>>> link.first
? 1
-- OK! --

>>> link.rest.first
? 2
-- OK! --

>>> link.rest.rest.rest is Link.empty
? True
-- OK! --

>>> link.first = 9001
>>> link.first
? 9001
-- OK! --

>>> link.rest = link.rest.rest
>>> link.rest.first
? 3
-- OK! --

>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest is Link.empty # link.rest.rest = link.rest = link
? False
-- OK! --

>>> link.rest.rest.rest.rest.first
? 1         
-- OK! --

>>> link = Link(2, Link(3, Link(4)))
>>> link2 = Link(1, link)
>>> link2.first
? 1
-- OK! --

>>> link2.rest.first
? 2
-- OK! --
---------------------------------------------------------------------
What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab08 import *
>>> link = Link(5, Link(6, Link(7)))
>>> link                  # Look at the __repr__ method of Link
? Link(5, Link(6, Link(7)))
-- OK! --

>>> print(link)           # Look at the __str__ method of Link
? (5 6 7)  
-- OK! --
```

# Q2: Withoutone

Implement without, which takes a linked list s and a non-negative integer i. It returns a linked list with all of the elements of s except for the one at index i. (Assume s.first is the element at index 0.)

The original linked list s should not be changed.

Hint: Using recursive approach might be easier than the iterative approach.

解题思路：

    题目提示使用递归，那么首先要判断递归函数是什么，递归函数的作用是什么？：先尝试使用withoutone()作为递归函数。
    从函数的定义可以看出，函数的返回值很明显是Link类。
    知道了递归函数的作用，接下来就是递归间的关系了，也就是递归调用：
        withoutone返回去掉了第i个元素的链表，i=0时去掉s.first。
        withoutone(s, i) = s.first 和 withoutone(s.rest, i-1)组成链表
    最后则是，基准条件：这很简单，要么递归到最后，能够找到第i个元素，此时i=0；要么到最后，找不到第i个元素——链表没有足够的长度，此时递归到最后，s变成了空链表，即Link.empty。

# Q3: Duplicate Link

Write a function duplicate_link that takes in a linked list s and a value val. It mutates s so that each element equal to val is followed by an additional val (a duplicate copy). It returns None. Be careful not to get into an infinite loop where you keep duplicating the new copies!

Note: In order to insert a link into a linked list, reassign the rest attribute of the Link instances that have val as their first. Try drawing out a doctest to visualize!

解题思路：防止无限循环，我认为应该先递到底，然后在归的过程中判断是否要修改原序列。
```python
# 方案 B
def duplicate_link(s, val): # 在归的过程中修改，不用担心无限循环。
    if s.rest is not Link.empty:
        duplicate_link(s.rest,val)

    if s.first == val:
        s.rest = Link(val, s.rest)

# 方案 B：更规范的写法——基准改为判"空链表"，放在最前面
def duplicate_link ( s, val ):
    if s is Link.empty: 
        return
    
    duplicate_link(s.rest, val) 
    
    if s.first == val:
        s.rest = Link(val, s.rest)
# 方案A
def duplicate_link(s, val): # 按顺序遍历，在递的过程中修改
    if s is Link.empty:
        return
    if s.first == val:
        s.rest = Link(val, s.rest)
        duplicate_link(s.rest.rest, val) # 跳过新加的元素
    else:
        duplicate_link(s.rest, val)
```

# Q4: Slice

Implement a function slice_link that slices a given linked list link.

slice_link should slice the link starting at start and ending one element before end, as with a normal Python list.

Additionally, similar to slicing normal Python lists, this function should return a new list and not modify the original list.

Q4（Slice）的核心是**"窗口"思想**：把`[start, end)` 想成一个滑动的窗口，递归就是让窗口在链表上右移——先丢掉窗口左边的节点，再收集窗口内的节点。

把"窗口滑动"翻译成递归——两个阶段、两个基准：

- 阶段一（跳过） ：`start > 0` ，当前节点还在窗口 左边 → 丢掉它，窗口整体右移一位：`slice_link(link.rest, start - 1, end - 1)` 。 注意`end` 也要减 1 ——窗口平移时长度不变（类比`lst[1:4]` 和`lst[2:5]` 都是 3 个元素，只是起点不同）。
- 阶段二（收集） ：`start == 0` ，当前节点在窗口内 → 用`Link(link.first, ...)` 收下它，窗口右侧收缩：`end - 1` 。
- 基准 1 ：链表走空 →`Link.empty` （兜住`end` 超长、`start` 超长的情况）。
- 基准 2 ：`end == 0` → 窗口收完 →`Link.empty` 。


# Q5: Cycles

Implement has_cycle,that returns whether its argument, a Link instance, contains a cycle.

Hint: Iterate through the linked list and try keeping track of which Link objects you've already seen.

如果是个环，沿着走一定能有重复的rest。注意，不是值重复。
判断标准只有一条： 沿着`rest` 一直走，能不能走到`Link.empty` 。