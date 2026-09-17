# Project: Ants

**完成Ants vs SomeBees**这一游戏所需要的类，植物大战僵尸 :)

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


*python3 ok -q 02 -u*
```python

```

# Problem 3:



# Problem 4:



# Problem 5:



# Problem 6:



# Problem 7:



# Problem 8:



# Problem 9:



# Problem 10:



# Problem 11:



# Problem 12: