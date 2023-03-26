import openai
import random
openai.api_key = "key"
  
def Get_Question(arr):
  package = {}
  package["reference"] = random.randint(1,3)
  paragraph = arr[package["reference"]]
  question_type = random.randint(1,5)
  if(question_type <= 2):
    package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a multiple choice question on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=500,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  elif(question_type == 3):
    package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a true/false question where the answer is true on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=500,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  else:
    package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a true/false question where the answer is false on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=500,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  
  question = package["question"]
  package["answer"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give an answer to the question, followed by a comprehensive detailed explanation: {question}",
    temperature=0.2,
    max_tokens=500,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  return package
