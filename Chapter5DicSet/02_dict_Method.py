marks={
    "Dibya":100,
    "Shubham":98,
    "Rohan":99
}
print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Dibya":1000,"Madhu":456})
# print(marks)
print(marks.get("Dibya"))
print(marks.get("jgf"))#KEY NOT FOUND->NONE
print(marks.get("hsdgvf"))#prints none
print(marks["dfgg"])#print ERROR
#explore by using chatgpt Ai tool