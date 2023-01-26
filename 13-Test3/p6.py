# The counter allows you to count any elements. Create a class C to create counters.
# The initial value of the counter is assigned when the object is created. The class contains the following methods:
#     m1() - returns the counter value
#     m2() - increases the counter value by 1
#     m3() - decreases the counter value by 1
#     m4(n) - increases the counter value by n

# Example:
#     c=C(5)
#     c.m1()  5
#     c.m2()
#     c.m1()  6
#     c.m4(-8)
#     c.m1()  -2
#     c.m3()
#     c.m1()  -3
#     c.m4(10)
#     c.m1()  7

class C():

    def __init__(self, n):
        self.count = n
    
    def m1(self):
        return self.count
    
    def m2(self):
        self.count += 1
    
    def m3(self):
        self.count -= 1
    
    def m4(self, n):
        self.count += n

def main():
    # function testing
    c=C(5)
    print(c.m1()==5)
    c.m2()
    print(c.m1()==6)
    c.m4(-8)
    print(c.m1()==-2)
    c.m3()
    print(c.m1()==-3)
    c.m4(10)
    print(c.m1()==7)

if __name__ == "__main__":
    main()