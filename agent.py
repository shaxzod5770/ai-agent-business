from openai import OpenAI import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def ai_agent(user_message): print("AI Agent ishga tushdi 🤖")
response = client.responses.create(
    model="gpt-5.6",
    input=user_message
)

return response.output_text
if name == "main": message = input("Siz nima qilmoqchisiz? ") result = ai_agent(message) print("\nAgent:", result)
