def pers(a):
    n = 0
    productlist = []
    number= a
    while len(str(number)) > 1:
        perslist = [int(i) for i in str(number)]
        products = 1
        for j in perslist:
            products *= j
        productlist.append(products)
        number = products
        n += 1
    return productlist,n

def searchforpers(a,b,c):
    resultn = 1
    listofproductpers = []
    numb=0
    if a == "a":
        for i in range(b,c):
            if not ("0" in str(i) or ("2" in str(i) or "4" in str(i) or "6" in str(i) or "8" in str(i)) and "5" in str(i)) or 0==int(i) or 10==int(i) or 25==int(i):
                persloc = pers(int(i))
                if persloc[1]> resultn:
                    numb = int(i)
                    resultn=persloc[1]
                    listofproductpers=persloc[0]
            else:
                if numb == 0:
                    listofproductpers = [int(i), 0]
                    numb = int(i)
        return numb,listofproductpers,resultn
    if a == "b":
        for i in range(0,99999999999999999999999999999999999999999999999999999):
            if not ("0" in str(i) or ("2" in str(i) or "4" in str(i) or "6" in str(i) or "8" in str(i)) and "5" in str(i)) or 0==int(i) or 10==int(i) or 25==int(i):
                persloc = pers(int(i))
                if persloc[1] == b:
                    return int(i), persloc[0]

#Persistence finder example:
#print(pers(int(input("Which number do you want to know the multiplicative persistence of?")))

#Persistence searcher mod A example:
#print(searchforpers("a",0,int(input("Search through 0 and which number?"))))

#Persistence searcher mod B example:
#print(searchforpers("b",int(input("This will show you the smallest number that has the persistence level of your choice. Input the level you want to know.",0))))
