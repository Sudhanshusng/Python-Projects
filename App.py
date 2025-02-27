# app.py
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Load the pre-trained model and tokenizer (using distilbert for simplicity; switch to CodeT5 or StarCoder for better code)
model_name = "distilbert-base-uncased"  # You can swap with "Salesforce/CodeT5-base" or "bigcode/starcoder" for code-specific tasks
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

st.title("Code Assistant 🤖")
st.write("Enter a code snippet or description, and I’ll suggest completions or explanations!")

# Input from user
user_input = st.text_area("Enter your code or question:", height=150)

if st.button("Generate Suggestion"):
    if user_input:
        # Generate a response using the model
        prompt = f"Complete or explain this code: {user_input}"
        try:
            # Generate text (adjust max_length and other parameters as needed)
            output = generator(prompt, max_length=150, num_return_sequences=1, temperature=0.7)
            suggestion = output[0]['generated_text'].replace(prompt, "").strip()  # Remove the prompt from the output
            
            st.subheader("Suggestion/Explanation:")
            st.write(suggestion)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some code or a question!")

st.write("Note: This is a simple demo. For better code-specific suggestions, use models like CodeT5 or StarCoder.")

# Optional: Add some styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)