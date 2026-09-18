# Project: Ants

**完成Ants vs SomeBees**这一游戏所需要的类，植物大战僵尸 :)

# Phase 1：Basic gameplay

# Problem 0:

Answer a set of conceptual questions after you have read the entire ants.py

A note on unlocking tests: 
    
    If you'd like to review the unlocking questions after you have completed the unlocking test, you can navigate to the tests folder (within the ants folder).
    
    For example, after unlocking Problem 0, you can review the unlocking test at tests/00.py.

*python3 ok -q 00 -u*
```python
---------------------------------------------------------------------
Q: What is the significance of an Insect's health attribute? Does this
value change? If so, how?
Choose the number of the correct choice:
1) It represents the strength of an insect against attacks, which
   doesn't change throughout the game
2) It represents health protecting the insect, so the insect can only
   be damaged when its health reaches 0
3) It represents the amount of health the insect has left, so the
   insect is eliminated when it reaches 0
? 2
---------------------------------------------------------------------
Q: Which of the following is a class attribute of the Insect class?
Choose the number of the correct choice:
1) damage
2) health
3) bees
4) place
? 0
---------------------------------------------------------------------
Q: Is the health attribute of the Ant class an instance attribute or class attribute? Why?
Choose the number of the correct choice:
1) class, Ants of the same subclass all have the same amount of starting health
2) instance, each Ant instance needs its own health value
3) instance, each Ant starts out with a different amount of health
4) class, when one Ant gets damaged, all ants receive the same amount of damage
? 1
---------------------------------------------------------------------
Q: Is the damage attribute of an Ant subclass (such as ThrowerAnt) an
instance or class attribute? Why?
Choose the number of the correct choice:
1) class, all Ants deal the same damage
2) instance, the damage an Ant depends on where the Ant is
3) instance, each Ant does damage to bees at different rates
4) class, all Ants of the same subclass deal the same damage
? 3
---------------------------------------------------------------------
Q: Which class do both Ant and Bee inherit from?
Choose the number of the correct choice:
1) Ant
2) Insect
3) Place
4) Bee
? 1
---------------------------------------------------------------------
Q: What do instances of Ant and instances of Bee have in common? Please choosethe most correct answer.
Choose the number of the correct choice:
1) Ants and Bees both have the attribute damage and the methods
   reduce_health and action
2) Ants and Bees both take the same action each turn
3) Ants and Bees have nothing in common
4) Ants and Bees both have the attributes health, damage, and place
   and the methods reduce_health and action
? 3
---------------------------------------------------------------------
Q: How many insects can be in a single Place at any given time in the
game (before Problem 8)?
Choose the number of the correct choice:
1) There can be one Bee and many Ants in a single Place
2) There can be one Ant and many Bees in a single Place
3) Only one insect can be in a single Place at a time
4) There is no limit on the number of insects of any type in a single Place
? 1
---------------------------------------------------------------------
Q: What does a Bee do during one of its turns?
Choose the number of the correct choice:
1) The bee stings the ant in its place or moves to the next place if there is no ant in its place
2) The bee stings the ant in its place and then moves to the next place
3) The bee moves to the next place, then stings the ant in that place
4) The bee flies to the nearest Ant and attacks it
? 0
---------------------------------------------------------------------
Q: When is the game lost?
Choose the number of the correct choice:
1) When no ants are left on the map
2) When the colony runs out of food
3) When the bees enter the colony
4) When any bee reaches the end of the tunnel or when the Queen Ant is killed
5) When any bee reaches the end of the tunnel and the Queen Ant is killed
? 3
```

# Problem 1:

## Part A:

修改HarvesterAnt和ThrowerAnt的 Food Cost相关的属性

Override this class attribute for HarvesterAnt and ThrowerAnt according to the "Food Cost" column in the table below.

| Class	| Food Cost	| Initial Health|
| :---: |   :---:   |      :---:    |
| HarvesterAnt | 2	| 1|
|ThrowerAnt	| 3	| 1|

## Part B: implement the HarvesterAnt class

Now that placing an Ant costs food, we need to be able to gather more food!
To fix this issue, implement the HarvesterAnt class.

A HarvesterAnt is a type of Ant that increases gamestate.food by 1 as its action.

