from api import llama

prompt = input("Instruction: ")
preprompt = f"""### Instruction: {prompt}\n### Response:"""
response = llama(preprompt)
try:
    response = response.replace(f"### Instruction: {prompt}", "")
    response = response.replace("### Response: ", "")
    response = response.replace("### Response:", "")
except UnicodeDecodeError as e:
    pass
                    
print(response)
