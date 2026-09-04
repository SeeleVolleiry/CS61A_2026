from __future__ import annotations # This makes the type annotations work


SOURCE_FILE = __file__


def flatten(s: list) -> list:
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    s_flattend = []
    for element in s:
        if type(element) != list:
            s_flattend = s_flattend + [element]
        else:
            s_flattend = s_flattend + flatten(element)
    return s_flattend


def close_list(s: list[int], k: int) -> list[int]:
    """Return a list of the elements of s that are within k of their index.
    That is, the absolute value of the difference between the element and its index 
    is less than or equal to k.
    
    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # Only 3 is equal to its index
    [3]
    >>> close_list(t, 1)  # 2, 3, and 5 are within 1 of their index
    [2, 3, 5]
    >>> close_list(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    [2, 4, 3, 5]
    """
    assert k >= 0
    return [s[i] for i in range(len(s)) if abs(s[i] - i) <= k]


def remove_first(lst: list, elem: int) -> list:
    """ This function removes the first appearance of elem in list lst.

    >>> remove_first([3, 4] , 3)
    [4]
    >>> remove_first([3, 4, 3] , 3)
    [4, 3]
    >>> remove_first([2, 4] , 3)
    [2, 4]
    >>> remove_first([] , 0)
    []
    """
    # base case
    if not lst:
        return []
    elif lst[0] == elem:
        return lst[1:]
    # recursive call
    else:
        return [lst[0]] + remove_first(lst[1:], elem)

def sort(lst: list) -> list:
    """This function returns a sorted version of the list lst.
    Hint: Use the remove_first function you just defined, and the built-in min function.

    >>> sort([6, 2, 5])
    [2, 5, 6]
    >>> sort([2, 3])
    [2, 3]
    >>> sort([3])
    [3]
    >>> sort([])
    []
    """
    lst_sort = []
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    else:
        curr_smallest = min(lst)
        lst_sort.append(curr_smallest)
        return lst_sort + sort(remove_first(lst, curr_smallest))
    

def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit: int) -> bool:
        if limit < 0:
            return False
        elif x == y:
            return True
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
    return can_reach


def make_func_repeater(f, x: int):
    """
    >>> increment_repeater = make_func_repeater(lambda x: x + 1, 1)
    >>> increment_repeater(2) #same as f(f(x))
    3
    >>> increment_repeater(5)
    6
    """
    def repeat(times: int):
        if times == 1:
            return f(x)
        else:
            return f(repeat(times -1))
    return repeat


import doctest

def ten_pairs(n: int) -> int:
    """Return the number of ten-pairs within positive integer n.
    Important: Use recursion; the tests will fail if you use any loops (for, while).

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6 
    6
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'ten_pairs', ['While', 'For'])
    True
    """
    last = n % 10
    if n < 10:
        return 0
    else:
        digit = 10 - last
        return count_digit(n // 10, digit) + ten_pairs(n // 10)

def count_digit(n: int, digit: int) -> int:
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_digits', ['While', 'For'])
    True
    """
    last = n % 10
    # base case
    if n == 0:
        return 0
    elif last == digit:
        return 1 + count_digit(n // 10, digit) # plus one

    # recursive calls
    else:
        return count_digit(n // 10, digit)


