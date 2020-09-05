fruits={"リンゴ":100,"バナナ":200,"オレンジ":400}

for fruit in fruits:
    print(fruit+"は"+str(fruits[fruit])+"円です")
    count=input(str(fruit)+"を何個買いますか?:")
    cost=fruits[fruit]*int(count)
    money=10000
    total_cost=money-cost

    if total_cost<=money:
        print("お支払い金額は"+str(cost)+"円です")
        money-=total_cost

        if money==0:
            print("お財布が空になりました")
        break
    else:
        print("お金が足りません")
        print(fruit+"を買えませんでした")

print("残高は"+str(total_cost)+"円です")