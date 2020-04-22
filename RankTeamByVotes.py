#Rank Team by Votes
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        t = list(votes[0])
        d = collections.defaultdict(lambda:[0]*n)
        for i in votes:
            for j in range(n):
                d[i[j]][j] += 1
        k = t.sort(key=lambda x: [-i for i in d[x]] + [x])
        return "".join(t)
