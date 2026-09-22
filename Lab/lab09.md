# Lab09: Scheme, Scheme Lists

## Q1: Over or Under

定义过程`over-or-under` ，接收两个数字`num1` 、`num2` ，返回：`-1` （num1 < num2）、`0` （num1 = num2）、`1` （num1 > num2）。

## Q2: Compose

编写过程`composed` ，接收过程`f` 和`g` ，返回一个新过程；该过程接收`x` ，返回`f(g(x))` 的结果。
Note: Remember to use Scheme syntax when calling functions. The form is (func arg), not func(arg).

## Q3: Repeat

编写过程`repeat` ，接收过程`f` 和数字`n` ，返回一个新过程；该过程接收`x` ，返回把`f` 应用于`x` 共`n` 次的结果。
Hint: The composed function you wrote in the previous problem might be useful.

## Q4: WWSD: Lists

WWSD: What Would Scheme Do?

    scm> (cons 1 (cons 2 nil))                    → (1 2)
    scm> (car (cons 1 (cons 2 nil)))              → 1
    scm> (cdr (cons 1 (cons 2 nil)))              → (2)
    scm> (list 1 2 3)                             → (1 2 3)
    scm> '(1 2 3)                                 → (1 2 3)
    scm> (cons 1 '(list 2 3))                     → (1 list 2 3)
    scm> (cons 1 `(list 2 3))                     → (1 list 2 3)
    scm> '(cons 4 (cons (cons 6 8) ()))           → (cons 4 (cons (cons 6 8) ()))
    scm> (cons 1 (list (cons 3 nil) 4 5))         → (1 (3) 4 5)

## Q5: Make a List 

根据给定的 box-and-pointer（方框指针）图（即`sepc`），构造对应的列表`lst` 。
构造一个列表使之满足题目给出的图示关系和元素。

```Python
---------------------------------------------------------------------
scm> (load-all ".")
scm> (define a '(1))
? a
-- OK! --

scm> a
? (1)
-- OK! --

scm> (define b (cons 2 a))
? b
-- OK! --

scm> b
? (2 1)  
-- OK! --

scm> (define c (list 3 b))
? c
-- OK! --

scm> c
? (3 (2 1)) 
-- OK! --

scm> (car c)
? 3
-- OK! --

scm> (cdr c)
? ((2 1))
-- OK! --

scm> (car (car (cdr c)))
? 2
-- OK! --

scm> (cdr (car (cdr c)))
? (1)
-- OK! --

scm> (load-all ".")
scm> lst ; type out exactly how Scheme would print the list that will be defined in this problem (see spec)
? ((1) 2 (3 4) 5)  
-- OK! --
```

## Q6: Without Duplicates

实现`without-duplicates` ，接收数字列表`lst` ，返回包含`lst` 中所有首次出现的唯一元素的新列表，顺序按首次出现、且无重复。
提示：用`=` 判等，配合`not` 与辅助`lambda` 使用`filter` 。

    解锁测试：
    (without-duplicates (list 5 4 2))           (5 4 2) 
    (without-duplicates (list 5 4 5 4 2 2))     (5 4 2) 
    (without-duplicates (list 5 5 5 5 5))       (5) 
    (without-duplicates ())                     ()

解题思路：
题目提示使用 filter、lambda、= 和 not，这强烈暗示我们应该使用递归配合过滤的解法。
核心算法就是：保留列表的第一个元素，然后把剩余列表中所有和它相等的元素全部删掉，再对剩下的列表递归做同样的事情。

### 分步实现解析：

处理基准情况 (Base Case)
    操作：如果列表为空 (null? lst)，直接返回空列表 '()。

提取并保留第一个元素：

    使用 (car lst) 获取第一个元素。
    根据题意“按第一次出现的顺序”，当前列表的第一个元素就是首次出现的元素，必须保留。

过滤剩余列表中的重复项：

    使用 (filter (lambda (x) (not (= x (car lst)))) (cdr lst))。

    (cdr lst) 是除去第一个元素后的剩余列表。
    lambda (x) 接收剩余列表中的每个元素 x。
    (= x (car lst)) 判断 x 是否与第一个元素相等。
    not 取反，意味着我们只保留不等于第一个元素的项。

    这一步将剩余列表中所有与第一个元素相同的值都剔除了。

```scheme
; filter基本语法
; (filter <predicate> <lst>)
; <predicate>（谓词函数）：一个接受单个参数并返回布尔值（#t 或 #f）的函数。通常你会用 lambda 来临时定义一个匿名函数。
; <lst>（列表）：你要进行筛选的原始列表。
; 返回值：一个新的列表，包含原列表中所有让 <predicate> 返回 #t 的元素。原列表不会被修改。
```

递归处理并拼接：

    对过滤后的列表调用 without-duplicates，并使用 cons 将第一个元素与递归结果连接起来。
    过滤后的列表可能还有其他的重复元素（例如 (4 4 2 2)），需要继续递归去重。最后将保留的元素拼接到结果前面。