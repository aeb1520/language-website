import os
from dotenv import load_dotenv
from openai import OpenAI
import random

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
        f"that uses these vocab words: {vocab_list}"
        f"also please make the story language learner friendly, and make sure the story is something that will help enhance the learner's understanding of the language."
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
        "Please simplify this story while ensuring that the vocabulary words are included: "
        f"{vocab_list}. Make it easier to understand."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    explanation = response.choices[0].message.content 
    return explanation

def generate_hard_version(story, language, vocab_list):
    prompt = (
        f"Here is a story: {story} in {language} with the vocab words: {vocab_list}.\n"
        "Please make this story more complex while ensuring that the vocabulary words are included: "
        f"{vocab_list}."
    )
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    harder_story = response.choices[0].message.content 
    return harder_story

def explain_unknown_words(unknown_words):
    explanations = {}
    for word in unknown_words:
        prompt = f"What does the word '{word}' mean?"
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        explanations[word] = response.choices[0].message.content
    return explanations

def process_version(story, language, vocab_list, version_type, unknown_list):
    #words = []
    if version_type == "easier":
        easy_story = generate_explanation(story, language, vocab_list)
        print("\nHere is your story, but easier:\n")
        print(easy_story)
    elif version_type == "harder":
        hard_story = generate_hard_version(story, language, vocab_list)
        print("\nHere is your story, but harder:\n")
        print(hard_story)

        syntax_easy = get_syntax(words)
        print("\nSyntactical Information for unknown words:\n")
        for word, info in syntax_easy.items():
            print(f"{word}: {info}")

    unknown_response = input(f"Are there any words you don't know in the {version_type} version? (yes/no) ").strip().lower()
    if unknown_response == "yes":
        words = input("Please enter the words you don't know, separated by commas: ").strip().split(',')
        words = [word.strip() for word in words]
        explanations = explain_unknown_words(words)
        print("\nExplanations for unknown words:\n")
        for word, explanation in explanations.items():
            print(f"{word}: {explanation}")

        unknown_list.extend(words)
        
        syntax_hard = get_syntax(words)
        print("\nSyntactical Information for unknown words:\n")
        for word, info in syntax_hard.items():
            print(f"{word}: {info}")

        print("\nThe word list:")
        print(", ".join(set(unknown_list)))


def get_syntax(unknown_words):
    syntax = {}
    for word in unknown_words:
        prompt = f"Provide the parts of speech, conjugations, gender, tense, mode, tone, and any other relevant information for the word '{word}'."
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        syntax[word] = response.choices[0].message.content
    return syntax

#QUIZ FUNCTIONALITY
def generate_sentence(vocab_word, language):
    prompt = (
        f"Please generate a sentence using the vocabulary word '{vocab_word}' in {language}. "
        f"The sentence should be interesting, colloquial, and educational. "
        f"It should also be vivid to achieve a more natural acquisition of the language. "
        f"Additionally, the usage of '{vocab_word}' should be relatively easy to memorize and should "
        f"help enhance memory over time."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    sentence = response.choices[0].message.content
    return sentence

def correct_user_input(user_input):
    prompt = (
        f"Here's a my response: '{user_input}'. "
        f"Please correct it if necessary and explain the usage of the vocab word in the sentence."
    )
    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [{"role": "user", "content": prompt}],
        max_tokens = 150
    )
    correction = response.choices[0].message
    return correction 

def interactive_conversation(vocab_list,language):
    print("Let's start an informal conversation! I'll use one of the vocabularies in a sentence, and you respond using another vocab word.")
    
    for i, vocab_word in enumerate(vocab_list):
        print(f"{generate_sentence(vocab_word,language)}")

        user_input = input("Please type your response, enter 'quit' to:")

        if user_input.strip().lower() == "quit":
            print("Thank you for participating in the conversation! Goodbye!")
            break

        feedback = correct_user_input(user_input)
        print(f"{feedback}")

    print("Conversation finished!")

def main():
    vocab_list = get_vocab_list()
    language = get_language()
    topic = get_topic()
    level = get_level()
    length = get_length()
    story = generate_story(vocab_list, language, topic, level, length)
    print("\nHere is your story:\n")
    print(story)

    unknown_list = []

    unknown_response = input("Are there any words you don't know in the story? (yes/no) ").strip().lower()
    if unknown_response == "yes":
        first_new_words = input("Please enter the words you don't know, separated by commas: ").strip().split(',')
        words = [word.strip() for word in first_new_words]

    first_explanations = explain_unknown_words(first_new_words)
    print("\nExplanations for unknown words:\n")
    for word, explanation in first_explanations.items():
        print(f"{word}: {explanation}")

    unknown_list.extend(word)

    syntax_info = get_syntax(word)
    print("\nSyntactical Information for unknown words:\n")
    for word, info in syntax_info.items():
        print(f"{word}: {info}")

    conversation = input("Would you like to have a conversation using the vocabulary? (yes/no) ").strip().lower()
    if conversation == "yes":
        interactive_conversation(vocab_list,language)
    elif conversation == "no":
        print("Thank you for using the program! Goodbye!")
        return
    
    while True:
        action = input("Do you want an easier or harder version of the story? (easier/harder/quit) ").strip().lower()
        if action == "quit":
            #print("\nWord list:")
            #print(", ".join(set(unknown_list))) 
            #print("Thank you for using the program! Goodbye!")
            break
        elif action in ["easier", "harder"]:
            process_version(story, language, vocab_list, action, unknown_list)
        else:
            print("Invalid input. Please enter 'easier', 'harder', or 'quit'.")    

    
if __name__ == "__main__":
    main()
