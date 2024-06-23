print("\n")
print("Computer asks a question to the user")
print("\n")
print("Okay, Let's get started")
print("\n")
print("======================= KAUN BANEGA CROREPATI ===========================")
print("\n")

questions = [
             "Question 1 : What is the capital of India ? \n A : Hyderabad        B : Chennai  \n C : Delhi            D : Mumbai \n " ,
             "Question 2 : Who is the national animal of India ? \n A : Lion        B : Elephant  \n C : Tiger       D : Peacock \n ",
             "Question 3 : Which planet is known as the Red Planet ? \n A : Earth        B : Mars  \n C : Jupiter      D : Venus \n ",
             "Question 4 : What is the largest ocean in the world ? \n A : Atlantic Ocean        B : Indian Ocean  \n C : Arctic Ocean          D : Pacific Ocean \n ",
             "Question 5 : What is the smallest planet in our solar system ? \n A : Venus        B : Mars  \n C : Mercury      D : Pluto \n ",
             "Question 6 : Which country is known as the Land of the Rising Sun ? \n A : China            B : Japan  \n C : South Korea      D : Thailand \n ",
             "Question 7 : Who is known as the Father of the Indian Nation ? \n A : Jawaharlal Nehru        B : Bhagat Singh  \n C : Mahatma Gandhi          D : Subhas Chandra Bose \n ",
             "Question 8 : What is the chemical symbol for gold ? \n A : Au        B : Ag  \n C : Fe        D : Hg \n ",
             "Question 9 : What is the tallest mountain in the world ? \n A : K2                  B : Kangchenjunga  \n C : Mount Everest       D : Lhotse \n ",
             "Question 10 : What is the largest planet in our solar system ? \n A : Earth          B : Jupiter  \n C : Saturn         D : Neptune \n "
            ]

answers = ["Delhi", "Tiger", "Mars", "Pacific Ocean", "Mercury", "Japan" , "Mahatma Gandhi", "Au" , "Mount Everest" , "Jupiter"]
Answers = ["delhi" , "tiger" , "mars" , "pacific ocean" , "mercury", "japan" , "mahatma gandhi" , "au" , "mount everest" , "jupiter"]

prizes = ["₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000", "₹20,000", "₹40,000", "₹80,000" , "₹90,000" ,"₹1,00,000"]
prize_amounts = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,90000,100000]  # For calculating total amount

flag = 0
flag1 = 0
current_prize_index = 0
total_amount = 0

for x in range(0, len(questions)):
    print(questions[x])
    answer = input("Enter Your Answer: ")

    if (answer == answers[x]) or (answer == Answers[x]):
        print("Correct Answer!!")
        print(f"You have won {prizes[current_prize_index]}!\n")
        total_amount += prize_amounts[current_prize_index]
        current_prize_index += 1  # Move to the next prize
        flag = flag + 1
    else:
        print("Wrong Answer!!")
        print("\n")
        correct_answer = answers[x]
        print(f"Correct Answer is {correct_answer}")
        print("You do not win any prize.\n")
        current_prize_index = 0  # Reset prize index
        flag1 = flag1 + 1
        print("\n\n")

print(f"Number of correct answers: {flag}")
print(f"Number of wrong answers: {flag1}")
print("\n\n")

print("Congratulations")
print("\n")

print(f"Total amount won: ₹{total_amount}")
print("\n\n")


