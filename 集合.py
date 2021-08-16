# s={11,22,333}
# print(s,type(s))
# s1=set(([11,22,33,33]))
# print(s1,type(s1))
# s2=set(range(6))
# print(s2,type(s2))
# s3=set(((11,22,33)))
# print(s3,type(s3))

# s={11,22}
# s.add(33)
# s.update({222,333})
# s.update([66,77])
# print(s)
# s.remove(11)
# print(s)
# s.discard(1111)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)

# s1 = {11,22,33}
# s2={33,11,22}
# print(s1==s1)
# print(s1!=s2)

# s1={11,22,33,44}
# s2={11,22}
# s3={11,99}
# print(s2.issubset(s1))  #判断一个集合是否为另一个集合的子集
# print(s3.issubset(s1))
# print(s1.issuperset(s2))  #判断一个集合是否为另一个集合的超集
# print(s1.issuperset(s3))
# print(s3.isdisjoint(s1))  #false 有交集

# s1={11,22,33,44,55}
# s2={11,22,99}
# print(s1.intersection(s2))
# print(s1 & s2)
# print(s1.union(s2))
# print(s1 | s2)
# print(s1.difference(s2))
# print(s1-s2)
# print(s1.symmetric_difference(s2))
# print(s1^s2)

# s={ i for i in range(1,6)}
# print(s)