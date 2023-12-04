import os
import openai
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY") 
msgs = []

# Main function that interacts with GPT-3.5-turbo
def get_test_cases(app,format,info):
    msg="Please give me test cases for "+app+" Application in the given format :" +format + ". Also consider this additional information"+info+ " Aditionally I want each test case inside flower brackets, if test case has lost of steps put [] inside for each step"
    msgs.append ({"role": "user", "content": msg})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
    test_cases=response["choices"][0]["message"]["content"]

    #generate pdf using fpdf

    pdf_file=convert_to_pdf(test_cases)

    return pdf_file


# returning text on the webpage
    # return test_cases


def convert_to_pdf(text,filename="testcases.pdf"):
    pdf=FPDF()
    pdf.add_page()  
    pdf.set_font("Arial", size = 12)  
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)
    return filename


