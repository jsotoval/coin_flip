import random
def multiple_coin_flips():
    list_of_coin_flips = []
    number_of_flips = input("Please enter the number of times you would like the coin to be flipped: ")
    while int(number_of_flips) > 0:
        heads_or_tails = random.randint(1,2)
        if(heads_or_tails == 1):
            list_of_coin_flips.append("Head")
        else:
            list_of_coin_flips.append("Tail")
        number_of_flips = int(number_of_flips) - 1
    print(list_of_coin_flips, "\nNumber of times that the coin landed on heads: " + str(list_of_coin_flips.count("Head")), "\nNumber of times that the coin landed on tails: " + str(list_of_coin_flips.count("Tail")), "\nTimes that coin was flipped: " + str(len(list_of_coin_flips)))    

def single_coin_flip():
    heads_or_tails = random.randint(1,2)
    if(heads_or_tails == 1):
        print("Head")
    else:
        print("Tail")
