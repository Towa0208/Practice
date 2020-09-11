class Func:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def process(self):
        return self.name+":￥"+str(self.price)
    
    def total(self,count):
        total_price=self.price*count

        if count>=5:
            total_price=total_price*0.8

        return round(total_price)

#####################################
              #本文#
#####################################

menu1=Func("リンゴ",100)
menu2=Func("モモ",120)
menu3=Func("ブドウ",230)
menu4=Func("バナナ",80)


menu=[menu1,menu2,menu3,menu4]


index=0

for menus in menu:
    print(str(index)+'.'+menus.process())
    index+=1

order=int(input('商品を入力してください'))
selected=menu[order]
print('選択された商品は:'+selected.name)


count=int(input('個数を入力してください:(5つ以上で2割引き)'))

result=selected.total(count)

print('合計は'+str(result)+'円です')
