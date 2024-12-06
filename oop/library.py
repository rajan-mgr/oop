class Library():
    opening_time="9 am" #not dependent on object so outside defined function or object (depend on class) 
    closing_time="9 pm"
    name="indian Library"
    
    @classmethod        #making a function related to class to change time
    def change_time(cls,otime,ctime):
        cls.opening_time=otime
        cls.closing_time=ctime
    # @classmethod
    # def change_name(cls, name):
    #     cls.name=name
    
    @staticmethod
    def is_open(hour):
        return 9<=hour and hour<=21  
        
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
    def show_detail(self):
        print("Name of the book:",self.title)
        print(f"Author of the book: {self.author}")    
        
b1=Library("Muna Madan","Laxmi Prasad")
b2=Library("Eklo","Buddhi Sagar")

# print(Library.openin_time)

Library.opening_time="10 am" #chaning value of opening time
print(f"Library Hours:{ Library.opening_time}-{Library.closing_time}")
Library.change_time("10am","8pm")
print(f"Updated library hours:{Library.opening_time}-{Library.closing_time}")       
# print(Library.name)
# Library.change_name("american Library")
# print(Library.name)
print(Library.is_open(10))  #While calling static function we use class
    