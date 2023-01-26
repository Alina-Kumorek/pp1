# The text t contains information about family members. Define a function f1(t) that extracts the names and ages
# of family members from the text and returns these data in the form of a dictionary, in alphabetical order.
# Define a function f2(d) that returns the total age of all family members based on the dictionary data. Example:
#     f1("Mark is 24 and Ann is 27")  {"Ann":27, "Mark":24}
#     f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")  {"Barbara":7, "John":103, "Peter":11} 
#     f2(f1("Mark is 24 and Ann is 27"))  51
#     f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))  121

def f1(t):

    list = t.split()
    names = []
    alf = []
    ages = []

    for i in range(len(list)):
        list[i] = list[i].strip(".,;!?()")

    for i in list:
        if i.isnumeric():
            ages.append(int(i))
        elif i.istitle():
            names.append(i)
            alf.append(i)

    alf.sort()
    d = {}

    for i in alf:
        d[i] = ages[names.index(i)]

        # alternatywna opcja:
        # for j in range(len(names)):
        #     if i == names[j]:
        #         d[names[j]] = ages[j]

    return d

def f2(d):
    sum = 0
    for i in d:
        sum += d[i]
    return sum

def main():
    # function testing
    print(f1("Mark is 24 and Ann is 27")=={"Ann":27, "Mark":24})
    print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")=={"Barbara":7, "John":103, "Peter":11})
    print(f2(f1("Mark is 24 and Ann is 27"))==51)
    print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))==121)

if __name__ == "__main__":
    main()