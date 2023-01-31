""" 
This is a quiz program that uses a dictionary of quizzes to test the user.
The user is printed a list of available quiz topics. 
Then, they select which quiz they would like to take.
Their progress is recorded and their results are printed at the end of each quiz.
Additional (topics: quizzes) can be added or removed to the all_quizzes dictionary.
Additional (questions: answers) can be added or removed to each nested topic dictionary.

Software Development Capstone
Due: 1/22/2023 
"""

# Store each quiz as a dictionary Keys = questions, Values = answers
all_quizzes = {
    'Art': {
        'Who painted the Mona Lisa?': 'Leonardo Da Vinci', 
        'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
        'Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?': 'Chicago',
        'Which kid\'s TV characters are named after Renaissance artists?': 'Teenage Mutant Ninja Turtles',
        'The graphite in an artist\'s pencil is made of what chemical element?': 'Carbon'
    }, 
    'Space': {
        'Which planet is closest to the sun?': 'Mercury',
        'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus', 
        'How many moons does Mars have?': '2'
    }, 
    'Sports': {
        'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': 'Simone Biles',   
        'Which country has won the soccer world cup the most times?': 'Brasil',   
        'What does MLB stand for?': 'Major League Baseball'
    }
}


# Define a function that loops through the all_quizzes dictionary and prints the topic of each quiz
def print_topics():

    # Create an empty list for available quiz topics
    list_of_topics = []

    # Loop through the dictionary of quizzes and add each topic to the empty list
    for quiz in all_quizzes:
        list_of_topics.append(quiz)

    # Since the keys of the dictionary are the topics, you can simplfy to
    list_of_topics = all_quizzes.keys()

    # Print the available topics, adding a comma to separate each
    print(', '.join(list_of_topics))


# Define a function that uses the user's topic selection to deliver the correct quiz
# return the quiz questions and answers
def get_quiz_by_topic(user_topic):

    # Convert the user's input to title case to match topics
    users_topic_title = user_topic.title()

    # Using the user's topic selection, send the quiz to the take_quiz function
    user_quiz = all_quizzes.get(users_topic_title)

    return user_quiz


# Loop through each question: answer and tally the points for the quiz
# return the total questions asked, and the total points 
def take_quiz(user_quiz):
    
    # Start counters for the number of correct answers and total number of questions
    total_score = 0
    number_of_questions = 0
    
    # Loop through each question: answer pair
    for question, answer in user_quiz.items():

        # Increase the number of questions by one each loop
        number_of_questions += 1

        # Print the question for the user to answer
        print(question)

        # Save the user's answer to a variable
        user_answer = input().lower()

        # Convert the correct answer to lower to ignore case
        correct_answer = answer.lower()

        # Compare the user's answer to the correct answer while ignoring case
        if user_answer == correct_answer:

            # Increase the score if the user got the question right
            total_score += 1

            # Print a message letting them know they got it right
            if total_score == 1:
                print('That\'s correct! You have 1 point.')
            else:
                print(f'That\'s correct. You now have {total_score} points.')
        
        # If they answered incorrectly, let them know that the correct answer was
        else:
            print(f'I\'m sorry, the correct answer was {answer}')

    # Send the quiz results to be printed to the user
    # better to write functions with defined input and output, easier to test. 
    return total_score, number_of_questions


# A function that uses the user's score and the total possible points to print the results
def print_results(total_score, number_of_questions):

    if total_score == number_of_questions:
        print(f'Congradulations! You got all {number_of_questions} questions correct!')
    else:
        print(f'You got {total_score} of the {number_of_questions} questions correct.')


# create a main function to define the starting point of the program 

def main():
    # Ask the user what type of quiz they would like to take
    print('What type of quiz would you like to take? The topics are: ')

    # Loop through the quiz list and print the topic of each quiz
    print_topics()

    # Ask the user what type of quiz they want to take
    user_topic_selection = input()  # add validation here to prevent user entering invalid topic, perhaps in a new function 

    # call the functions that represent the parts of the quizzing process in order 
    # Eaasier to look at main and see the flow through the program and order of operations 

    # Use the user's choice to select the dictionary that has the correct topic
    quiz = get_quiz_by_topic(user_topic_selection)

    total_score, number_of_questions = take_quiz(quiz)    

    print_results(total_score, number_of_questions)

main()
