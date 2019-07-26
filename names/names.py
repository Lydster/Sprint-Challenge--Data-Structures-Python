import time


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

f = open('names_2.txt', 'r')
names_2 = BinarySearchTree('name')
for row in f:
    name = str.strip(row)
    names_2.insert(name)
f.close()

duplicates = []
for name_1 in names_1:
    if names_2.contains(name_1):
        duplicates.append(name_1)


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# third or fourth solution I tried. I was getting results, but not the correct names. Would like to discuss with TL.
# duplicates = []

# name_dup = BinarySearchTree('name')

# for i in names_1:
#     name_dup.insert(i)

# for j in names_2:
#     if name_dup.contains(j):
#         duplicates.append(j)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
