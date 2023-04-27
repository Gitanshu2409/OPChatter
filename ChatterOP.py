import time
import random
# Cool ASCII ART LOL
print("")
print("  /$$$$$$  /$$                   /$$     /$$                          /$$$$$$  /$$$$$$$ ")
print(" /$$__  $$| $$                  | $$    | $$                         /$$__  $$| $$__  $$")
print("| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ | $$  \ $$| $$  \ $$")
print("| $$      | $$__  $$ |____  $$|_  $$_/|_  $$_/   /$$__  $$ /$$__  $$| $$  | $$| $$$$$$$/")
print("| $$      | $$  \ $$  /$$$$$$$  | $$    | $$    | $$$$$$$$| $$  \__/| $$  | $$| $$____/ ")
print("| $$    $$| $$  | $$ /$$__  $$  | $$ /$$| $$ /$$| $$_____/| $$      | $$  | $$| $$      ")
print("|  $$$$$$/| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$/|  $$$$$$$| $$      |  $$$$$$/| $$      ")
print(" \______/ |__/  |__/ \_______/   \___/   \___/   \_______/|__/       \______/ |__/      v_1")
print("")



def realworldproblems():
    print("That's my favourite topic......but there are many subtopics here too")
    print("Some of them are -> Climate Change, Education")
    time.sleep(2)
    print("What would you like to discuss about ?")
    time.sleep(1)
    discuss = input("What topic would you like ? : ")

    if "climate" in discuss.lower() or "climate change" in discuss.lower() or "pollution" in discuss.lower():
        print("What do you think reason should be for climate change (or ask me a question)? : ")
        climate()
    elif "violence" in discuss.lower() or "riots" in discuss.lower() or "terrorism" in discuss.lower():
        print("What you think?")
        violenece()
    elif "education" in discuss.lower():
        print("Rather at very large scale or a very short scale education system in cuntries is sstil a problem..")
        print("Make a guess why this is so or ask me a few questions......")
        study()
    else:
        print("Not my cup of tea")
        chatter()

def introduce():
    print("Would like me to introduce myself to you ?")
    prompt = input("Y/N : ")
    if prompt.lower() == "y":
        print("Yo, Myself OPChatter : OP stands for Overpowered\nI was designed in a time crunch of 5 hours\nI am better than my previous Java protoype which took days\nI have many functions\nBut i am mainly meant to create awareness about real world problems..\nCredits : Gitanshu & Simarjeet")
    else:
        print("As you wish")
    chatter()

def calculate():
    print("Oh my favourite :")
    print("Here are my functions:\nAddition(a+b)\nSubtraction(a-b)\nExponentation(a^b)\nMultiplication(a*b)\nDivision(a/b)")
    time.sleep(1)
    print("Choose a and b wisely")
    a = int(input("Choose a : "))
    b = int(input("Choose b : "))
    mathprompt = input("Which function should i perform : ")
    if mathprompt.lower() == "add" or mathprompt.lower() == "addition":
        print("Result : ", a+b)
    elif mathprompt.lower() == "multiply" or mathprompt.lower() == "multiplication":
        print("Result : ", a*b)
    elif mathprompt.lower() == "subtract" or mathprompt.lower() == "differentiate" or mathprompt.lower() == "difference" or mathprompt.lower() == "subtraction":
        print("Result : ", a-b)
    elif mathprompt.lower() == "divide" or mathprompt.lower() == "division":
        print("Result : ", a/b)
    elif mathprompt.lower() == "exponent" or mathprompt.lower() == "exponentation" or mathprompt.lower() == "power":
        print("Result : ",a**b)
    else:
        print("I can't do that")
        print("Try something else.....")
    chatter()

def fact():
    print("Yup, I can tell you random facts :")
    a = float(random.random())
    if a < 0.1:
        print("Competitive art used to be in the Olympics.")
    elif a < 0.2:
        print("A chef's hat has exactly 100 pleats.")
    elif a < 0.3:
        print("Some cats are actually allergic to humans.")
    elif a < 0.4:
        print("The majority of your brain is fat.")
    elif a < 0.5:
        print("Oranges aren't naturally occurring fruits.")
    elif a < 0.6:
        print("Stop signs used to be yellow.")
    elif a < 0.7:
        print("There is a fruit that tastes like chocolate pudding.")
    elif a < 0.8:
        print("Too much water can kill you.")
    elif a < 0.9:
        print("The moon is (slowly) slowing the Earth's rotation.")
    else:
        print("Out of facts right now")
    chatter()

def chatter():
    print("Type -> 'What can you do ?' to know my functionalities")
    chatinpt = input("User Input : ")
    while chatinpt != "quit" or chatinpt != "exit" or chatinpt != "bye":    
        if "introduce" in chatinpt.lower():
            introduce()
        elif "calculate" in chatinpt.lower():
            calculate()
        elif "fact" in chatinpt.lower():
            fact()
        elif "what can you do ?" in chatinpt.lower():
            print("-> I can do math...\n","-> I can tell random facts\n","-> I am designed to discuss about real world problems")
            chatter()
        elif "realworld" in chatinpt.lower() or "real-world" in chatinpt.lower() or "global issues" in chatinpt.lower():
            realworldproblems()
        elif "quit" in chatinpt.lower() or "exit" in chatinpt.lower() or "bye" in chatinpt.lower():
            print("Yeet!")
            exit()
        else:
            print("Sorry..can't do that")
            chatter()

