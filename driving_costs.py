'''
2.14 LAB: Driving costs
Driving is expensive. Write a program with a car's gas milage (miles/gallon)
and the cost of gas (dollars/gallon) as floating-point input,
and output the gas cost for 20 miles, 75 miles, and 500 miles.

INPUT
    mpgForMyCar
    costPerGallon
    tripMiles
OUTPUT
    driveCost
'''

def main():

    mpg = 0.0
    costPerGal = 0.0
    tripMiles = 0.0
    driveCost = 0.0



    print("Gas Calculator")
    mpg = getFloat("Enter car's miles per gallon: ")
    costPerGal = getFloat("Enter the cost of gas: ")
    tripMiles = getFloat("Enter distance of trip (in miles): ")

    #Display output
    displayOutput(mpg, costPerGal, tripMiles, driveCost)

    driveCost = (tripMiles / mpg) * costPerGal


#-----------

# getFloat function and its parameters
# use a loop control variable to make sure user enters in correct value

def displayOutput(mpg, costPerGal, tripMiles, driveCost):
    print("Car MPG: {0:,.2f}".format(mpg))
    print("Cost per gallon: {0:,.2f}".format(costPerGal))
    print("Driving distance: {0:,.2f}".format(tripMiles))
    print("Cost of the trip: {0:,.2f}".format(driveCost))


def getFloat(message):
    result = 0.0
    badValue = True
    while(badValue):
        try:
            result = float(input(message))
            badValue = False
        except:
            print("Number type entered must be a float.")
            badValue = True
    return result

main()