# Lab04: Sequences, Tree Recursion, Trees

Topics:
    
    Sequences, Tree Recursion, Data Abstraction, Trees.

## Q1: Map

my_map takes in a one argument function fn and a sequence seq and returns a list containing fn applied to each element in seq.

Use only a single line for the body of the function. (Hint: use a list comprehension.)

## Q2: Filter

my_filter takes in a predicate function pred and a sequence seq and returns a list containing all elements in seq for which pred returns True. (A predicate function is a function that takes in an argument and returns either True or False.)

Use only a single line for the body of the function. (Hint: use a list comprehension.)

## Q3: Reduce

my_reduce takes in a two argument function combiner and a non-empty sequence seq and combines the elements in seq into one value using combiner.

## Data Abstraction for Next Qs

Say we have a data abstraction for cities. A city has a name, a latitude coordinate, and a longitude coordinate.

Our data abstraction has one constructor:

    make_city(name, lat, lon): Creates a city object with the given name, latitude, and longitude.

We also have the following selectors in order to get the information for each city:

    get_name(city): Returns the city's name
    get_lat(city): Returns the city's latitude
    get_lon(city): Returns the city's longitude


## Q4: Distance

We will now implement the function distance, which computes the distance between two city objects. 

Recall that the distance between two coordinate pairs (x1, y1) and (x2, y2) can be found by calculating the sqrt of (x1 - x2)^2 + (y1 - y2)^2. We have already imported sqrt for your convenience. 

Use the latitude and longitude of a city as its coordinates; you'll need to use the selectors to access this info!

## Q5: Closer City

Implement closer_city, a function that takes a latitude, longitude, and two cities, and returns the name of the city that is closer to the provided latitude and longitude.

You may only use the selectors get_name get_lat get_lon, constructors make_city, and the distance function you just defined for this question.

Hint: How can you use your distance function to find the distance between the given location and each of the given cities?

返回值为城市的名字，而不是city这一数据对象。

## Q6: Don't violate the abstraction barrier!

Note: this question has no code-writing component (if you implemented the previous two questions correctly).

## Q7: WWPD: Trees

Tree Abstraction 在lab04.py文件最后。回答问题前，不明白tree()的可以先看，也可以直接 python3 -i。

```python
>>> from lab04 import *
>>> t = tree(1, tree(2))
Error

>>> t = tree(1, [tree(2)])
Nothing

>>> label(t)
1

>>> label(branches(t)[0])
2

>>> x = branches(t)
>>> len(x)
1

>>> is_leaf(x[0])
True

>>> branch = x[0]
>>> label(t) + label(branch)
3

>>> len(branches(branch))
0

>>> from lab04 import *
>>> b1 = tree(5, [tree(6), tree(7)])
>>> b2 = tree(8, [tree(9, [tree(10)])])
>>> t = tree(11, [b1, b2])
>>> for b in branches(t):
...     print(label(b)) # shift + enter -> 开始/结束换行
(line1)5
(line2)8

>>> for b in branches(t):
...     print(is_leaf(branches(b)[0]))
True
False


>>> [label(b) + 100 for b in branches(t)]
[105, 108]

>>> [label(b) * label(branches(b)[0]) for b in branches(t)]
[30, 72]
```

## Q8: Perfectly Balanced

Implement sum_tree, which returns the sum of all the labels in tree t.
Then, implement balanced, which returns whether every branch of t has the same total sum and that the branches themselves are also balanced.

### 重要辨析——源于Deepseek和lab04前attendence中的知识

在 CS61A 的这种定义下（tree 返回 [label] + list(branches)），树（Tree）和树枝列表（List of branches）在 Python 底层类型上确实都是 list。

这恰恰是初学抽象数据类型（ADT）时最令人困惑的地方：“运行时类型” 和 “抽象语义类型” 的区别。

既然它们底层都是列表，那为什么 balanced(b) 能工作，而 balanced(branches(t)) 会出大问题？我们来用 “数据形状（Shape）” 的视角彻底拆穿这个陷阱。


#### 1. 拆解数据形状（Shape）

