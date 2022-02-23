#가위바위보 게임

import random as r

com = ["가위","바위","보"]

computer = ""

my = ""

for x in range(10):
    computer = r.choice(com)
    my = input("가위바위보중 하나를 입력해 주세요:")
    if computer == "가위":
        if my == "가위":
            print("비겼다")
        if my == "바위":
            print("승리")
        if my == "보":
            print("패배")
    if computer == "바위":
        if my == "바위":
            print("비겼다")
        if my == "가위":
            print("패배")
        if my == "보":
            print("승리")
    if computer == "보":
        if my == "보":
            print("비겼다")
        if my == "가위":
            print("승리")
        if my == "바위":
            print("패배") 
            
    
