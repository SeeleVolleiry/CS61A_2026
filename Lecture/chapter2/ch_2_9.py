'''Recursive Objects
*** Objects can have other objects as attribute values.
    When an object of some class has an attribute value of that same class, it is a recursive object.
'''

'''Linked List Class
*** A linked list is composed of a first element and the rest of the list.
    The rest of a linked list is itself a linked list — a recursive definition.
***  A linked list is a sequence: it has a finite length and supports element selection by index.
'''
class Link:
    '''A linked list with a first element and the rest'''
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

s = Link(3, Link(4, Link(5)))

def link_expression(s):
    '''return a string that would evaluate to s'''
    if s.rest is Link.empty:
        rest = ''
    else:
        return 'Link((0), (1))'.format(s.first, s.rest)

link_expression(s) # 'Link(3, Link(4, Link(5)))'

# Recursive functions are particularly well-suited to manipulate linked lists.
def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)
join_link(s, ",") # '3, 4, 5'

# Recursive Construction: 递归构造。
def partitions(n, m):
    if n == 0:
        return 0
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m-1)
        return with_m + without_m

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))


'''Tree Class
*** A tree is any data structure that has as an attribute a sequence of branches that are also trees.
***
*** Defining trees that have internal values at the roots of each subtree.
    An internal value is called an label in the tree.
'''
class Tree:
    def __init__(self, label, branches=()) -> None:
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, self.branches)
        else:
            return 'Tree({0})'.format(self.label)
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.label + right.label, (left, right))

def sum_labels(t):
    '''Sum the labels of a tree t.'''
    return t.label + sum([sum_labels(b) for b in t.branches])


'''Sets/集合: a type of sequence. 一堆不重复的元素。
*** Abstractly, a set is a collection of distinct objects that supports membership testing, union, intersection, and adjunction.
***
*** In addition to the list, tuple, and dictionary, Python has a fourth built-in container type called a set.
    Duplicate elements are removed upon construction.
    Sets are unordered collections
***
*** Sets support a variety of operations:
    membership tests, length computation, and the standard set operations of union and intersection
    isdisjoint, issubset, issuperset
    add(), remove(), discard(), pop(), clear(), update()
***
*** Sets' three representations:集合的三种实现/表示
    ordered sequences, unordered sequences, binary search tree.
'''
s = {1, 3, 4, 3, 2, 4}
print(s)
print(3 in s) # True
len(s) # 4
s.union({1, 5}) # {1, 2, 3, 4, 5}
s.intersection({6, 5, 4, 3}) # {3, 4}

# One way to represent a set is as a sequence in which no element appears more than once.
def empty(s):
    return s is Link.empty

def set_contains(s, v):
    '''Return true if and only if set s contains v'''
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def adjoin_set(s, v):
    '''Return a set containing all elemetns of s and v'''
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect_set(set1, set2):
    '''Return a set containing all elements common to set1 and set2'''
    return keep_if_link(set1, lambda v: set_contains(set2, v))

def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = keep_if_link(set1, lambda v: not set_contains(set2, v))
    return extend_link(set1_not_set2, set2)

# Representing a set of numbers by listing its elements in increasing order.
def set_contains(s, v):
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def intersect_set(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect_set(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set(set1.rest, set2)
        elif e2 < e1:
            return intersect_set(set1, set2.rest)

# Sets as binary search trees.
def set_contains(s, v):
    if s in None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        set_contains(s.right, v)
    elif s.entry > v:
        set_contains(s.left, v)

def adjoin_set(s, v):
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Tree(s.entry, s.left, adjoin_set(s.right, v))
    elif s.entry > v:
        return Tree(s.entry, adjoin_set(s.left, v), s.right)