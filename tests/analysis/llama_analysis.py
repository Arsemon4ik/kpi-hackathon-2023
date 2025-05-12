from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")


def llama_analysis(logs: str, classification: str) -> str:
    prompt = f"""
    Analyze the following test logs and provide a short summary:\n\n{logs}\nOverall classification: {classification}\n\nSummary:
    """
    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(inputs.input_ids, max_length=100)
    summary = tokenizer.decode(outputs[0])
    return summary
