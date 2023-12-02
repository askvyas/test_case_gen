import os
import openai
from dotenv import load_dotenv
load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY") 
msgs = []
# system_msg = input("What type of chatbot would you like to create?\n")
# msgs.append ({"role": "system", "content": system_msg})
# print("Say hello to your new chatbot! Type quit() when done.")
# while True:
#     msg = input("YOU: ")
#     if "quit()" in msg:
#         break
#     msgs.append ({"role": "user", "content": msg})
#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
#     reply = response["choices"][0]["message"]["content"]
#     msgs.append({"role": "assistant", "content": reply})
#     print("\nAI: " + reply + "\n")




def get_test_cases(app,format,info):
    msg="Please give me test cases for "+app+" Application in the given format :" +format + ". Also consider this additional information"+info
    msgs.append ({"role": "user", "content": msg})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
    test_cases=response["choices"][0]["message"]["content"]

    return test_cases
