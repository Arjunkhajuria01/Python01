#"Cr"eate a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.


# KAUN BANEGA "CR"OREPATI

quiz = [
    {
        "question": "Q1. Why did the computer go to therapy?",
        "options": [
            "A) It lost its memory",
            "B) It had too many tabs open",
            "C) It couldnt find its purpose",
            "D) It kept crashing emotionally"
        ],
        "cr" : "A"
    },
    {
        "question": "Q2. What would happen if you microwave your phone?",
        "options": [
            "A) It charges faster",
            "B) You unlock the multiverse",
            "C) You get a free trip to the repair shop",
            "D) You get 5G inside your brain"
        ],
        "cr" : "B"
    },
    {
        "question": "Q3. Why do owls blink one eye at a time?",
        "options": [
            "A) To keep their eyes moist",
            "B) To take micro-naps",
            "C) To give their brain a loading screen",
            "D) To skip boring conversations"
        ],
        "cr" : "C"
    },
    {
        "question": "Q4. What happens if you press all the elevator buttons at once?",
        "options": [
            "A) You unlock a secret floor",
            "B) The elevator gets confused",
            "C) You get kicked out by security",
            "D) Nothing, except angry looks"
        ],
        "cr" : "D"
    },
    {
        "question": "Q5. Why don't fish ever do homework?",
        "options": [
            "A) They're too cool for school",
            "B) They can't hold pencils",
            "C) They live in schools already",
            "D) They're always underwater"
        ],
        "cr" : "A"
    },
    {
        "question": "Q6. Why did the tomato turn red?",
        "options": [
            "A) Because it saw the salad dressing",
            "B) It was sunburnt",
            "C) It felt shy",
            "D) It lost a bet with a chili"
        ],
        "cr" : "B"
    },
    {
        "question": "Q7. What would you find in a kangaroos pocket?",
        "options": [
            "A) A lost phone",
            "B) A baby kangaroo (joey)",
            "C) Snacks and receipts",
            "D) Another smaller pocket"
        ],
        "cr" : "C"
    },
    {
        "question": "Q8. What happens when you try to tickle yourself?",
        "options": [
            "A) You burst out laughing",
            "B) You level up your ninja skills",
            "C) Nothing at all",
            "D) You unlock self-awareness"
        ],
        "cr" : "D"
    },
    {
        "question": "Q9. Why do cats stare at nothing?",
        "options": [
            "A) They're meditating",
            "B) They're seeing ghosts",
            "C) They're buffering",
            "D) They just enjoy the void"
        ],
        "cr" : "A"
    },
    {
        "question": "Q10. What would happen if you microwave your phone?",
        "options": [
            "A) It charges faster",
            "B) You unlock the multiverse",
            "C) You get a free trip to the repair shop",
            "D) You get 5G inside your brain"
        ],
        "cr" : "B"
    }
]



print("AAPKA SWAGAT HAI KON BANEGA CROREPATI ME  \n  Pehla question aapki computer screen par ")

for q in quiz:
    print(q["question"])

    for opt in q["options"]:
        print(opt)

    ans = input("YOUR ANSWER:- ").strip().upper()

    if ans == q["cr"]:
     print ("correct")
    else:
     print("WRONG")                  # im doing basic right wrong not giving scores yet
     







        

