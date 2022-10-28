class Product:
    def __init__(self,code,name,price,manu_cost,stock,month_units):
        print("*** Morgan's Sample Stock Statment ***")
        print("Product Code:",code,)
        print("Product Name:",name,)

        print("Sale Price:",price,"CAD")
        print("Manufacture Cost:",manu_cost,"CAD")
        print("Monthly Production:",month_units,"units (Approx.)")
    
    



class Application:

    loop = False
    print("Welcome to Morgan's Magnificent Products")
    while loop == False:
        code = input("Please enter your Product's code: ")
        int(code)
        if code >= 100 & code <= 1000:
            loop == True
        else:
            print("Invalid Product Code, please try again")
    loop = False
    name = input("Please enter the Name of your Product: ")
    while loop == False:
        price = input("Please enter the Price of the Product: ")
        float(price)
        if type(price) == float & price >= 0:
            loop = True
        else:
            print("Invalid Price, please try again")
    loop = False
    while loop == False:
        manu_cost = input("Please enter the Manufacturing Cost: ")
        float(manu_cost)
        if type(manu_cost) == float & manu_cost >= 0:
            loop = True
        else:
            print("Invalid Manufacture Cost, please try again")
    loop = False
    while loop == False:
        stock = input("Please enter the amount of Stock of the Product: ")
        int(stock)
        if type(stock) == int & stock >= 0:
            loop = True
        else:
            print("Invalid amount of Stock, please try again")
    loop = False
    while loop == False:
        month_units = input("Please enter the amount of stock made in a month: ")
        int(month_units)
        if type(month_units) == int & month_units >= 0:
            loop = True
        else:
            print("Invalid Monthly Units, please try again")
    App_product = Product(code,name,price,manu_cost,stock,month_units)
