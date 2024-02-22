# import joblib
# # import tensorflow

# def predict(data):
#     # clf = tensorflow.keras.models.load_model("model.h5")
#     # print(clf)
    # return "yes your name is hira"
import os
import requests

# Set the Hugging Face Hub API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Define the API URL for the Mistral-7B-Instruct-v0.1 model
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

# Define the query function
def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

# Define the predict function
def predict(prompt):
    # Send the query with the prompt
    output = query({"inputs": prompt})
   
    # Extract the generated text from the response
    generated_text = output[0]['generated_text']
   
    return generated_text

