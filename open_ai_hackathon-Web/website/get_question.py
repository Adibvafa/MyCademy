def get_question(arr):
  import openai
  import random

  openai.api_key = "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"
  
  package = {}
  package["reference"] = random.randint(1,3)
  paragraph = arr[package["reference"]]
  package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"give a multiple choice or true/false question on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=2500,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  question = package["question"]
  package["answer"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"give an answer to the question, followed by a comprehensive detailed explanation: {question}",
    temperature=0.5,
    max_tokens=2500,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  return package