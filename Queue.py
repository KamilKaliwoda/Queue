from typing import List


class Queue:
    def __init__(self):
        self.size = 5
        self.save = 0
        self.read = 0
        self.tab = [None for i in range(self.size)]

    def realloc(self, size: int) -> List:
        old_size = self.size
        self.size = size
        new_tab = [self.tab[i - old_size] if i - old_size >= self.read else None for i in range(self.size)]
        for i in range(self.save):
            new_tab[i] = self.tab[i]
        self.read += old_size
        return new_tab

    def is_empty(self) -> bool:
        if self.save == self.read:
            return True
        else:
            return False

    def peek(self) -> [int, float, str]:
        if self.is_empty():
            raise ValueError("List is empty.")
        else:
            return self.tab[self.read]

    def enqueue(self, data: [int, float, str]) -> None:
        self.tab[self.save] = data
        if self.save == self.size - 1:
            self.save = 0
        else:
            self.save += 1
        if self.save == self.read:
            new_size = self.size * 2
            self.tab = self.realloc(new_size)
            self.size = new_size

    def dequeue(self) -> [int, float, str]:
        if self.is_empty():
            return None
        else:
            data = self.tab[self.read]
            self.tab[self.read] = None
            if self.read == self.size - 1:
                self.read = 0
            else:
                self.read += 1
            return data

    def disp_tab(self) -> None:
        print("Full array: ", self.tab)

    def disp_queue(self) -> None:
        string = "["
        if self.read > self.save:
            read = self.read
            while read < self.size:
                if read - self.size - 1 == self.save:
                    string += str(self.tab[read]) + "]"
                else:
                    string += str(self.tab[read]) + ", "
                read += 1
            if self.save:
                for s in range(self.save):
                    if s == self.save - 1:
                        string += str(self.tab[s]) + ']'
                    else:
                        string += str(self.tab[s]) + ", "
            print("Actual queue: ", string)
        elif self.read < self.save:
            for i in range(self.read, self.save):
                if i == self.save - 1:
                    string += str(self.tab[i]) + "]"
                else:
                    string += str(self.tab[i]) + ", "
            print("Actual queue: ", string)
        else:
            print("Queue is empty.")




