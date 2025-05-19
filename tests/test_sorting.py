# tests/test_sorting.py

from visualizers.sorting import SortingVisualizer

def test_bubble_sort():
    arr = [4, 2, 5, 1, 3]
    vis = SortingVisualizer(arr)
    vis.bubble_sort()
    assert vis.arr == [1, 2, 3, 4, 5]
