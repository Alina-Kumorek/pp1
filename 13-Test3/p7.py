# A class C contains the following static/class methods:
#     m1(n) – returns a number based on n, with the odd digits removed
#     m2(n) – returns true when each subsequent digit in a number n is equal to
#       or greater than the previous digit or false otherwise
#     m3() – returns a string, with the digits missing from the number n, in ascending order

# Example:
#     C.m1(4231564)  4264
#     C.m1(79381)  8
#     C.m2(125579)  True
#     C.m2(4557879)  False
#     C.m3(23557)  "014689"
#     C.m3(12340)  "56789"

class C():

    @staticmethod
    def m1(n):
        n = str(n)
        m = ""
        for i in n:
            if int(i) % 2 == 0:
                m += i
        return int(m)
    
    @staticmethod
    def m2(n):
        n = str(n)
        check = True
        p = int(n[0])
        for i in range (1, len(n)):
            if int(n[i]) < p:
                check = False
            p = int(n[i])
        return check
    
    def m3(n):
        n = str(n)
        m = ""
        for i in range(10):
            if str(i) not in n:
                m += str(i)
        return m

def main():
    # function testing
    print(C.m1(4231564)==4264)
    print(C.m1(79381)==8)
    print(C.m2(125579)==True)
    print(C.m2(4557879)==False)
    print(C.m3(23557)=="014689")
    print(C.m3(12340)=="56789")

if __name__ == "__main__":
    main()