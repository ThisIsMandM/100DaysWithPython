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
max_bid_name = None
max_bid = -1
for name , bid in bid_storage.items():
    if bid > max_bid:
        max_bid = bid
        max_bid_name = name
    else:
        max_bid = max_bid
    
print(f"The Winner is {max_bid_name}, the final bid is ${max_bid}")
    

