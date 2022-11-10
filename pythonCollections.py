
# NAMETUPLE
# from collections import namedtuple
# Nametuple is a method in collections allows to create a tuple with key and value
# a = namedtuple("courses", "name , technology")
# s = a("data_science", "python")
# You can make use of list to add value inside the nametuple
# s = a._make(["artificial inteligence", "python"])
# print(s)


# DEQUE
# from collections import deque
# with deque u can insert and delete from a list
# a = ["e","d","u","r","e","k","a"]

# s = deque(a)
# append is a method in deque that allows you to add value into a list
# s.append("python")
# appendleft is a method in deque that allows you to add value into a list from the begining
# s.appendleft("python")
# pop is a method in deque that allows you to remove value in a list
# s.pop()
# popleft is a method in deque that allows you to remove value in a list from the begining
# s.popleft()
# print(s)

# CHAINMAP

# from collections import ChainMap
# ChainMap is a dictionary like class for creating a single view of mutiple mappings

# a = {1:"edureka", 2: "python"}
# b = {3: "ml", 4:"ai"}

# al = ChainMap(a,b)
# print(al)

# Counter 
# from collections import Counter
# Counter is a dictionary subclass for counting hashable objects

# a = [1,2,2,3,4,3,5,4,56,6,67,2,5,6,3,5,1,4,6,3,2]
# c = Counter(a)
# print(c)

# print(list(c.elements()))

# print(c.most_common())

# sub = {2:1, 67:1}
# print(c.subtract(sub))
# print(c.most_common())

# OREREDDICTIONARY
# from collections import OrderedDict
# OrderedDict is dictionary subclass wish remebers the order in which the entries were done
# d = OrderedDict()
# d[1] = "e"
# d[2] = "d"
# d[3] = "u"
# d[4] = "r"
# d[5] = "e"
# d[6] = "k"
# d[7] = "a"

# print(d)

# print(d.keys())
# d[1] = "p"
# print(d)

# DEFAULTDICTIONARY
from collections import defaultdict
# defaultdict is dictionary subclass wish calls a factory function to supply missing values

d = defaultdict(int)

d[1] = "python"
d[2] = "edureka"

print(d)
print(d[3])