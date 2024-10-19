import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("API key not found. Please check the .env file and make sure it's loaded correctly.")

client = OpenAI(api_key=api_key)

#this gets weird kinda need to check later for variables declared
def generate_text(prompt):
    response = client.Completion.create(
        #the version I am using
        engine = "git-3.5-turbo",
        max_words = 20,
        user_input = user_input,
    )

    return client.choices[0].text.strip


def user_interaction_text_and_story():
    
    count = input("Please enter the amount of lexicon you wish to learn about")
    #deal with different input here 1-3, 3 is an error (over max)
    if (count <= 5):
        word_bundle = [] 
        for i in range (n):
            word = input("Enter the word: ")
            word_bundle = word_bundle.append(word)

        #an empty thing to store the sentences
        success_generation = []
        for generate in word:
            sentence = generate_text(word_bundle)
            success_generation.append(sentence)

        #printing
        print("Here are the sentences!")   
        for result in success_generation:
            print(success_generation)
    



def main():
    print("Welcome come to our_website_name")
    print("This is your first ever intermediate language learning website!")
    print("This portion is dedicated to lexicon learning and practices you can do with them beyond")
    print("Please enter the amount of new lexicons you want to learn (1-20), and we will give you niche sentences!")
    print("Different numbers of lexicons are targeted towards different example sentences/stories.")
    print("For 1-5 new words, we will give you example sentences")
    print("For 6-20 new words, we will give you a personalized story")

    user_interaction_text_and_story()
    generate_text()




    

