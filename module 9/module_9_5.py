class StepValueError(ValueError):

    def __init__(self, message):
        self.message = message


class Iterator:

    def __init__(self, start, stop, step = 1):

        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):

        self.pointer += self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
            else:
                return self.pointer
        else:
            if self.pointer < self.stop:
                raise StopIteration()
            else:
                return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end = '')
except StepValueError as exc:
    print(f'Шаг указан неверно: {exc.message}')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, ' ', end = '')
print()

for i in iter3:
    print(i,' ', end = '')
print()

for i in iter4:
    print(i,' ', end = '')
print()

for i in iter5:
    print(i,' ', end = '')
print()



