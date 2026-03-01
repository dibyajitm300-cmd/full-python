# celcius to farehnite
# c/2 = (f-32)/9
def cel2far(c):
    f=((9*c)/2)+32
    return f
cel = int(input("ENTER THE VALUE OF CELCIUS: "))
value= cel2far(cel)
print(value)
