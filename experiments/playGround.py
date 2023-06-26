# import itertools
import math

device_indexes = [3, 2, 3]


class Sequencer:
    def __init__(self):
        self.dev_sizes = []
        self.change = []
        self.current = []

    def add_size(self, size: int) -> None:
        self.dev_sizes.append(size)

    def _calculate(self, index: int) -> list:
        result = []
        for a in self.dev_sizes:
            index, d = divmod(index, a)
            result.append(d)
        return result

    def _calc_change(self, index: int) -> None:
        previous = self._calculate(index - 1)
        for idx, a in enumerate(self.current):
            self.change.append(a != previous[idx])

    def get_finished(self, index: int) -> bool:
        return index == math.prod(self.dev_sizes)

    def get_index(self, index: int) -> list:
        if len(self.current) == 0:
            self.current = self._calculate(index)
            self._calc_change(index)
        return [self.current.pop(0), self.change.pop(0)]


indexer = Sequencer()
indexer.add_size(4)
indexer.add_size(2)
indexer.add_size(3)

for a in range(0, 24):
    for b in indexer.dev_sizes:
        print(indexer.get_index(a))
