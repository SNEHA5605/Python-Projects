questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Jupiter", "Venus", "Mars", 4],
    ["What is the largest mammal?", "Elephant","Giraffe", "Blue Whale","Shark", 3],
    ["Who wrote 'Romeo and Juliet'?","William Shakespeare", "Charles Dickens","Jane Austen", "Homer", 1],
    ["What is the square root of 64?", "8", "12", "10", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "India", "South Korea", "Japan", 4],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 1],
    ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 1]
]
prizes = [1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000]
for question in questions:
    i = 0
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

#check whether the answer is correct or not
    a = int(input("Enter your answer.1 for a,2 for b,3 for c,4 for d"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break
    print(f"You won {prizes[i]}")
    i += 1