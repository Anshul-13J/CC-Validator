def check_sum(card):
    s=0
    card = list(card)
    if len(card)!= 16:
        return False
    for i in range(16):
        card[i]=int(card[i])
        
    check_digit = card.pop()
    
    
   # print(card)
    for i in range(0,15,2):
        card[i] *= 2
        if card[i]>=10:
            card[i]= 1 + (card[i]%10)
        
   # print(card)

    for i in range(15):
        s += card[i]
        
    if s>100:
        s=s%100
    if s%10 == int(check_digit):
        return True
    
    
cc_num= input("Enter your 16-digit card number (in the format xxxxxxxxxxxxxxxx): ")
validator= check_sum(cc_num)
if validator:
    print("CC is valid")
else:
    print("CC is invalid")
    
        
    
