def onStrategyStart(n):
        global buy,nh
        nh=main.createNH().REF(1)
        buy=0
        return n

def onBar():
        global buy,quantity
        if(nh.Nh>30) and buy==0:
                quantity=round(amount/O/100)*100
                main.Buy(stock,quantity,O)
                buy=1
                return 0
                
        if (nh.Nl>3) and buy==1:
                main.Sell(stock,quantity,C)
                buy=0
        return 0

