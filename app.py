import os
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


# Core LLM chat function
def chat(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.set_page_config(page_title="Agentic AI Opportunity Finder", layout="centered")
st.title("🤖 Agentic AI Opportunity Finder")
st.write("Enter a business or ministry area to explore Agentic AI ideas:")

# User input field
user_input = st.text_input("What business/ministry area would you like to explore?")

if st.button("Generate AI Opportunity"):
    if user_input:
        with st.spinner("Analyzing opportunity..."):

            # Step 1
            step1_messages = [
                {"role": "system", "content": "You are a helpful assistant with strong business analysis skills."},
                {"role": "user", "content": "Pick a business area that might be worth exploring for an Agentic AI opportunity."}
            ]
            business_area = chat(step1_messages)

            # Step 2
            step2_messages = [
                {"role": "system", "content": "You are a business consultant skilled at identifying challenges in various industries."},
                {"role": "user", "content": f"Present a pain-point of '{business_area}', something challenging that might be ripe for an Agentic AI solution."}
            ]
            pain_point = chat(step2_messages)

            # Step 3
            step3_messages = [
                {"role": "system", "content": "You are an expert in building Agentic AI solutions."},
                {"role": "user", "content": f"Given the pain point: '{pain_point}', propose an Agentic AI-based solution for the '{user_input}' domain."}
            ]
            agentic_solution = chat(step3_messages)

        # Display results
        st.subheader("📌 Step 1 - Business Area:")
        st.success(business_area)

        st.subheader("⚠️ Step 2 - Pain Point:")
        st.info(pain_point)

        st.subheader("🤖 Step 3 - Agentic AI Solution:")
        st.write(agentic_solution)
    else:
        st.warning("Please enter a business or ministry area.")
