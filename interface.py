import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Set pad_token if not defined
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def generate_reply(user_input):
    prompt = f"<|system|>\nYou are a helpful assistant.\n<|user|>\n{user_input}\n<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    output_ids = model.generate(
        **inputs,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
    )

    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    if "<|assistant|>" in output:
        response = output.split("<|assistant|>")[-1].strip()
    else:
        response = output.strip()

    return response

def main():
    print("\n🤖 Chatbot ready. Type '/exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break
        bot_reply = generate_reply(user_input)
        print(f"Bot: {bot_reply}\n")

if __name__ == "__main__":
    main()