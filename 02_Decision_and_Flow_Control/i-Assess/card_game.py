card_type1, card_num1 = input().split()
card_type2, card_num2 = input().split()
card_type3, card_num3 = input().split()

if (card_type1 == card_type2 == card_type3) and (card_num1 == card_num2 == card_num3):
    print("Double Bonanza")
elif card_type1 == card_type2 == card_type3 or card_num1 == card_num2 == card_num3:
    print("Bonanza")
else:
    print("No Bonanza")