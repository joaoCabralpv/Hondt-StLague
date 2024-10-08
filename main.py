class Party:
    def __init__(self,name: str, points:int):
        self.name = name
        self.points = int(points)
        self.divisor = 1
        self.recived = 0

    def get_display_info(self) -> str:
        return f"{self.name};{self.recived}"

def max_points(partyList:list[Party]) -> Party:
    max = partyList[0]
    for party in partyList:
        if party.points/party.divisor > max.points/max.divisor:
            max = party
        elif party.points/party.divisor == max.points/max.divisor:
            if party.points < max.points:
                max = party
    return max

def base_method(partyList:list[Party],distribute:int,increment:float):
    for _ in range(0,distribute):
            p:Party = max_points(partyList)
            p.recived+=1
            p.divisor+=increment


def Hondt(partyList:list[Party],distribute:int):
    print("Hondt")
    base_method(partyList,distribute,1)

def StLague(partyList:list[Party],distribute:int):
    print("St Lague")
    base_method(partyList,distribute,2)

def main():
    method = None
    distribute = 0
    partyList = []

    print("What method do want to use?")
    print("1-Hondt")
    print("2-St Lague")
    while True:
        method=input("Method: ").strip().lower()
        if method == "1" or method == "hondt":
            method = Hondt
            break
        if method == "2" or method == "stlague" or method ==  "stlaguë":
            method = StLague
            break
        print("Invalid input")

    print("What is the number of thing to distribute?")
    while True :
        try:
            distribute = int(input("Enter the number of things").strip())
            break
        except:
            print("Invalid Input")

    while True:
            print("Instert the name of the party and the number of points, separated by commas Ex:example,62831")
            print("Input finish whan you're done")
            party_data = input().strip()
            if party_data.lower() == "finish":
                break
            try:
                party_data = party_data.split(",",1)
                partyList.append(Party(party_data[0],party_data[1]))
            except:
                print("Invalid input")

    """if method == Method.Hondt:
        Hondt(partyList,distribute)
    elif method == Method.StLague:
        StLague(partyList,distribute)"""
    method(partyList,distribute)

    for party in partyList:
        print(party.get_display_info())


if __name__ == "__main__":
    main()