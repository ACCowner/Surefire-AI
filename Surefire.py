import openai
import random

# Set up your OpenAI API key
openai.api_key = 'sk-proj-jV5TasUoUhj5faWmM3EzT3BlbkFJgXsDH3879VSH4df3mCzp'

# Define a dictionary of responses
responses = {
    "hi": ["Hi there!", "Hello!", "Hey!"],
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "Pretty good, thanks for asking!"],
    "what's your name": ["I'm Surefire, the chatbot created by ACC.", "My name is Surefire, I'm from ACC."],
    "bye": ["Goodbye!", "See you later!", "Bye now!"],
    "age": ["I'm just a chatbot, so I don't really have an age!", "I don't age, I'm timeless!"],
    "weather": ["I'm sorry, I'm just a chatbot and I can't provide weather updates."],
    "who created you": ["I was created by the ACC team.", "I'm a creation of the ACC developers."],
    "how do you work": ["I work by analyzing your input and generating responses based on predefined patterns."],
    "monke-related": ["Monke gang rise up!", "Monkies are the ultimate beings!", "Monkay!"],
    "monkeys": ["Monkeys are primates that belong to the order Primates, which also includes apes, lemurs, and humans.",
                "There are many different species of monkeys, including capuchins, macaques, and baboons.",
                "Monkeys are known for their dexterous hands and long tails, which they use for balance.",
                "Some monkeys, like the spider monkey, have prehensile tails that can grasp objects.",
                "Monkeys are found in various habitats, including rainforests, savannas, and mountains.",
                "Monkeys are highly social animals and often live in groups called troops or bands.",
                "Monkeys communicate with each other through vocalizations, facial expressions, and body language.",
                "Many monkeys are omnivores, meaning they eat both plants and animals, although diet varies among species.",
                "Some species of monkeys, such as the Japanese macaque, are known for their use of hot springs for relaxation.",
                "Monkeys play important roles in their ecosystems as seed dispersers and prey for larger predators."],
    "thank you": ["You're welcome!", "No problem!", "Glad I could help!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "how's it going": ["It's going well, thanks for asking!", "Everything's good, how about you?"],
    "good": ["That's great!", "Glad to hear it!", "Awesome!"],
    "bad": ["I'm sorry to hear that.", "Hope things get better soon.", "Hang in there!"]
}

# Map various inputs to the "monke-related" response category
monke_related_inputs = ["monke", "monk", "munkee", "monkey", "tej andrews", "max frolick", "ryan wang"]
for input_word in monke_related_inputs:
    responses[input_word] = responses["monke-related"]

def generate_response():
    """Generate a random response for unknown inputs."""
    generic_responses = [
        "I'm not sure I understand.",
        "Could you please elaborate?",
        "Hmm, interesting!",
        "I'll have to think about that!",
        "That's something to ponder!",
        "I'm not programmed to respond to that."
    ]
    return random.choice(generic_responses)

def get_gpt_response(user_input):
    """Generate a GPT-3 response for user input."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def surefire_chatbot():
    """Starts the Surefire chatbot."""
    print("Hi! I'm Surefire, the chatbot created by ACC.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print(random.choice(responses["bye"]))
            break
        elif user_input in responses:
            if "{name}" in random.choice(responses[user_input]):
                print(personalize_response(random.choice(responses[user_input]), name))
            else:
                print(random.choice(responses[user_input]))
        else:
            # Use GPT-3 to generate a response for unknown inputs
            gpt_response = get_gpt_response(user_input)
            print("GPT-3:", gpt_response)

# Start the chatbot
surefire_chatbot()
