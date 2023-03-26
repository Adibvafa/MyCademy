import openai
import random
import time
openai.api_key = "key"
  
def Get_Question(arr):
  start = time.time()
  package = {}
  package["reference"] = random.randint(1,3)
  paragraph = arr[package["reference"]]
  question_type = random.randint(1,4)
  if(question_type <= 2):
    package["question"] = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Give a difficult multiple choice question on this paragraph without giving the answer: {paragraph}"}],
    temperature=0.1,
    max_tokens=500,
    top_p=0.95,
  )['choices'][0]['message']['content'].strip()
  elif(question_type == 3):
    package["question"] = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Give a difficult true/false question where the answer is true on this paragraph without giving the answer: {paragraph}"}],
    temperature=0.1,
    max_tokens=500,
    top_p=0.95,
  )['choices'][0]['message']['content'].strip()
  else:
    package["question"] = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Give a difficult true/false question where the answer is false on this paragraph without giving the answer: {paragraph}"}],
    temperature=0.1,
    max_tokens=500,
    top_p=0.95,
  )['choices'][0]['message']['content'].strip()
  
  question = package["question"]
  package["answer"] = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Give an answer to the question, followed by a comprehensive detailed explanation: {question}"}],
    temperature=0.1,
    max_tokens=500,
    top_p=0.95,
  )['choices'][0]['message']['content'].strip()

  end = time.time()
  print(end - start)
  return package

print(Get_Question(['Introduction \nLinear Algebra is one of the most important subject in mathematics and is used in a multitude of applications in a large variety of fields. Linear Algebra is a branch of mathematics dealing with groups of linear equations and their representations in vector spaces. It has tangible applications in physics, economics, engineering and many other fields. This course will provide an introduction to the foundational concepts and techniques of the subject and demonstrate how they can be applied to solve real world problems. \n\n', 'Main body 1 \nThe first concept to understand in Linear Algebra is that of a vector. A vector is an object that has both a magnitude (or length) and a direction associated with it. Vectors can be represented by arrows, with the length of the arrow representing the magnitude and the direction indicated by the direction of the arrow. In Linear Algebra we will generally use the standard mathematical notation for vectors and regard them as elements of a vector space. \n \n', 'Main body 2 \nThe second important concept in Linear Algebra is that of a Matrix. A matrix is a table of numbers that can be used to represent a group of linear equations. A matrix can be thought of as a collection of vectors and can be used to transform one vector into another. Matrices can be used to solve systems of linear equations and can also be used to represent linear transformations. \n\n', 'Main body 3 \nThe third topic covered in this course is that of linear independence. In Linear Algebra, two vectors are said to be linearly independent if they are not multiples of each other. Linear independence is a key concept in solving systems of linear equations and is a basic property of the vector spaces we will encounter. \n\n', 'Main body 4 \nThe fourth and final concept we will cover is inner product spaces. An inner product space is a vector space where the vectors can be "multiplied" together. This multiplication operation is known as an inner product and is used to calculate certain properties of the vector. Inner product spaces are also used to compute certain distances between vectors. \n\n', 'Conclusion \nIn conclusion, a good understanding of the fundamental concepts and techniques of linear algebra are necessary for many applications. In this course, we have provided a comprehensive introduction to the foundational concepts and techniques of the subject and demonstrated how they can be applied to solve real world problems. We hope you now have the knowledge and skills necessary to begin your journey into the exciting world of linear algebra.']))
