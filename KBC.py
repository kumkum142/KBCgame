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



# import tkinter as tk
# from tkinter import messagebox
# import colorsys
# import turtle

# # Questions, answers, and prizes
# questions = ["Question 1: What is the capital of India?\n A: Hyderabad        B: Chennai\n C: Delhi           D: Mumbai\n",
#              "Question 2: Who is the national animal of India?\n A: Lion        B: Elephant\n C: Tiger       D: Peacock\n",
#              "Question 3: Which planet is known as the Red Planet?\n A: Earth        B: Mars\n C: Jupiter      D: Venus\n",
#              "Question 4: What is the largest ocean in the world?\n A: Atlantic Ocean        B: Indian Ocean\n C: Arctic Ocean          D: Pacific Ocean\n",
#              "Question 5: What is the smallest planet in our solar system?\n A: Venus        B: Mars\n C: Mercury      D: Pluto\n",
#              "Question 6: Which country is known as the Land of the Rising Sun?\n A: China            B: Japan\n C: South Korea      D: Thailand\n",
#              "Question 7: What is the chemical symbol for gold?\n A: Au        B: Ag\n C: Fe        D: Hg\n",
#              "Question 8: Who is known as the Father of the Indian Nation?\n A: Jawaharlal Nehru        B: Bhagat Singh\n C: Mahatma Gandhi          D: Subhas Chandra Bose\n"]

# answers = ["C", "C", "B", "D", "C", "B", "A", "C"]
# prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000]

# class QuizApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("KBC Quiz")
#         self.root.geometry("600x400")
#         self.current_question = 0
#         self.total_amount = 0
#         self.current_prize_index = 0
        
#         self.question_label = tk.Label(root, text=questions[self.current_question], font=('Arial', 14))
#         self.question_label.pack(pady=20)
        
#         self.answer_var = tk.StringVar()
        
#         self.option_a = tk.Radiobutton(root, text="A", variable=self.answer_var, value="A", font=('Arial', 12))
#         self.option_a.pack(anchor='w')
        
#         self.option_b = tk.Radiobutton(root, text="B", variable=self.answer_var, value="B", font=('Arial', 12))
#         self.option_b.pack(anchor='w')
        
#         self.option_c = tk.Radiobutton(root, text="C", variable=self.answer_var, value="C", font=('Arial', 12))
#         self.option_c.pack(anchor='w')
        
#         self.option_d = tk.Radiobutton(root, text="D", variable=self.answer_var, value="D", font=('Arial', 12))
#         self.option_d.pack(anchor='w')
        
#         self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=('Arial', 14))
#         self.submit_button.pack(pady=20)
    
#     def check_answer(self):
#         if self.answer_var.get() == answers[self.current_question]:
#             self.total_amount += prizes[self.current_prize_index]
#             self.current_prize_index += 1
#             messagebox.showinfo("Correct", f"Correct Answer!\nYou have won ₹{prizes[self.current_prize_index - 1]}")
#         else:
#             messagebox.showerror("Incorrect", f"Wrong Answer!\nCorrect Answer is {answers[self.current_question]}")
#             self.current_prize_index = 0
        
#         self.current_question += 1
#         if self.current_question < len(questions):
#             self.question_label.config(text=questions[self.current_question])
#         else:
#             self.show_final_amount()
    
#     def show_final_amount(self):
#         messagebox.showinfo("Quiz Over", f"Congratulations!\nTotal amount won: ₹{self.total_amount}")
#         self.root.quit()

# root = tk.Tk()
# app = QuizApp(root)
# root.mainloop()

# # Turtle Graphics for some visual effect
# turtle.bgcolor("black")
# t = turtle.Turtle()
# t.speed(0)
# t.width(2)
# colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

# for i in range(360):
#     color = colorsys.hsv_to_rgb(i / 360, 1.0, 1.0)
#     t.pencolor(color)
#     t.forward(i)
#     t.left(59)

# turtle.done()