假设我们有一棵树：t = tree(1, [tree(2), tree(3)])

根据 tree 的定义，t 在内存中的实际样子是：

```python
[1, [2], [3]]
```
b（单个分支）：当 for b in branches(t): 循环时，b 第一次拿到的是 [2]，第二次拿到的是 [3]。

    b 的形状是：[标签, 子树枝列表]（即 [int, list]）。

branches(t)（树枝列表）：它的值是 \[ [2], [3] ]。

    它的形状是：[树, 树]（即 [list, list]）。


#### 2. 代入 balanced 函数看会发生什么（致命逻辑错乱）
我们的 balanced 函数第一行通常是 label(t) 或检查 branches(t)。我们代入看看：

正确情况：balanced(b)，传入 [2]

    label(b) 会执行 b[0]，返回 2（整数）。✅ 符合预期。

    branches(b) 会执行 b[1:]，返回 []（空列表）。✅ 叶子节点。

错误情况：balanced(branches(t))，传入 [[2], [3]]

    label(传入值) 会执行 传入值[0]，返回 [2]（这是一个列表，而不是一个整数标签！）。💥 逻辑错误。

    branches(传入值) 会执行 传入值[1:]，返回 [[3]]（它把第二个子树当成了“树枝列表”）。💥 结构错乱。

结论：虽然 Python 不会报 TypeError（因为都是 list，下标操作都能执行），但函数内部的逻辑完全错位了。它会把第一个子树 [2] 误当成“标签”，把剩下的子树 [[3]] 误当成“树枝”。这会算出完全错误的求和或判断，或者因为类型不匹配（比如拿列表去加整数）而抛出 TypeError。

#### 3. 为什么课堂上还要这样定义？（抽象屏障）
你可能会想：“既然这么容易混淆，为什么不把树定义成自定义类（Class）？”

CS61A 故意这样用列表实现，是为了教你“抽象屏障（Abstraction Barrier）”：

构造函数 tree 和选择器 label / branches 是你与数据交互的唯一合法接口。

即使底层是列表，你在写 balanced 时，脑子里绝对不能把树当成列表，必须把它们当成“节点”和“节点列表”。

如果你试图绕过选择器，直接把 branches(t)（一个列表）塞给 balanced（它期望节点），你就打破了抽象屏障，代码会立刻崩溃。

branches(t) 是“装树的篮子”，b 才是“树”本身。
递归函数只收“树”，不收“篮子”。

所以，当你需要检查所有分支时，必须从篮子里一个一个把树取出来（for b in branches(t)），再交给递归函数。绝对不能把整个篮子丢进去。

## Q9: Number of Trees (Optional)

A full binary tree is a tree where each node has either 2 branches or 0 branches, but never 1 branch.

Write a function which returns the number of unique full binary tree structures that have exactly n leaves. See the doctests for visualizations of the possible full binary tree sturctures that have 1, 2, and 3 leaves.

Hint:

    A full binary tree can be constructed by connecting two smaller full binary trees to a root node. 

    If the two smaller full binary trees have a and b leaves, the new full binary tree will have a + b leaves.

    For example, as shown in the first diagram below, a full binary tree with 4 leaves can be constructed by connecting a full binary tree that has three leaves (yellow) with a full binary tree that has one leaf (orange).
    A full binary tree with 4 leaves can also be constructed by connecting two full binary trees with 2 leaves each (second diagram)

```python
def num_trees(n):
    if n == 1:
        return 1
    total = 0
    for i in range(1, n):
        total += num_trees(i) * num_trees(n - i)
    return total
```
存在重复计算，越是前面的项计算次数越多。所以需要一个缓存序列，记录以前计算过的值。之后，遇见该值可直接根据索引获取。
如果使用序列缓存计算过的值，那么num_trees函数的返回值就是序列对应的值。

## Q10: Only Paths (Optional)

Implement only_paths, which takes a Tree of numbers t and a number n. It returns a new tree with only the nodes of t that are on a path from the root to a leaf with labels that sum to n, or None if no path sums to n.

寻找树t 总和为n 的路径，并组成新的树。