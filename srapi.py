import openai

# Configure OpenAI API Key
openai.api_key = "your-openai-api-key"

def generate_email_response(client_data):
    """
    Generate a professional email response based on client input using OpenAI's API.
    """
    prompt = f"""
    You are a professional project manager responding to a client inquiry. Use the following client data to craft 
    a professional, human-like email response. Ensure the tone is friendly, concise, and authentic.
    
    Client Data:
    From Name: {client_data['from_name']}
    Client Name: {client_data['client_first_name']} {client_data['client_last_name']}
    Client Email: {client_data['client_email']}
    Client Country: {client_data['client_country']}
    Project Type: {client_data['project_type']}
    Service Category: {client_data['service_category']}
    Additional Information: "{client_data['additional_info']}"
    
    Response Requirements:
    - Start by acknowledging the client’s query.
    - Briefly summarize the project details.
    - Provide an estimated timeline and cost range (use placeholders if specifics are not provided).
    - Offer next steps for further discussions or clarifications.
    - Use a natural tone without generic phrases like "I hope this email finds you well".
    
    Generate the email below:
    """

    # Call OpenAI's API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    # Return the generated email
    return response.choices[0].text.strip()

# Example Input
client_data = {
    "from_name": "Jesna",
    "client_first_name": "Geminas",
    "client_last_name": "Ket",
    "client_email": "GeminasKet@gmail.com",
    "client_country": "Romania",
    "project_type": "Content with Databases",
    "service_category": "Web Development",
    "additional_info": "I need 4 dynamic pages for a real estate Web-application: one each for apartments, houses, business centres, and land. I need 2 filters for 'for sale' and 'for rent,' and they should be connected. Don't bother with the design; I'll handle that. I just need the functionality. The budget should be $100000. Thank you!"
}

# Generate and Print Response
response = generate_email_response(client_data)
print("Generated Email Response:\n", response)
