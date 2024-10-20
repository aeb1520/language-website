import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_vocab_list():
    vocab_list = input("Please enter a vocabulary list: ")
    return vocab_list

def get_language():
    language = input("What is the language you want to learn: ")
    return language

def get_topic():
    topic = input("What is the style of story you want: ")
    return topic

def get_level():
    level = input("What is the level you want the output to be in: ")
    return level

def get_length():
    while True:
        try:
            word_limit = int(input("What is the word limit for the story? "))
            if word_limit > 0:
                return word_limit
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def generate_story(vocab_list, language, topic, level, length):
    prompt = (
        f"Write a {level} story in {language} with the style of {topic} with a maximum words of {length}"
        f"that uses these vocab words: {vocab_list}."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    story = response.choices[0].message.content
    return story

def generate_explanation(story, language, vocab_list):
    prompt = (
        f"Here is a story: {story} in {language} with the vocab words: {vocab_list}.\n"
        "Please simplify this story while ensuring that the following vocabulary words are included: "
        f"{vocab_list}. Make it easier to understand."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    explanation = response.choices[0].message.content 
    return explanation


def main():
    vocab_list = get_vocab_list()
    language = get_language()
    topic = get_topic()
    level = get_level()
    length = get_length()
    story = generate_story(vocab_list, language, topic, level, length)
    print("\nHere is your story:\n")
    print(story)
    
    #ask if the user wants to have more explanation (basically easier version)
    easy = input("Do you want an easier version of the story? (yes/no)").strip().lower()
    if(easy == "yes"):
        story_easy = generate_explanation(story, language, vocab_list)
        print("\nHere is your story, but easier:\n")
        print(story_easy)
        
    

if __name__ == "__main__":
    main()
