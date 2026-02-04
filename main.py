what_to_say = {
    # Greetings
    "hello": "hello!",
    "hi": "hi there!",
    "hey": "hey!",
    "good morning": "good morning ☀️",
    "good afternoon": "good afternoon!",
    "good evening": "good evening!",
    
    # Farewells
    "bye": "bye!",
    "goodbye": "goodbye!",
    "see you": "see you later!",
    "see ya": "see ya!",
    "quit": "okay, exiting...",
    
    # Polite phrases
    "how are you": "I'm doing well, thanks!",
    "how r u": "I'm good! You?",
    "what's up": "not much, you?",
    "thanks": "you're welcome!",
    "thank you": "no problem!",
    "sorry": "it's okay!",
    
    # Questions
    "what is your name": "I'm a simple chatbot.",
    "who are you": "I'm a program that learns replies.",
    "what can you do": "I can chat and learn new replies!",
    "help": "Just type something and I'll reply.",
    
    # Feelings
    "i am happy": "that's great to hear!",
    "i am sad": "I'm sorry to hear that.",
    "i am bored": "want to talk about something fun?",
    "i am tired": "maybe you should get some rest.",
    "i am angry": "take a deep breath, it'll be okay.",
    
    # Fun / random
    "tell me a joke": "Why did the computer go to sleep? Because it was tired of crashing!",
    "lol": "😂",
    "haha": "😄",
    "nice": "glad you think so!",
    "cool": "yeah, pretty cool 😎",
    
    # Yes / No
    "yes": "okay!",
    "no": "alright.",
    "maybe": "hmm, interesting.",
}
while True:
    input1 = input('What do you want to say:')
    if input1 in what_to_say:
        print(what_to_say[input1])
        stay = input('do you want to quit:')
    else:
        say = input(f'What would you say to reply {input1}:')
        what_to_say[input1] = say
        print(what_to_say[input1])
        stay = input('do you want to quit:')
    if stay == 'yes':
        break