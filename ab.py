import random
import itertools
import string

def generatemmr(num=10):
    a = []
    for x in range(0, num):
        a.append((x+1, random.randrange(0, 5000)))
    return(a)

class TeamBalance():
    def __init__(self, players):
        self.players = players;

    def balance(self, exact=True):
        ratings = [x[1] for x in self.players]
        num = int(len(self.players)/2)
        if exact:
            teamavg = sum(ratings)/2
            combinations = itertools.combinations(self.players, num)
            resultlist = []
            for c in combinations:
                resultlist.append([sum([x[1] for x in c]), c])
            closest = min(resultlist, key=lambda x:abs(x[0]-teamavg))
            bp = sum([x[1] for x in closest[1]])/sum(ratings)
            teams = [[],[],bp]
            for mmr in self.players:
                if mmr in closest[1]:
                    teams[0].append(mmr)
                else:
                    teams[1].append(mmr)
            teams[0].sort(reverse=True, key = lambda x: x[1])
            teams[1].sort(reverse=True, key = lambda x: x[1])
            return teams
        else:
            self.players = sorted(self.players, reverse=True, key = lambda x: x[1])
            teama = self.players[::2]
            bp = sum([x[1] for x in teama])/sum(ratings)
            teams = [self.players[::2], self.players[1::2], bp]
            return teams
