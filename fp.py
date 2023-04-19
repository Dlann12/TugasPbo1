# filter function untuk mengembalikan nilai genap
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# map function to mengalikan 2 angka
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# reduce function untuk menghitung jumlah seluruh elemen dalam list
from functools import reduce
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
