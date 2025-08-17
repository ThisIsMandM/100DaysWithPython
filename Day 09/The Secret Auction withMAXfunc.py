from art import gavel
print(gavel)

bid_storage = {}

bid_on = True

while bid_on:
    name = str(input("What is your name?"))
    bid = int(input("What's your bid? $"))
    bid_storage[name] = bid
    next_bidder = str(input("Is there any other bidder? type 'yes' or 'no'?\n")).lower()
        
    if next_bidder == "yes":
        bid_on = True
        print("\n" * 100)
    else:
         
        bid_on = False

    if bid_storage:
        winner = max(bid_storage, key=bid_storage.get)

    print(f"The Winner is {winner}, the final bid is ${bid_storage[winner]}")
    

