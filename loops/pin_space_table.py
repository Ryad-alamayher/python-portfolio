#pin_space_table.py

GUESSES_PER_SECOND = 10

#min = PINS // (60*GUESSES_PER_SECOND)
#days= min //(24*60)

for digits in range(4,9):
    PINs = 10 ** digits
    MINs = PINs // (60*GUESSES_PER_SECOND)
    DAYs = (MINs) // (60*24)
    
    print (f"{digits} digits: {PINs} PINs, {MINs} minutes, {DAYs} days")
    
    
    
    