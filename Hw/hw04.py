from __future__ import annotations


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product: str, price: int):
        """Set the product and its price, as well as other instance attributes."""
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    def restock(self, n: int) -> str:
        """Add n to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        """
        self.stock += n
        curr_stock = f'Current {self.product} stock: {self.stock}'
        return curr_stock

    def add_funds(self, n: int) -> str:
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Nothing left to vend. Please restock. Here is your $4.

        Otherwise, add n to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        """
        if self.stock == 0:
            return f'Nothing left to vend. Please restock. Here is your ${n}.'
        else:
            self.balance += n
            curr_funds = f'Current balance: ${self.balance}'
            return curr_funds

    def vend(self) -> str:
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Nothing left to vend. Please restock.
              Please add $3 more funds.
        """
        # 能卖出的情况
        if self.stock > 0 and self.balance >= self.price:
            change = self.balance - self.price
            self.stock -= 1
            self.balance = 0
            if change == 0:
                return f'Here is your {self.product}.'
            else:
                return f'Here is your {self.product} and ${change} change.'
        # 库存为零的情况
        elif self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        # 有库存但不能找钱/余额不足的情况
        else:
            add = self.price - self.balance
            return f'Please add ${add} more funds.'


def cumulative_mul(t: Tree) -> None:
    """Mutates t so that each node's label becomes the product of its own
    label and all labels in the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    >>> otherTree = Tree(2, [Tree(1, [Tree(3), Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> cumulative_mul(otherTree)
    >>> otherTree
    Tree(5040, [Tree(60, [Tree(3), Tree(4), Tree(5)]), Tree(42, [Tree(7)])])
    """
    # 递归函数的作用是修改参数t的根节点的值。
    # 递推关系：cumulative_mul(t) = 每个子树b cumulative_mul后的根节点的累计的积 * 根节点值
    if t.is_leaf():
        return
    t_root_product = 1
    for b in t.branches:
        cumulative_mul(b) # 先cumulative_mul(b)把子树改好，然后读b.label。因为子树已经被就地改完，此刻 b.label 恰好就等于"该子树的全部乘积"。
        t_root_product *= b.label
    t.label = t_root_product * t.label


def prune_small(t: Tree, n: int) -> None:
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest labels.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while len(t.branches) > n:
        largest = max(t.branches, key=lambda x: x.label)
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b, n)


class Pet:

    def __init__(self, name: str, owner: str) -> None:
        self.name = name
        self.owner = owner

    def talk(self) -> None:
        print(self.name)

class Cat(Pet):
    """
    >>> my_cat = Cat("Furball", "Me", lives=2)
    >>> my_cat.talk()
    Meow!
    >>> my_cat.name
    'Furball'
    >>> my_cat.lose_life()
    >>> my_cat.is_alive
    True
    >>> my_cat.eat("poison")
    Meow!
    Furball ate a poison!
    >>> my_cat.is_alive
    False
    >>> my_cat.lose_life()
    'Cat is dead x_x'
    """
    def __init__(self, name: str, owner: str, lives: int = 9) -> None:
        assert type(lives) == int and  lives > 0
        self.name = name
        self.owner = owner
        self.lives = lives
        self.is_alive = True

    def talk(self) -> None:
        """A cat says 'Meow!' when asked to talk."""
        say = 'Meow!'
        print(say)

    def lose_life(self) -> str | None:
        """A cat can only lose a life if it has at least one
        life. When there are zero lives left, the 'is_alive'
        variable becomes False.
        """
        if self.lives >= 1:
            self.lives -= 1
        if self.lives == 0:
            self.is_alive = False
        if not self.is_alive:
            death = 'Cat is dead x_x'
            return death

    def eat(self, thing: str) -> None:
        self.talk()
        print(f"{self.name} ate a {thing}!")
        if thing == "poison":
            self.is_alive = False


class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

