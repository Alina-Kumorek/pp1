# Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer.
# Then write a program that displays the first five lines from the file and then waits for the Enter key to be pressed.
# Then repeat displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

run = True
options = ["", "q", "Q"]

f = open("pan-tadeusz.txt", encoding="UTF-8")

while run:
    for i in range(5):
        print(f.readline())
    
    x = "x"
    while x not in options:
        x = input("Press Enter to continue, pres Q to quit: ")
    
    if x in options[1:3]:
        run = False
    
f.close()