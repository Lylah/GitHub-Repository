#Tech academy workshop drill, still a work in progress. **THIS CODE ONLY WORKS IN PYTHON 2.7.13**


my_dictionary = {'movie1' : 120, 'movie2' : 90, 'movie3' : 150, 'movie4' : 110 }


count = 0
while count <2:
    user_response = raw_input(["Do you want to see a movie? Please answer 'yes', 'no', or 'maybe'"]).lower()
    possible_responses = ['yes', 'no', 'maybe']
    if user_response in possible_responses:
        count = 2
        if user_response == 'yes' or 'maybe':
            next_question = int(input(["How much time do you have? Please answer in minutes."]))
            for i in my_dictionary:
                if my_dictionary[i] <= next_question:
                    print "You could see " + i
                    
        else:
            print "Have a nice day!"
    elif user_response not in possible_responses:
        count +=1
