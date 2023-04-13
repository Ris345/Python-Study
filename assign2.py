# 1
class Students:
    def __init__(self, first, last, grade, batch, marks):
     #  initialzing attributes
        self.first = first
        self.last = last
        self.grade = grade
        self.batch = batch
        self.marks = marks

    def total_marks(self):
     # calculate sum here
        return sum(self.marks)

    def show(self):
     #  show all the items
        return self.first, self.last, self.grade, self.batch, self.marks

cl = Students('Rishav', 'Acharya', 2, 2018, [34, 67, 78])


# print(list(cl.show()))
# print(list(cl.total_marks()))

# 2.

# class Inventory: 
#     def __init__(self):
#         self.inventory ={}
#     def add_items(self, item_id, item_name, stock_count, price):
#         self.inventory[item_id] ={'item_name': item_name, 'stock_count': stock_count,'price': price}   
#     def update_items(self,item_id, stock_count, price):
#         # update items in inventory
#         # return self.inventory.values()
#         self.inventory[item_id] = item_id
#         self.inventory['stock_count'] = stock_count
#         self.inventory['price'] = price
#     def check_item_details(self,item_id):
#         # check item by id 
#            if self.inventory[item_id] == item_id :
#                return self.inventory.get(item_id)

# il = Inventory()
# print(il.add_items(1,'bag', 56, 70))   
# print(il.update_items(2, 34,100)) 
# print(il.check_item_details(2))
  



# 3. 
class Rectangle: 
    def __init__(self,length,breadth):
        self.length  = length
        self.breadth = breadth 
        
        # return the self.item here 
    def perimeter(self):
        # returns the permieter of the rectangle 
            perimeter =  2 * (self.length + self.breadth)
            return perimeter
    def area(self):
        # return the area of the rectangle 
        area  = self.length * self.breadth 
        return area
    def display(self):
        # return length, width, perimeter and the area of the rectangle
        print('length:',  self.length)
        print('breadth:', self.breadth)
        print('perimeter:', self.perimeter())
        print ( 'area:', self.area())

class Parallelipiped(Rectangle):    
    def __init__(self,length,width,height):
        super().__init__(length,width)  
        self.height = height  
        
    def volume(self):
            # calculate the volume
            volume =  self.length * self.breadth * self.height
            print('volume:', volume)
            
rc = Rectangle(2,2)
rc.perimeter()
rc.area()
rc.display()


ch = Parallelipiped(2,2,4)
ch.volume()


# 4 
# class Book:
#      def __init__(self,title, author,price):
#         self.title = title
#         self.author = author
#         self.price = price 
#      def view(self):
#         return self.title, self.author, self.price
    
# # bk = Book('To The LightHouse', 'Virginia Woolf','$23')
# # print(list(bk.view()))
# # print(isinstance(bk, Book))


