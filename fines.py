def speed_fine (speed,limit):
    over = speed - limit
    if over <= 0:
        return ("OK")
    elif over <=10:
        return ("$50")
    elif over <=20:
        return ("$150")
    else:
        return ("$300")
    
if __name__ == "__main__":
    speed = float(input("Enter the speed of the car:").strip())
    limit = float(input("Enter the speed limit:").strip())
    print (speed_fine(speed,limit))