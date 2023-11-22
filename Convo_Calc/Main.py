# Functions
def statement_generator(text, decoration):
    # Make a string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def num_check(question, low):

    valid = False
    while not valid:

        error = "Please enter an integer that is more than(or equal to) {}".format(low)
        print()

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# lists go here
time = ["secs", "mins", "hours"]
weigh = ["grams", "kilograms"]

def instructions():
    statement_generator("Instructions / Information", "=")
    print("This generator is here to help you convert things like cm into mm,etc...")
    print("Just enter your measurement, and the magic will happen >:) ")
    print()
    return ""


def user_choice():
    # List of valid responses
    time_ok = ["time", "t"]
    weight_ok = ["weight", "w"]
    distance_ok = ["distance", "dist", "d"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("Do you want to convert Distance Time or Weight? ").lower()

        # Checks for valid response and returns text, integer or image

        if response in time_ok:
            return "time"

        elif response in weight_ok:
            return "weight"

        elif response in distance_ok:
            return "distance"

        else:
            # if response is not valid, output error
            print("Please choose a measurement type!")
            print()


def time_conver():
    valid = False
    while not valid:

        for item in time:
            print(item)

        print()
        unit_one = input("Please enter a unit of time ")
        print()

        if unit_one not in time:
            print("Sorry, this is not a valid unit type!")
            print()

        else:
            unit_num = num_check("How many? ", 1)

        unit_two = input("Select another unit to convert to ")

        print("You wish to convert {} {}s to {}s".format(unit_num, unit_one, unit_two))

        if unit_two not in dist:
            print("BROOOO YOU SUCK SO MUCHH!!! DO BETTER DUDE >:(")
            print()


def distance_conver():

    dist = {
        "1" : "mm",
        "2" : "cm",
        "3" : "m",
        "4" : "km"
    }

    conver_conversy = {}


    print(dist)
    unit_one = input("Please choose a unit ")
    print()




def weight_conver():

    valid = False
    while not valid:

        for item in weigh:
            print(item)

        print()
        unit_one = input("Please enter a unit of weight ")
        print()

        if unit_one not in weigh:
            print("Sorry, this is not a valid unit type!")
            print()


        else:
            unit_num = num_check("How many? ", 1)

        unit_two = input("Select another unit to convert to ")

        print("You wish to convert {} {}s to {}s".format(unit_num, unit_one, unit_two))

        if unit_two not in dist:
            print("BROOOO YOU SUCK SO MUCHH!!! DO BETTER DUDE >:(")
            print()



# def conver_conversy():

# main routine


statement_generator("Welcome to the Ultimate Conversion Calculator!", "-")

first_time = input("For instructions <enter>, or any key to continue ")
print()

if first_time == "":
    instructions()


keep_going = ""
while keep_going == "":

    measurement_type = user_choice()
    print("you chose ", measurement_type)
    print()

    if measurement_type == "distance":
        distance_conver()

    if measurement_type == "time":
        time_conver()

    if measurement_type == "weight":
        weight_conver()

