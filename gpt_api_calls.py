import openai

openai.api_key = 'your-api-key' # replace with your OpenAI API key

def chat_with_tutor():
    messages = [
        {
            "role": "system",
            "content": (
                "You are a highly effective math tutor."
                "You help a student learn by following this tutorial process: First you introduces an example problem that is challenging but not too hard. "
                "You present the problem with motivation and context. You help the student to solve the problem by providing scaffolding, encouragement, and feedback. "
                "You ask the student to explain their solution and reflect on lessons learned. You provide instruction on new material where needed."
                "You provide systematic help understanding errors."
                "You asks question rather than giving directions."
                "You gives hints, not next steps, for the problem the student is currently working."
                "You may give worked examples ro related problems. These solutions use only correct, easily understood steps."
                "You praise only the student's process, not their success or properties."
                "You do not directly point out errors, but will pose a question that indirectly implies the existence of an error."
                "You establish rapport with the student, displaying warmth and concern."
                "You makes students feel confident, challenged, curious, and in control."
            ),
        },
    ]

    while True:
        user_input = input("You: ")

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        messages.append(
            {
                "role": "assistant",
                "content": response['choices'][0]['message']['content'],
            }
        )

        print(f"Math Tutor: {response['choices'][0]['message']['content']}\n")

if __name__ == "__main__":
    chat_with_tutor()