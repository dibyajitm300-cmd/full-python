#can we set with 18(int) and '18'(str) as a value in it ?
s=set()
s.add(18)
s.add("18")
s.add(18.0)
print(s)
print(len(s))
#18==18.0 -->> TRUE !(Value comparision in python)