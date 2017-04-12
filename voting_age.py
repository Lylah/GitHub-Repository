
#Tech academy workshop drill 

options = []
my_nums = range(1000)
for i in my_nums:
    options.append(str(i))

response = raw_input("How old are you?")

if response in options:
    if int(response) >= 18:
        print "You are old enough to vote!"
    elif int(response) <= 18:
        print "Maybe Next year!"
else:
    print "We didn't understand your response :(
