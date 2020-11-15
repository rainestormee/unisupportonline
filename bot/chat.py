import random

def getRandomWord(words):
    return words[random.randrange(0,len(words)-1)]

excited = ['excited', 'energetic', 'aroused', 'bouncy', 'nervous', 'perky', 'antsy'] # + 4 points
tender = ['intimate', 'loving', 'warm', 'hearted', 'warm-hearted', 'sympatetic', 'touched', 'soft', 'kind', 'tender'] # + 3 points
scared = ['tense', 'nervous', 'anxious', 'jittery', 'frightened', 'panic-stricken', 'terrified', 'scared'] # - 3 points
angry = ['irritated', 'resentful', 'miffed', 'upset', 'mad', 'furious', 'raging', 'angry'] # - 5 points
sad = ['down', 'blue', 'mopey', 'grieved', 'dejected', 'depressed', 'heartbroken', 'sad'] # - 4 points
happy = ['happy', 'fulfilled', 'contented', 'glad', 'complete', 'satisfied', 'optimistic', 'pleased'] # + 5 points

triggerWords = ['kill', 'end', 'nobody cares', 'die', 'useless', 'myself'] # - 10 points

swearWords = ['fuck', 'shit', 'piss', 'idiot', 'cunt', 'retard', 'motherfucker', 'twat', 'racist'] # - 2 points

openingMessage = ['Hey, my name is chatty what is your name?', 'Beep. Boop. I am chatty, who are you?']

feelingMessage = ['How have you been?', 'How is everything going?', 'Are things okay?', 'How are you today?', 'How have you been lately?']

interestedMessage = ['Tell me more!', 'I wanna hear more!', 'Is that so?', 'Please tell me more!', 'I really wanna hear more about it!', 'Can you tell me more?']

positiveResponse = ['Keep up the good work!', 'So everything is going stelarlly.', '']

negativeResponse = ["You shouldn't feel bad!", 'You can always try later!', 'Never give up!', 'Sadness is part of the road to hapiness!']

def parse(message):
    score = 0
    for word in excited:
        if word in message:
            score += 4
    for word in tender:
        if word in message:
            score += 3
    for word in scared:
        if word in message:
            score -= 3
    for word in angry:
        if word in message:
            score -= 5
    for word in sad:
        if word in message:
            score -= 4
    for word in happy:
        if word in message:
            score += 5
    for word in swearWords:
        if word in message:
            score -= 2
    for word in triggerWords:
        if word in message:
            score -= 10
    return score

def chatBot():
    score = 0
    chatIsActive = True

    print(getRandomWord(openingMessage))

    user_message = input()
    score += parse(user_message)

    while chatIsActive:
        print(getRandomWord(feelingMessage))
        user_message = input()
        score += parse(user_message)
        # Anything above 30 is golden
        if(score > 30):
            print("Wow you're doing really great maybe you should share some of the hapiness!")
            return 1
        
        # From 10 to 30 is kinda okay
        if(score > 10 and score <= 30):
            print(getRandomWord(positiveResponse))
        
        # From -10 to 10 is neutral
        if(score >= -10 and score <= 10):
            print(getRandomWord(interestedMessage))

        # From -10 to -40 is kinda bad
        if(score < -10 and score > -40):
            print(getRandomWord(negativeResponse))
        
        # Anything below -40 is really bad *D*A*N*G*E*R
        if(score <= -40):
            return -1
        
        user_message = input()
        score += parse(user_message)

if(chatBot() == -1):
    print('Call 111!')