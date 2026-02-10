from abc import abstractmethod

class SortAbstract:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.arr = []

    def fit(self, arr):
        self.arr = arr

    def get_array(self):
        return self.arr

    @abstractmethod
    def sort(self):
        pass

    def num_comparisons_and_swaps(self):
        return (self.comparisons, self.swaps)