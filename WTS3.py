#WTS3

def greedy(amount):

    coinvalue = [ 1, 5, 10 , 25 ] 
    
    totalcoins = len(coinvalue)

    listresult = []

    temp = totalcoins - 1

    while(temp >= 0):
          
        while (amount >= coinvalue[temp]):
            amount -= coinvalue[temp]
            listresult.append(coinvalue[temp]) # add results to new array
  
        temp -= 1
  
    for temp in range(len(listresult)):
        print(listresult[temp])
  
if __name__ == '__main__':

    amount = input("input integer amount: ")
    greedy(int(amount))
      