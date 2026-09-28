response = client.responses.create(
    model="gpt-5.6",
    input=user_message
)

return response.output_text
