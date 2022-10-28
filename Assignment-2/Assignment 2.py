class Product:
    print("*** Morgan's Sample Stock Statment ***")
    def _init_(self,code,name,price,manu_cost,stock_lvl,month_units_manu):
        print("Product Code: ",code,)


class Application:

    print("Welcome to Morgan's Magnificent Products")
    code = input("Please enter your Product's code?: ")
    name = input("what is the name of your Product?: ")
    price = input("how much is the sale price of your Product?: ")
    manu_cost = input("how much does it cost to build?: ")
    stock_lvl = input("What's your stock level?: ")
    month_units_manu= input("What's the estimated amount of product made in a Month?: ")
    App_product = Product(code,name,price,manu_cost,stock_lvl,month_units_manu)



        