def climate():
    reason = input("User Input : ")
    while reason != "quit" or reason != "exit" or reason != "end":
        if "pollution" in reason.lower():
            print("Sure")
            time.sleep(1)
            print("")
            print("Burning fossil fuels, cutting down forests and farming livestock are increasingly \ninfluencing the climate and the earth's temperature.")
        elif "what is global warming?" in reason.lower() or "global warming" in reason.lower():
            print("In short: The world is getting hotter, and humans are responsible.")
            time.sleep(1)
            print("Climate change describes a change in the average conditions — such as temperature and \n\
rainfall — in a region over a long period of time. NASA scientists have observed Earth’s \n\
surface is warming, and many of the warmest years on record have happened in the past 20 \n\
years. ")
        elif "effect" in reason.lower() and "greenhouse" in reason.lower():
            print("The greenhouse effect is a process that occurs when gases in Earth's atmosphere trap the \n\
Sun's heat. This process makes Earth much warmer than it would be without an atmosphere. \n\
The greenhouse effect is one of the things that makes Earth a comfortable place to live. ")
        elif "carbon" in reason.lower():
            print("Carbon is in carbon dioxide, which is a greenhouse gas that traps heat close to \n\
Earth. It helps Earth hold some of the heat it receives from the Sun so it doesn't \n\
all escape back into space. But CO2 is only good up to a point – beyond that \n\
point, Earth's temperature warms up too much. NASA research satellites such as \n\
OCO-2 and OCO-3 are studying how carbon moves around the planet. ")
        elif "climate" in reason.lower() or "climate change" in reason.lower():
            print("Scientists have been observing Earth for a long time. They use NASA satellites \n\
and other instruments to collect many types of information about Earth's land, \n\
atmosphere, ocean and ice. This information tells us that Earth's climate is \n\
getting warmer. ")
        elif "oceans" in reason.lower():
            print("The ocean covers about 70% of Earth’s surface. So, it’s not surprising that it \n\
plays a large part in Earth’s environment. As Earth warms, water in the ocean \n\
soaks up energy (heat) and distributes it more evenly across the planet. The \n\
ocean also absorbs carbon dioxide from Earth’s atmosphere. The additional  \n\
heat and carbon dioxide in the ocean can change the environment for the many  \n\
plants and animals that live there. ")
        elif "volcano" in reason.lower() or "natural" in reason.lower() or "fluctuations" in reason.lower() or "nature" in reason.lower():
            print("Yeah it is a minor reason")
            print("Volcanic eruptions, fluctuations in solar radiation, tectonic shifts, and even \nsmall changes in our orbit have all had observable effects on planetary warming and \ncooling patterns")
        elif "no idea" in reason.lower() or "don't know" in reason.lower() or "you may tell" in reason.lower() or "tell me" in reason.lower():
            print("Here is a reason --\nHeat-trapping Greenhouse Gases And The Earth's Climate")
        elif "problem" in reason.lower() or "worry" in reason.lower():
            print("More frequent and intense drought, storms, heat waves, rising sea levels, \nmelting glaciers and warming oceans can directly harm animals, destroy the places \nthey live, and wreak havoc on people's livelihoods and communities. As climate change \nworsens, dangerous weather events are becoming more frequent or severe.")
        elif "quit" in reason.lower() or "exit" in reason.lower() or "end" in reason.lower():
            print("ok")
            chatter()
        else :
            print("Out of my Scope")
            climate()
        climate()

def study():
    reasonst = input("User Input : ")
    while reasonst.lower() != "quit" or "exit" or "end":
        if "corruption" in reasonst.lower():
            print("true")
            time.sleep(1)
            print("Corrupt educational institutes make money through Entrance tests, coaching centres, etc. \nUnder the guise of a seat quota for management, they are exploiting donations to obtain money for admissions. \nInstitutes charge high fees which not everyone can afford.")
        elif "grades" in reasonst.lower() or "marks" in reasonst.lower():
            print("Yupp")
            time.sleep(1)
            print("In the education system in India, a student’s intelligence and performance are thought to be mostly determined by their grades. \n")
        elif "competition" in reasonst.lower():
            print("")
            print("Yes, In a perfect world, a student with a score of at least 90% would be regarded as intelligent")
        elif reasonst.lower() == "quit" or reasonst.lower() == "exit" or reasonst.lower() == "end":
            print("OK")
            chatter()
        elif "no idea" in reasonst.lower() or "don't know" in reasonst.lower() or "you may tell" in reasonst.lower() or "tell me" in reasonst.lower():
            print("Ok let me tell you")
            time.sleep(1)
            print("Lack of a budget \
            Too much Pressure on Grades \
            Too much competition \
            Not Focusing on Overall Growth\
            Lack of Training")
        elif "less"in reasonst.lower() or "lack" in reasonst.lower():
            if "budget" in reasonst.lower():
                print("This is so true.......")
                time.sleep(1)
                print("Inadequate levels of funding leave too many students unable to reach established performance benchmarks.")
            elif "teachers" in reasonst.lower():
                print("Nevertheless....still a reason")
                time.sleep(1)
                print("The number of students in search of proper education is way more in comparison to the teachers and faculty available. \nThus, qualified teachers must be appointed to impart knowledge to the future of the country")
            elif "creative" in reasonst.lower() or "creativity" in reasonst.lower():
                print("A sad reality....")
                time.sleep(1)
                print("The world now needs creative minds and the Government must encourage schools \nto boost the students and utilise their capacities to the max and \nnot let their ideas go unheard")
            study()
        else:
            print("i don't know that")
            print("try something else")
        study()

time.sleep(1)

usrname = input("Your Name : ")
time.sleep(0.75)

print("Welcome to ChatterOP : ", usrname)
confirm = input("Would you like to begin : ")
if "no" in confirm.lower() or "nah" in confirm.lower():
    print("Hasta la vista (Goodbye) : Exiting...")
    exit()
elif "yes" in confirm.lower() or "yeah" in confirm.lower():
    chatter()
else:
    exit()
    
