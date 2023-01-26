# A class C contains a dictionary with students and their grades. The dictionary is passed to the object when it is created.
# Define a method m(n) that returns a list of students whose average grade is not lower than n.
# Return the list of students as a string, names separated by commas, without spaces, in alphabetical order. Example:
#     s = C({"Peter":[4,5,4]}, "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
#     s.m(4)  "Barbara,Peter"
#     s.m(3)  "Barbara,Harry,Peter"
#     s.m(5)  ""

class C():

    def __init__(self, d):
        self.d = d
    
    def m(self, n):
        l = []

        for i in self.d:
            av = 0

            for j in self.d[i]:
                av += j

            av = av / len(self.d[i])

            if av >= n:
                l.append(i)

        l.sort()

        s = ""
        for i in l:
            s += i + ","
        s = s.removesuffix(",")
        return s

def main():
    s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
    print(s.m(4)=="Barbara,Peter")
    print(s.m(3)=="Barbara,Harry,Peter")
    print(s.m(5)=="")

if __name__ == "__main__":
    main()