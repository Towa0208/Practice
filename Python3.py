import random

def validate(hand):
    if hand<0 or hand>2:
        return False
    return True


def pattern(hand,name="ゲスト"):
    hands=["グー","チョキ","パー"]
    print(name+"は"+hands[hand]+"を出しました")


def judge(computer,human):
    if computer==human:
        return "あいこ"
    elif computer==0 and human==1:
        return "負け"
    elif computer==1 and human==0:
        return "負け"
    elif computer==2 and human==1:
        return "負け"
    else:
        return "勝ち"


print("じゃんけんを始めます")
your=input("あなたの名前を入力してください:")
value=int(input("何を出しますか?[グー:0 チョキ:1 パー:2]"))
print("数字を入力してください")

if validate(value):
    computer_hand=random.randint(0,2)

    if your=='':
        pattern(value)
    else:
        pattern(value,your)


    pattern(computer_hand,"コンピューター")
    
    result=judge(value,computer_hand)
    print("結果は"+result+"でした")
else:
    print("入力値が間違えています")