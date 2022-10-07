import statistics
class Stat:
    def __init__(self,statlist:list):
        self.statlist = statlist
    
    def list_sum(self) -> float:
        return sum(self.statlist)
    
    def mean(self) -> float:
        return self.list_sum()/len(self.statlist)
        
    def median(self) -> float:
        return statistics.median(self.statlist)
    
    def min(self) -> float:
        return min(self.statlist)
    
    def max(self) -> float:
        return max(self.statlist)

stat1 = Stat([1,2,3,4,5])
print(stat1.list_sum())
print(stat1.mean())
print(stat1.median())
print(stat1.min())
print(stat1.max())