import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Create a Streamlit app
st.title("Text Generation with Hugging Face GPT-2")

# Input text
input_text = st.text_area("Enter some text:", "Once upon a time")

# Generate text when a button is clicked
if st.button("Generate"):
    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text using the model
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the generated text and display it
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    st.text("Generated Text:")
    st.write(generated_text)
