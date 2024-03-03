l = [5, 7, 22, 97, 54, 62, 577, 623, 973, 661]
# l =[str(i)[::-1] for i in l].sort()
# print (l.sort(key=lambda x:x%10,reverse=False))
# print (list(map(lambda x:x%10,l)).sort())
print([i for i in l if i == i % 10].sort())
