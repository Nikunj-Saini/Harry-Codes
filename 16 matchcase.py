x = int(input("Enter the value of x "))
match x :
    case 0:
        print(" there is nothing")
    case 1:
        print("k dekhe se ")
    case 7:
        print("please enter a valid number")
        # for default down
    # case _ :
    #     print("op bro ")
    case _ if x!=90:
        print("you are wrong ")
