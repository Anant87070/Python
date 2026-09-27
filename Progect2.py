# Rule based AI python ChatBot

import datetime
import time

name = input("Hey , Enter your name :")
presentHour = datetime.datetime.now().hour

if 5<= presentHour <= 11:
    print("Good Morning,",name)
elif 11<= presentHour <=17:
    print("Good Afternoon,",name)
elif 17<= presentHour <=20:
    print("Good evening,",name)
else:
    print("Good night,",name)


print("Namasta! Welcime to Rule-Based ChatBot ")
print("You can assk me basic question, Type 'bye' to exit from the bot")

#Chatbot Memory Creation [dictionary of responses]
responses = {
    "hello":"Hi, Welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "Who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that"
}

#Method/Function to get response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey] 
    return "I am not able to tell thet yet. I will learn that soon"

# Take user input

while True:
    userInput = input("please ask your question:")
    reply= getResponseOfBot(userInput)
    print("BOt Response :", reply)

    if "bye" in userInput.lower():
        break
