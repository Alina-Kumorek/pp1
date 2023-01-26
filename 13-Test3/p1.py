# Define a function f(n) that represents any integer n using sticks.
# The function returns a string containing as many sticks as indicated by the number. 
# or efficient calculations, the sticks are grouped in groups of five and separated by a minus sign. Example:
#     f(-4)  ""
#     f(0)  ""
#     f(5)  "/////"
#     f(7)  "/////-//"
#     f(10)  "/////-/////"
#     f(11)  "/////-/////-/"

def f(n):
    if n > 0:
        c = 0
        s = ""
        for i in range(n):
            if c == 5:
                c = 1
                s += "-/"
            else:
                c += 1
                s += "/"
        return s
    else:
        return ""

def main():
    # function testing
    print(f(-4)=="")
    print(f(0)=="")
    print(f(5)=="/////")
    print(f(7)=="/////-//")
    print(f(10)=="/////-/////")
    print(f(11)=="/////-/////-/")

if __name__ == "__main__":
    main()