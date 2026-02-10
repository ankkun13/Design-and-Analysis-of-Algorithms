class Sorter():
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy

    def fit(self, arr):
        self.sort_strategy.fit(arr)

    def sort(self):
        return self.sort_strategy.sort()
    
    def num_comparisons_and_swaps(self):
        return self.sort_strategy.num_comparisons_and_swaps()