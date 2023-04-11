# 1
class Students:
    def __init__(self, first, last, grade, batch, marks):
     #    initialzing variables
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
#     def __init__(self, item_id, item_name, stock_count,price):
#         self.item_id = item_id
#         self.item_name = item_name
#         self.stock_count = stock_count
#         self.price = price
#         self.inventory = {}
    
#     def add_item(self):
#         # add items in the inventory
        
#      def update_item(self):
#         # update items in the dict
#       def check_item(self):
#         # returns item with the respective id 
     
        
# 3. 
# class Rectangle: 
#     def __init__(self):
#         # return the self.item here 
#         def perimeter(self):
#         # returns the permieter of the rectangle 
#             def area(self):
#         # return the area of the rectangle 
#              def display(self):
#         # return length, width, perimeter and the area of the rectangle
    
# class Parallelipiped:
#     def __init__(self):
#         # return the parent class info
#         def volume(self):
#             # calculate the volume



# 4 
class Book:
     def __init__(self,title, author,price):
        self.title = title
        self.author = author
        self.price = price 
     def view(self):
        return self.title, self.author, self.price
    
# bk = Book('To The LightHouse', 'Virginia Woolf','$23')
# print(list(bk.view()))
# print(isinstance(bk, Book))


