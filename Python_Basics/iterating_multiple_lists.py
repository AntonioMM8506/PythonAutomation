l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

# zip() function takes two or more iterables and returns an iterator of tuples, 
# where the i-th tuple contains the i-th element from each of the input iterables. 
# The iteration stops when the shortest input iterable is exhausted.
for a, b in zip(l1, l2):
    print(a, b)