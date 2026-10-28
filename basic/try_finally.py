def main():
    try:
        a=int(input("Enter a number:"))
        print(a)

    except Exception as e:
        print(e)

    finally:
       print("hey i am inside the finally")
    
main()

#finally only use in some function.
    




