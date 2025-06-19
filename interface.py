from chat_memory import ChatMemory
from model_loader import load_model

def generate_reply(model, tokenizer, device, context, user_input):
    prompt = f"<|system|>\nYou are a helpful assistant.\n{context}\n<|user|>\n{user_input}\n<|assistant|>\n"
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

    model, tokenizer, device = load_model()
    memory = ChatMemory(max_turns=3)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        context = memory.get_context()
        bot_reply = generate_reply(model, tokenizer, device, context, user_input)
        memory.add(user_input, bot_reply)
        print(f"Bot: {bot_reply}\n")

if __name__ == "__main__":
    main()
