money=10000
cd=1667
count=input("cdを何枚買いますか?")

total_cd=cd*int(count)

total_cost=money-total_cd

print("CDを"+str(count)+"枚買いました")

if(int(total_cost)>0):
    print("CDを買って"+str(total_cost)+"円余りました")
elif(total_cost==money):
    print("ピッタリでした")
elif(0>total_cost):
    print("買えませんでした")