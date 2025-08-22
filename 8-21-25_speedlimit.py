speed = float(input("Enter the speed of the vehicle:").strip())
limit = float(input("Enter the posted speed limit:").strip())
def speed_fine (speed, limit):
    return speed - limit 
print (speed_fine)
