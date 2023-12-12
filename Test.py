from transformers import PhobertTokenizer, TFAutoModelForCausalLM

def restore_punctuation(sentence, beam_size=5):
    tokenizer = PhobertTokenizer.from_pretrained("vinai/phobert-base")
    model = TFAutoModelForCausalLM.from_pretrained("vinai/phobert-base")

    inputs = tokenizer.encode(sentence, return_tensors="tf", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=512, num_beams=beam_size, early_stopping=True)

    restored_sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return restored_sentence

# Sử dụng hàm restore_punctuation
input_sentence = "toi dang hoc"
restored_sentence = restore_punctuation(input_sentence)
print(f"Input: {input_sentence}")
print(f"Restored output: {restored_sentence}")
