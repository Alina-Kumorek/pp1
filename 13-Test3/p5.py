# The object created from a class C contains an array of integers, passed in when the object is created.
# Define a text representation of an object that returns an expression that sums up all the numbers in an array,
# in the order as in the array. Example:
#     C([5,12])  "5+12=17"
#     C([6,0,15])  "6+0+15=21"

class C():

    def __init__(self, arr):
        self.arr = arr
    
    def __str__(self):
        sum = 0
        for i in self.arr:
            sum += i
        
        ex = ""
        for i in self.arr:
            ex += str(i) + "+"
        ex = ex.removesuffix("+")
        ex += "=" + str(sum)

        return ex

def main():
    # function testing
    print(C([5,12]).__str__()=="5+12=17")
    print(C([6,0,15]).__str__()=="6+0+15=21")

if __name__ == "__main__":
    main()