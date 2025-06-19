from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    model_name = "microsoft/DialoGPT-small"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # ⚠️ Set pad token manually
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(model_name)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return model, tokenizer, device