# ab.py
A script to sort players into two teams in a multiplayer game.

Accepts a list of player tuples in the following format:

```
[(playerid, playerrating), (playerid, playerrating)]
````

The class: TeamBalance accepts the player list as an argument and provides two methods for balancing.
The first method is the "exact" method, also known as the exact change method. It finds the most even grouping of players assuming the rating supplied is a linear indication of skill.
The second method is the "spread" method. The spread method spreads the players by rating into two teams.

The output of the balance method is a list of two teams and the level of balance achieved.

The script also provides the generatemmr function to randomly generate a list of players for testing purposes.

Example:
```
python -i ab.py
>>> a = generatemmr()
>>> b = teambalance(a)
>>> b.balance()
[[(9, 4642), (5, 2223), (1, 2167), (4, 1450), (7, 25)], [(10, 3425), (2, 3388), (6, 2722), (8, 828), (3, 103)], 0.5009774471940114]
```