def ai_agent(user_message):
    print("AI Agent ishga tushdi 🤖")
    print("Siz:", user_message)

    response = f"Agent sizning so'rovingizni qabul qildi: {user_message}"

    return response


if __name__ == "__main__":
    message = input("Siz nima qilmoqchisiz? ")
    result = ai_agent(message)
    print("Agent:", result)
