def main():
    try:
        a=int (input("HEY !Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    

    finally:
        print("HEY still im running inside finally")

main()        