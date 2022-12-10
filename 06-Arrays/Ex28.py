# Define a median(array) function that returns the median of the given array of numbers.
# Do not use built-in functions. The median is the middle value in the ordered sequence of numbers
# (https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png).
# Then, using the defined function, calculate and display the median for the following values:
#     a.	[1,0,9,4,6]
#     b.	[6,8,3,1,0,5,7]

def bubblesort(array):

    done = False

    while done != True:
        changed = False

        # Compare each (exept the last) element of the array with the next one and change their location if needed
        for i in range(len(array) - 1):
            a = array[i]
            b = array[i + 1]
            if a > b:
                array[i] = b
                array[i + 1] = a
                changed = True

        # Check if there were any changes made in the current loop iteration
        if changed == False:
            done = True
    
    return array

def median(array):
    array = bubblesort(array)
    if len(array) % 2 != 0:
        med = array[len(array)//2]
    else:
        med = (array[(len(array)//2)-1]+array[len(array)//2])/2
    return med

arrays = [[1,0,9,4,6], [6,8,3,1,0,5,7], [6,8,3,1,0,5]]

for i in arrays:
    print(f"Array: {i}")
    print(f"Median: {median(i)}")
    print()