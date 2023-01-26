# The computer system registers all entries into the car park ("in") and exits from the car park ("out").
# Define the function f(d), which for the given data will return an array containing the registration numbers
# of the vehicles that remain in the car park, in alphabetical order. Example:
#     cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
#     ["BA111","in"],["BA123","out"],["KR234","in"]]
#     f(cars)  ["BA111","GX444","KR234"]

def f(d):
    l = []
    for i in range(len(d)):
        if d[i][1] == "in":
            l.append(d[i][0])
        if d[i][1] == "out":
            l.remove(d[i][0])
    l.sort()
    return l

def main():
    # function testing
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],["BA111","in"],["BA123","out"],["KR234","in"]]
    print(f(cars)==["BA111","GX444","KR234"])

if __name__ == "__main__":
    main()