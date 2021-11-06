#linear search
def linearSearch(arrayt, selected):



    for i in range(len(arrayt)):
        if arrayt[i] == selected:
            house = arrayt.index()
            print("Linear search:", house)
        



if __name__ ==  "__main__":

    global_array = [1,4,7,3,6,8] #random numbers

    print("Here are my numbers:", global_array)

    selected = int(input("Which number would you like me to find:"))
    
    linearSearch(global_array, selected)



