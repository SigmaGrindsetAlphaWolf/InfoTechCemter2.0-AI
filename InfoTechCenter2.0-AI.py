import random
from time import sleep

def getGasLevel():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def getGasStation():
    gasStations = ["Shell", "Speedway", "Marathon", "Buc-ee's", "Mobile", "Costco", "Meijer", "7Eleven"]
    return random.choice(gasStations)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = getGasLevel()

    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low" or gasLevelIndicator == "Quarter Tank":
        print(f"Your gas tank is {gasLevelIndicator.lower()}, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {getGasStation()}, which is {milesToGasStationLow} miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half empty, no refueling is necessary.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is 3/4 full.")
    else:
        print("Your gas tank is full, good job.")

gasLevelAlert()