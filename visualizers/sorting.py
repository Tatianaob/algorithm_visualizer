import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

class SortingVisualizer:
    def __init__(self, arr):
        self.arr = arr

    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _print_array(self, highlight_indices=None):
        highlight_indices = highlight_indices or []
        for i, val in enumerate(self.arr):
            if i in highlight_indices:
                print(Fore.RED + f"{val}", end=" ")
            else:
                print(f"{val}", end=" ")
        print()
        time.sleep(0.3)
        self._clear()

    def bubble_sort(self):
        n = len(self.arr)
        self._clear()
        for i in range(n):
            for j in range(n - i - 1):
                self._print_array([j, j+1])
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        self._print_array()
