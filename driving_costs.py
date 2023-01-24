"""
Tyler Sotomayor
Dennis Hunchuck

            Completed in Partial Fulfillment of the Requirements of
            COP 2930 | Select Topics in Computer Programming - Python

24 January 2023

§2.14 LAB: Driving costs
Driving is expensive. Write a program with a car's gas mileage (miles per gallon)
and the cost of gas (dollars per gallon) and trip distance (miles) as floating-point input,
and output the gas cost. [Adapted from zyBooks]
"""


def main():

    greeting = "Driving Cost Calculator\n-----------------------------------"
    print(greeting)
    miles_per_gallon = get_float("Enter the car's fuel economy (MPG): ")
    cost_per_gallon = get_float("Enter the price of gas ($/gallon): ")
    trip_miles = get_float("Enter the trip driving distance (in miles): ")
    driving_cost = trip_miles / miles_per_gallon * cost_per_gallon

    display_output(miles_per_gallon, cost_per_gallon, trip_miles, driving_cost)


def display_output(miles_per_gallon, cost_per_gallon, trip_miles, driving_cost):
    print("Fuel Economy: {0:,.2f} mpg".format(miles_per_gallon))
    print("Price per gallon of gas: ${0:,.2f}".format(cost_per_gallon))
    print("Trip driving distance: {0:,.2f} mi".format(trip_miles))
    print("Trip Fuel Cost: ${0:,.2f}".format(driving_cost))


def get_float(message):
    result = 0.0
    badValue = True
    while badValue:
        try:
            result = float(input(message))
            badValue = False
        except ValueError:
            print("Entered number type must be a float.")
            badValue = True
    return result


main()
