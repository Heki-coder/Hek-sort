class Sort:
    def small(self, numberes):
        size = []
        while not len(numberes) == 0:
            size.append(min(numberes))
            numberes.remove(min(numberes))
        return size
    def big(self, numbers):
        size = []
        while not len(numbers) == 0:
            size.append(max(numbers))
            numbers.remove((max(numbers)))
        return size