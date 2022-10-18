height = 164
in2f = 12
cm2in = 2.54

height_in = height / cm2in
feet = int(height_in // in2f)
in_left = round(height_in % in2f, 1)

print(f"I am {height} cm tall, i.e. {feet} feet and {in_left} inches.")