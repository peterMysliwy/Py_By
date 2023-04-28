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
        self.change = [(a != previous[idx]) for idx, a in enumerate(self.current)]

    def debug(self, index: int):
        self.current = self._calculate(index)
        self._calc_change(index)
        return [self.current, self.change]

    def get_sizes(self):
        return math.prod(self.dev_sizes)

    def get_finished(self, index: int):
        return index == self.get_sizes()

    def get_index(self, index: int) -> list:
        if len(self.current) == 0:
            self.current = self._calculate(index)
            self._calc_change(index)
        return [self.current.pop(0), self.change.pop(0)]


if __name__ == '__main__':
    indexer = Sequencer()
    indexer.add_size(4)
    indexer.add_size(2)
    indexer.add_size(3)

    for a in range(0, indexer.get_sizes()):
        # for b in indexer.dev_sizes:
        print(a, indexer.debug(a))
