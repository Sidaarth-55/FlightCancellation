import PyPDF2
import os
import transformers
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM, pipeline



def file_to_text(file_path):
    text=''
    if file_path.endswith('.pdf'):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as pdf_file:
                pdf_reader=PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(pdf_reader.pages)):
                    page=pdf_reader.pages[page_num]
                    text+=page.extract_text()
    if file_path.endswith('.txt'):
        with open(file_path,'r') as file:
            text=file.read().rstrip()

    return text

def QA(question,context):
    model= AutoModelForCausalLM.from_pretrained(
        "meta-llama/Llama-2-7b-chat-hf",
        cache_dir="/users/sid/LLMs",
        device_map='auto'
    )

    prompt="[INST]Answer the question using the context.Question:"+question+".Context:"+context+"[/INST]"

    tokenizer=AutoTokenizer.from_pretrained("meta-llama/llama-2-7b-chat-hf", cache_dir="/users/sid/LLMs")

    inputs=tokenizer(prompt, return_tensors="pt").to('mps')
    outputs=model.generate(**inputs, max_new_tokens=20, temperature=0.05)
    response= tokenizer.decode(outputs[0],skip_special_tokens=True)

    

    
    return response.replace(prompt, "")
