# (p2.py) Define a function f(arr) that returns true if the given two-dimensional array is a valid multiplication table,
# or false otherwise. Example:
#     f([[1,2,3],[2,4,6],[3,6,9]])  True
#     f([[1,2],[2,4]])  True
#     f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]])  True
#     f([[1,2],[3,6]])  False
#     f([[1,2,3],[2,4,6]])  False
#     f([[1,2,3],[2,5,6]])  False

def f(arr):
    if len(arr) == len(arr[0]) and len(arr) > 0:
        check = True
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] != (i + 1) * (j + 1):
                    check = False
        return check
    else:
        return False

def main():
    # function testing
    print(f([[1,2,3],[2,4,6],[3,6,9]])==True)
    print(f([[1,2],[2,4]])==True)
    print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]])==True)
    print(f([[1,2],[3,6]])==False)
    print(f([[1,2,3],[2,4,6]])==False)
    print(f([[1,2,3],[2,5,6]])==False)

if __name__ == "__main__":
    main()