*python3 ok -q 01 -u*
```python
---------------------------------------------------------------------
Q: What is the purpose of the food_cost attribute?
Choose the number of the correct choice:
0) Each turn, each Ant in the colony eats food_cost food from the
   colony's total available food
1) Placing an ant into the colony will decrease the colony's total
   available food by that ant's food_cost
2) Each turn, each Ant in the colony adds food_cost food to the
   colony's total available food
? 1
---------------------------------------------------------------------
Q: What type of attribute is food_cost?
Choose the number of the correct choice:
0) instance, the food_cost of an Ant depends on the location it is placed
1) class, all Ants cost the same to place no matter what type of Ant it is
2) instance, the food_cost of an Ant is randomized upon initialization
3) class, all Ants of the same subclass cost the same to place
? 3
---------------------------------------------------------------------
>>> from ants import *
>>> from ants_plans import *
>>> Ant.food_cost
? 0

>>> HarvesterAnt.food_cost
? 2

>>> ThrowerAnt.food_cost
? 3
---------------------------------------------------------------------
>>> from ants import *
>>> from ants_plans import *
>>> # Testing HarvesterAnt action
>>> # Create a test layout where the colony is a single row with 9 tiles
>>> beehive = Hive(make_test_assault_plan())
>>> gamestate = GameState(beehive, ant_types(), dry_layout, (1, 9))
>>> #
>>> gamestate.food = 4
>>> harvester = HarvesterAnt()
>>> # Note: initializing an Ant doesn't cost food,
>>> # only deploying an Ant in the game layout does.
>>> # For this test case, Ants can still take actions
>>> # without being deployed in the game layout.
>>> #
>>> gamestate.food
? 4

>>> harvester.action(gamestate) # Executing harvester's action method. This symbolizes the ant taking one turn.
>>> gamestate.food
? 5

>>> harvester.action(gamestate) # Harvester's action is executed again.
>>> gamestate.food
? 6
```

# Problem 2: 位于Place类中

implement Plcae.\__init__ by adding code that tracks entrances. 

Place.\__init__ should use this logic:

    A newly created Place always starts with its entrance set to None.
    If the Place has an exit, then the exit's entrance is set to that Place.

Hint: 
    
    Remember that when the __init__ method is called, the first parameter, self, is bound to the newly created object.

    Try drawing out two Places next to each other if things get confusing.
    In the GUI, a place's entrance is to its right while the exit is to its left.

    Remember that Places are not stored in a list, so you can't index into anything to access them.
    This means that you can't do something like colony[index + 1] to access an adjacent Place.
    How can you move from one place to another?

**易错点**:

    一个palce的出口时exit，那么exit的入口就是该place。

    在Place class中完成problem 2时，应注意判断出口是否为None。创建一个Place实例时，传入的参数exit可以为None。
    对于None类型，其没有entrance属性。这会产生错误，使得测试不通过。

*python3 ok -q 02 -u*
```python
---------------------------------------------------------------------
Q: What does a Place represent in the game?
Choose the number of the correct choice:
0) Where the bees start out in the game
1) The entire space where the game takes place
2) The tunnel that bees travel through
3) A single tile that an Ant can be placed on and that connects to
   other Places
? 3
---------------------------------------------------------------------
Q: p is a Place whose entrance is q and exit is r (q and r are not None). Whenis p.entrance first set to a non-None value?
Choose the number of the correct choice:
0) When q is constructed
1) When p is constructed
2) Never, it is always set to None
? 0
---------------------------------------------------------------------
Q: p is a Place whose entrance is q and exit is r (q and r are not None). Whenis p.exit first set to a non-None value?
Choose the number of the correct choice:
0) Never, it is always set to None
1) When q is constructed
2) When p is constructed
? 2
---------------------------------------------------------------------
>>> from ants import *
>>> from ants_plans import *
>>> #
>>> # Create a test layout where the gamestate is a single row with 3 tiles
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 3)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Simple test for Place
>>> place0 = Place('place_0')
>>> print(place0.exit)
? None

>>> print(place0.entrance)
? None

>>> place1 = Place('place_1', place0)
>>> place1.exit is place0
? True

>>> place0.entrance is place1
? True 
```

# Problem 3: ThrowerAnt中的nearset_bee()

从投掷蚁所在格起，一格一格向前（沿 entrance）找"最近一格有蜜蜂、且不是 Hive"的地方，随机打那格的一只蜜蜂；一路打不到就返回 None。

Your job is to fix it so that a ThrowerAnt will throw_at the nearest Bee in front of it that is not still in the Hive. 
This includes Bees that are in the same Place as a ThrowerAnt

Hint: 

    All Places have an is_hive attribute, which is set to True when that place is the Hive and False otherwise.

Change nearest_bee so that it returns a random Bee from the nearest Place that contains Bees.

*Your implementation should follow this logic*:

    Start from the ThrowerAnt's current Place.
    If the Place contains one or more Bees, return a random one. Otherwise, check the next Place in front of it (stored as the current Place's entrance).
    Repeat this process until a Bee is found and returned. If no Bee is available to attack, return None.
    Ensure that Bees in the Hive are never returned by nearest_bee.

Hint:
    
    The random_bee function provided in ants.py returns a random Bee from a list of Bees or None if the list is empty.
    As a reminder, if there are no Bees present at a Place, then the bees attribute of that Place instance will be an empty list.
    Having trouble visualizing the test cases? Try drawing them out on paper! The sample diagram provided in Game Layout shows the first test case for this problem.

*python3 ok -q 03 -u*
```python
---------------------------------------------------------------------
Q: What Bee should a ThrowerAnt throw at?
Choose the number of the correct choice:
0) The ThrowerAnt finds the nearest place in either direction that has
   Bees and throws at a random Bee in that place
1) The ThrowerAnt finds the nearest place behind its own place
   that has Bees and throws at a random Bee in that place
2) The ThrowerAnt finds the nearest place including and in front of its
   own place that has Bees and throws at a random Bee in that place
3) The ThrowerAnt throws at a random Bee in its own Place
? 2
---------------------------------------------------------------------
Q: How do you get the Place object in front of another Place object?
Choose the number of the correct choice:
0) Increment the place by 1
1) Decrement the place by 1
2) The place's exit instance attribute
3) The place's entrance instance attribute
? 3
---------------------------------------------------------------------
Q: What is the entrance of the first Place in a tunnel (i.e. where do the beesenter from)?
Choose the number of the correct choice:
0) None
1) The Hive
2) An empty Place
? 1
---------------------------------------------------------------------
Q: How can you determine if a given Place is the Hive?
Choose the number of the correct choice:
0) by checking the ant attribute of the place instance
1) by checking the bees attribute of the place instance
2) by using the is_hive attribute of the place instance
? 2
---------------------------------------------------------------------
Q: What should nearest_bee return if there is no Bee in the tunnel in front ofthe ThrowerAnt?
Choose the number of the correct choice:
0) The closest Bee behind the ThrowerAnt
1) A random Bee in the Hive
2) None
? 2
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> thrower = ThrowerAnt()
>>> ant_place = gamestate.places["tunnel_0_0"]
>>> ant_place.add_insect(thrower)
>>> #
>>> # Testing nearest_bee
>>> near_bee = Bee(2) # A Bee with 2 health
>>> far_bee = Bee(3)  # A Bee with 3 health
>>> hive_bee = Bee(4) # A Bee with 4 health
>>> hive_place = gamestate.beehive
>>> hive_place.is_hive # Check if this place is the Hive
? True

>>> hive_place.add_insect(hive_bee)
>>> thrower.nearest_bee() is hive_bee # Bees in the Hive can never be attacked
? False

>>> near_place = gamestate.places['tunnel_0_3']
>>> far_place = gamestate.places['tunnel_0_6']
>>> near_place.is_hive # Check if this place is the Hive
? False

>>> near_place.add_insect(near_bee)
>>> far_place.add_insect(far_bee)
>>> nearest_bee = thrower.nearest_bee()
>>> thrower.place is ant_place    # Don't change self.place!
? True

>>> nearest_bee is far_bee
? False

>>> nearest_bee is near_bee
? True

>>> nearest_bee.health
? 2

>>> thrower.action(gamestate)    # Attack! ThrowerAnts do 1 damage
>>> near_bee.health
? 1

>>> far_bee.health
? 3

>>> thrower.place is ant_place    # Don't change self.place!
? True
```

# Phase 2：More Ants

After you implement each Ant subclass in these sections, you'll need to set its implemented class attribute to True.

# Problem 4:

**易错点**：

    1. 先判断是否为None，不为None才有is_hive属性，才能判断is_hive的真假。
    2. 范围判断不能放在循环入口。当下界不为零时，distance_away却等于0，直接不能进入循环。

In this problem, you'll implement two subclasses of ThrowerAnt that are less costly but have constraints on the distance they can throw:

    The LongThrower can only throw_at a Bee that is found after following at least 5 entrance transitions. In other words, it cannot hit Bees that are in the same Place as it or in the first 4 Places in front of it. If there are two Bees, one too close to the LongThrower and the other within its range, the LongThrower should only throw at the farther Bee, which is within its range, instead of trying to hit the closer Bee.
    
    The ShortThrower can only throw_at a Bee that is found after following at most 3 entrance transitions. In other words, it cannot throw at any Bees further than 3 Places in front of it.

    Neither of these specialized throwers can throw_at a Bee that is exactly 4 Places away.


|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|ShortThrower|	2|	1|
|LongThrower |	2|	1|

*python3 ok -q 04 -u*
```python
---------------------------------------------------------------------
Q: What class do ShortThrower and LongThrower inherit from?
Choose the number of the correct choice:
0) Bee
1) ThrowerAnt
2) ShortThrower
3) LongThrower
? 1
---------------------------------------------------------------------
Q: What constraint does a regular ThrowerAnt have on its throwing distance?
Choose the number of the correct choice:
0) A regular ThrowerAnt can only attack Bees at most 3 places away
1) A regular ThrowerAnt can only attack Bees at least 3 places away
2) There is no restriction on how far a regular ThrowerAnt can throw
3) A regular ThrowerAnt can only attack Bees at most 5 places away
? 2
---------------------------------------------------------------------
Q: What constraint does a LongThrower have on its throwing distance?
Choose the number of the correct choice:
0) A LongThrower can only attack Bees at least 3 places away
1) A LongThrower can only attack Bees at least 5 places away
2) There is no restriction on how far a LongThrower can throw
3) A LongThrower can only attack Bees at most 5 places away
? 1
---------------------------------------------------------------------
Q: What constraint does a ShortThrower have on its throwing distance?
Choose the number of the correct choice:
0) A ShortThrower can only attack Bees at least 3 places away
1) There is no restriction on how far a ShortThrower can throw
2) A ShortThrower can only attack Bees at most 3 places away
3) A ShortThrower can only attack Bees at most 5 places away
? 2
---------------------------------------------------------------------
Q: With the addition of these new ThrowerAnt subclasses, we must modify
our definition of nearest_bee. Now what Bee should ThrowerAnts throw
at?
Choose the number of the correct choice:
0) The closest random Bee in front of it within range
1) Any Bee in its current Place
2) Any Bee within range
3) The closest random Bee behind it within range
? 0
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing Long/ShortThrower parameters
>>> ShortThrower.food_cost
? 2

>>> LongThrower.food_cost
? 2

>>> short_t = ShortThrower()
>>> long_t = LongThrower()
>>> short_t.health
? 1

>>> long_t.health
? 1
```


# Problem 5: Implement FireAnt Class

Implement the FireAnt.
    
    If FireAnt is damaged by damage_taken health units, it does a damage of damage_taken to all Bees in its place (this is called reflected damage). 
    If it dies, it does an additional amount of damage, as specified by its damage attribute, to all the Bees in its place.
    The default value for the damage attribute in the FireAnt class is 3.

To implement this, override FireAnt's reduce_health method. 
Your overriden method should call the reduce_health method inherited from the superclass (Ant) which inherits from its superclass Insect to reduce the current FireAnt instance's health. 
Calling the inherited reduce_health method on a FireAnt instance reduces the insect's health by the given damage_taken and removes the insect from its place if its health reaches zero or lower.

your method needs to also include the reflective damage logic:

    Determine the reflective damage amount: start with the damage_taken inflicted on the FireAnt, and then add damage if the ant's health has dropped to or below 0.
    
    For each Bee in the place, damage them with the total reflective damage amount by calling its appropriate reduce_health method.
    
    Remember that when any Ant loses all its health, it is removed from its Place, so pay careful attention to the order of your logic in reduce_health.

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|FireAnt| 5 | 3 |

*python3 ok -q 05 -u*:易错点就在回答中
```python
---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 16)

Q: How can you obtain the current place of a FireAnt?
Choose the number of the correct choice:
0) By calling the Place constructor, passing in the FireAnt instance
1) By calling the FireAnt constructor
2) By accessing the place instance attribute, which is the name of
   some Place object
3) By accessing the place instance attribute, which is a Place object
? 3


---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 2
(cases remaining: 15)

Q: How can you obtain all of the Bees currently in a given place?
Choose the number of the correct choice:
0) By calling the add_insect method on the place instance
1) By accessing the bees instance attribute, which is a dictionary of
   Bee objects
2) By calling the Bee constructor, passing in the place instance
3) By accessing the bees instance attribute, which is a list of Bee
   objects
? 3


---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 3
(cases remaining: 14)

Q: Can you iterate over a list while mutating it?
Choose the number of the correct choice:
0) No, Python doesn't allow list mutation on a list that is being
   iterated through
1) Yes, you can mutate a list while iterating over it with no problems
2) Yes, but you should iterate over a copy of the list to avoid skipping
   elements
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) No, Python doesn't allow list mutation on a list that is being
   iterated through
1) Yes, you can mutate a list while iterating over it with no problems
2) Yes, but you should iterate over a copy of the list to avoid skipping
   elements
? 2


---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 1
(cases remaining: 13)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing FireAnt parameters
>>> fire = FireAnt()
>>> FireAnt.food_cost
? 5


>>> fire.health
? 3


---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 2
(cases remaining: 12)

-- Already unlocked --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 3
(cases remaining: 11)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing fire does damage to all Bees in its Place
>>> place = gamestate.places['tunnel_0_4']
>>> fire = FireAnt(health=1)
>>> place.add_insect(fire)        # Add a FireAnt with 1 health
>>> place.add_insect(Bee(3))      # Add a Bee with 3 health
>>> place.add_insect(Bee(5))      # Add a Bee with 5 health
>>> len(place.bees)               # How many bees are there?
? 2


>>> place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
>>> fire.health
? 0


>>> fire.place is None
? True


>>> len(place.bees)               # How many bees are left?
? 2
-- Not quite. Try again! --

? 1


>>> place.bees[0].health           # What is the health of the remaining Bee?
? 0
-- Not quite. Try again! --

? -1
-- Not quite. Try again! --

? 1


---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 4
(cases remaining: 10)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> place = gamestate.places['tunnel_0_4']
>>> ant = FireAnt(health=1)           # Create a FireAnt with 1 health
>>> place.add_insect(ant)      # Add a FireAnt to place
>>> ant.place is place
? True 


>>> place.remove_insect(ant)   # Remove FireAnt from place
>>> ant.place is place         # Is the ant's place still that place?
? False

```

# Problem 6: WallAnt

Unlike with previous ants, we have not provided you with a class statement.
Implement the WallAnt class from scratch:
    Give it a class attribute name with the value 'Wall'
    Give it a class attribute implemented with the value True.

Hint: 
    Make sure you implement the \__init__ method too so the WallAnt starts off with the appropriate amount of health!

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|WallAnt| 4 | 4 |


*python3 ok -q 06 -u*:从中可以理解WallAnt class的属性、方法
```python
---------------------------------------------------------------------
Q: What class does WallAnt inherit from?
Choose the number of the correct choice:
0) HungryAnt
1) The WallAnt class does not inherit from any class
2) Ant
3) ThrowerAnt
? 2
---------------------------------------------------------------------
Q: What is a WallAnt's action?
Choose the number of the correct choice:
0) A WallAnt increases its own health by 1 each turn
1) A WallAnt attacks all the Bees in its place each turn
2) A WallAnt takes no action each turn
3) A WallAnt reduces its own health by 1 each turn
? 2
---------------------------------------------------------------------
Q: Where do Ant subclasses inherit the action method from?
Choose the number of the correct choice:
0) Ant subclasses inherit the action method from the Ant class
1) Ant subclasses do not inherit the action method from any class
2) Ant subclasses inherit the action method from the Insect class
? 2
---------------------------------------------------------------------
Q: If a subclass of Ant does not override the action method, what is the
default action?
Choose the number of the correct choice:
0) Move to the next place
1) Nothing
2) Throw a leaf at the nearest Bee
3) Reduce the health of all Bees in its place
? 1
```

# Problem 7: HungryAnt

大嘴花/食人花的机制。

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|HungryAnt| 4 | 1 |

*python3 ok -q 07 -u*：
```python
---------------------------------------------------------------------
Q: Should cooldown be an instance or class attribute? Why?
Choose the number of the correct choice:
0) instance, all HungryAnt instances in the game chew simultaneously
1) class, each HungryAnt instance chews independently of other
   HungryAnt instances
2) class, all HungryAnt instances in the game chew simultaneously
3) instance, each HungryAnt instance chews independently of other
   HungryAnt instances
? 3
---------------------------------------------------------------------
Q: When is a HungryAnt able to eat a Bee?
Choose the number of the correct choice:
0) Whenever a Bee is in its place
1) When it is chewing, i.e. when its cooldown attribute is at least 1
2) Each turn
3) When it is not chewing, i.e. when its cooldown attribute is 0
? 3
---------------------------------------------------------------------
Q: When a HungryAnt is able to eat, which Bee does it eat?
Choose the number of the correct choice:
0) The closest Bee in either direction
1) The closest Bee in front of it
2) The closest Bee behind it
3) A random Bee in the same place as itself
? 3
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing HungryAnt parameters
>>> hungry = HungryAnt()
>>> HungryAnt.food_cost
? 4

>>> hungry.health
? 1

>>> hungry.chew_cooldown
? 3

>>> hungry.cooldown
? 0
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing HungryAnt eats and chews
>>> hungry = HungryAnt()
>>> super_bee, wimpy_bee = Bee(1000), Bee(1)
>>> place = gamestate.places["tunnel_0_0"]
>>> place.add_insect(hungry)
>>> place.add_insect(super_bee)
>>> hungry.action(gamestate)         # super_bee is no match for HungryAnt!
>>> super_bee.health
? 0   


>>> place.add_insect(wimpy_bee)
>>> for _ in range(3):
...     hungry.action(gamestate)     # chewing...not eating
>>> wimpy_bee.health
? 1

>>> hungry.action(gamestate)         # back to eating!
>>> wimpy_bee.health
? 0
```

# Problem 8: ProtectorAnt

To more easily implement the ProtectorAnt, we will break up this problem into 3 subparts. In each part, we will making changes in either the ContainerAnt class, Ant class, or ProtectorAnt class.

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|ProtectorAnt| 4 | 2 |

## Problem 8a：ContainerAnt

We will define and work in a *ContainerAnt* parent class that we will later use for our ProtectorAnt.

   instance attribute：ant_contained， storing the ant it contains. This ant, ant_contained, initially starts off as None to indicate that there is no ant being stored yet. 

   store_ant method: it sets the ContainerAnt's ant_contained instance attribute to the ant argument passed in.

   action method: This method will ensure that if our ContainerAnt currently contains an ant, ant_contained's action is performed.

*python3 ok -q 08a -u*
```python
---------------------------------------------------------------------
Q: Where is the ant contained by a ContainerAnt stored?
Choose the number of the correct choice:
0) In the ContainerAnt's ant_contained class attribute
1) In the ContainerAnt's ant_contained instance attribute
2) Nowhere, a ContainerAnt has no knowledge of the ant that it's protecting
3) In its place's ant instance attribute
? 1
-- OK! --
---------------------------------------------------------------------
Q: How does a ContainerAnt guard its ant?
Choose the number of the correct choice:
0) By allowing Bees to pass without attacking
1) By increasing the ant's health
2) By attacking Bees that try to attack it
3) By protecting the ant from Bees and allowing it to perform its original action
? 3
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
>>> #
>>> container = ContainerAnt(1)
>>> container2 = ContainerAnt(2)
>>> container3 = ContainerAnt(3)
>>> throw_long = LongThrower(1)
>>> container.can_contain(container2)
? False
-- OK! --

>>> container3.can_contain(throw_long)
? True
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
>>> #
>>> container = ContainerAnt(2)
>>> friend = HungryAnt()
>>> container.ant_contained is None
? True
-- OK! --

>>> container.store_ant(friend)
>>> container.ant_contained is friend
? True
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
>>> #
>>> container = ContainerAnt(2)
>>> container.ant_contained is not None
? False
-- OK! --

>>> friend = HungryAnt()
>>> container.store_ant(friend)
>>> container.ant_contained is friend
? True
-- OK! --

>>> place = gamestate.places["tunnel_0_0"]
>>> place.add_insect(container)
>>> friend.place = place
>>> bee = Bee(3)
>>> place.add_insect(bee)
>>> container.action(gamestate)  # Container holds a HungryAnt that loves to eat!
>>> bee.health
? 0
-- OK! --

>>> container.can_contain(FireAnt()) # Container already holds another ant!
? False
-- OK! --
```

## Problem 8b：Modify Ant.add_to()

Modify Ant.add_to to allow a container and its contained ant to occupy the same place according to the following rules:

   If the Ant originally occupying a place can_contain the Ant being added, then both Ants occupy the place and the original Ant contains the Ant being added.
   
   If the Ant being added can_contain the Ant originally in the space, then both Ants occupy the place and the Ant being added contains the original Ant.
   
   If neither Ant can_contain the other, raise the same AssertionError as before (the one already present in the starter code).

Important:
   
   If there are two Ants in a specific Place, the ant attribute of the Place instance should refer to the container ant, and the container ant should contain the non-container ant.

Hint: 
   
   You should also take advantage of the can_contain method you wrote and avoid repeating code.

Note:
   
   If you're getting an "unreachable code" warning for Ant.add_to via the VSCode Pylance extension, it's fine to ignore this specific warning as the code is actually run (the warning in this case is inaccurate).

*python3 ok -q 08b -u*:
```python
---------------------------------------------------------------------
Q: When can a second Ant be added to a place that already contains an Ant?
Choose the number of the correct choice:
0) When exactly one of the Ant instances is a container and the
   container ant does not already contain another ant
1) When exactly one of the Ant instances is a container
2) There can never be two Ant instances in the same place
3) When both Ant instances are containers
? 0
-- OK! --
---------------------------------------------------------------------
Q: If two Ants occupy the same Place, what is stored in that place's ant
instance attribute?
Choose the number of the correct choice:
0) A list containing both Ants
1) The Ant being contained
2) Whichever Ant was placed there first
3) The Container Ant
? 3
-- OK! --
---------------------------------------------------------------------
Problem 8b > Suite 1 > Case 3
(cases remaining: 5)

Q: Which Ant does a ContainerAnt guard?
Choose the number of the correct choice:
0) The Ant instance in the place closest to its own place
1) The Ant instance that is in the same place as itself
2) A random Ant instance in the gamestate
3) All the Ant instances in the gamestate
? 1
-- OK! --
```

## Problem 8c：

Finally, we can work on implementing our ProtectorAnt class.

   Add a ProtectorAnt.\__init__ that sets the initial amount of health for the ProtectorAnt.
   
   We do not need to create an action method here since the ProtectorAnt class inherits it from the ContainerAnt class.
   
   Also note that the ProtectorAnt does not do any damage.

   Once you've finished implementing the ProtectorAnt, give it a class attribute implemented with the value True.

*python3 ok -q 08c -u*
```python
---------------------------------------------------------------------
Q: Where does a ProtectorAnt directly inherit all of its instance attributes from?
Choose the number of the correct choice:
0) Ant class
1) ContainerAnt class
2) Insect class
3) the ProtectorAnt does not inherit from any other class
? 1
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> # Testing ProtectorAnt parameters
>>> protector = ProtectorAnt()
>>> ProtectorAnt.food_cost
? 4
-- OK! --

>>> protector.health
? 2
-- OK! --
```

# Problem 9: TankAnt

The TankAnt is a ContainerAnt that protects an ant in its place and also deals 1 damage to all Bees in its Place each turn.
Like any ContainerAnt, a TankAnt allows the ant that it contains to perform its action each turn.

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|TankAnt| 6 | 2 |

*python3 ok -q 09 -u*
```python
nothing worth recording.
```

# Phase 3: Water and Might

In the final phase, you're going to add one last kick to the game by introducing a new type of place and new ants that are able to occupy this place.
One of these ants is the most important ant of them all: the queen of the colony!

# Problem 10: Water.add_insect()

We're going to create a new type of Place called Water.

Implement the add_insect method for Water.
   
   First, add the Insect to the Place regardless of whether it is waterproof.
   Then, if the Insect is not waterproof, reduce the Insect's health to 0.
   Do not repeat code from elsewhere in the program. Instead, use methods that have already been defined.

*python3 ok -q 10 -u*
```python
---------------------------------------------------------------------
>>> from ants import *
>>> from ants_plans import *
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing water with soggy (non-waterproof) bees
>>> test_bee = Bee(1000000)
>>> test_bee.is_waterproof = False    # Make Bee non-waterproof
>>> test_water = Water('Water Test2')
>>> test_water.add_insect(test_bee)
>>> test_bee.health
? 0
-- OK! --

>>> len(test_water.bees)
? 0
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> from ants_plans import *
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing water with waterproof bees
>>> test_bee = Bee(1)
>>> test_water = Water('Water Test3')
>>> test_water.add_insect(test_bee)
>>> test_bee.health
? 1
-- OK! --

>>> test_bee in test_water.bees
? True
-- OK! --
```

# Problem 11: ScubaThrower

Implement the ScubaThrower, which is a subclass of ThrowerAnt that is more costly and waterproof, but otherwise identical to its base class.
A ScubaThrower should not lose its health when placed in Water.

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|ScubaThrower| 6 | 1 |

*python3 ok -q 11 -u*
```python
---------------------------------------------------------------------
Q: How is a ScubaThrower different from a regular ThrowerAnt?
Choose the number of the correct choice:
0) It is not waterproof, so its health will be reduced to 0 when it is
   placed in a Water Place
1) It throws water pellets instead of leaves
2) It is waterproof, so its health won't be reduced to 0 when it is
   placed in a Water Place
? 2
-- OK! --
---------------------------------------------------------------------
Q: Which inherited attributes and/or methods should ScubaThrower
override?
Choose the number of the correct choice:
0) food_cost, action, damage
1) name, nearest_bee, is_waterproof
2) name, is_waterproof, food_cost
3) is_waterproof, action
? 2
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> # Testing ScubaThrower parameters
>>> scuba = ScubaThrower()
>>> ScubaThrower.food_cost
? 6
-- OK! --

>>> scuba.health
? 1
-- OK! --

>>> scuba.name
? 'Scuba'
-- OK! --

>>> scuba.is_waterproof
? True
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), wet_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing if ScubaThrower is waterproof
>>> water = gamestate.places["water_0_2"]
>>> ant = ScubaThrower()
>>> water.add_insect(ant)
>>> ant.place is water
? True
-- OK! --

>>> ant.health
? 1
-- OK! --
---------------------------------------------------------------------
>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), wet_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing that ThrowerAnt is not waterproof
>>> water = gamestate.places["water_0_2"]
>>> ant = ThrowerAnt()
>>> ant.is_waterproof
? False
-- OK! --

>>> water.add_insect(ant)
>>> ant.place is water
? False
-- OK! --

>>> ant.health
? 0
-- OK! --
```

# Problem 12: QueenAnt

A queen is a ThrowerAnt that inspires her fellow ants through her bravery.
In addition to the standard ThrowerAnt action, a QueenAnt doubles the damage of all the ants behind her in her tunnel each time she performs an action.
However, once an ant's damage has been doubled, it cannot be doubled again. Try to think of a way to keep track of whether an ant's damage has already been doubled (Hint: Use an instance attribute!)

Note: The reflected damage of a FireAnt should not be doubled, only the extra damage it deals when its health is reduced to 0.

However, with great power comes great responsibility.
If a QueenAnt ever has its health reduced to 0, the ants lose.
You will need to override Insect.reduce_health in QueenAnt and call ants_lose() in that case in order to signal to the simulator that the game is over. (The ants also still lose if any bee reaches the end of a tunnel.)

Hint: 

   For doubling the damage of all ants behind her, you may fill out the double method defined in the Ant class, then call it from the QueenAnt class.

   When doubling the ants' damage, keep in mind that there can be more than one ant in a Place, like in the case of container ants storing another.

   Remember that QueenAnt's reduce_health method adds the additional task of calling ants_lose() to the superclass's reduce_health method. How can we make sure we still do everything from the superclass's method without repeating code?

   You can find each Place in a tunnel behind a QueenAnt by starting at the queen's place.exit and then repeatedly moving back to the previous Place's exit. The exit of a Place at the end of a tunnel is None.

|Class|Food Cost|Initial Health|
|:---:|:---:|:---:|
|QueenAnt| 7 | 1 |

*python3 ok -q 12 -u*
```python

```