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
    package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a thinking multiple choice question with options a b c d on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=250,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]

  elif(question_type == 3):
    package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a thinking true/false with options true or false question where the answer is true on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=250,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]

  elif(question_type == 4):
    package["question"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a thinking true/false with options true or false question where the answer is false on this paragraph without giving the answer: {paragraph}",
    temperature=0.5,
    max_tokens=250,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]
  question = package["question"]
  package["answer"] = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give an answer to the question, followed by a comprehensive detailed explanation: {question}",
    temperature=0.5,
    max_tokens=250,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )["choices"][0]["text"]

  end = time.time()
  print(end - start)
  return package

#print(Get_Question(['Introduction: As a professional baker with years of experience, I am the most relevant person to create a course on how to make an apple pie. Apple pie is a classic dessert that is loved by many, and making it from scratch is a rewarding experience. In this course, I will guide you through the process of making a delicious apple pie that will impress your family and friends. We will cover everything from selecting the right apples to making the perfect crust.', 'Selecting the Apples: The first step in making an apple pie is selecting the right apples. You want to choose apples that are firm and crisp, with a balance of sweet and tart flavors. Some of the best apples for pie include Granny Smith, Honeycrisp, and Braeburn. Once you have selected your apples, you will need to peel, core, and slice them. I recommend using a sharp knife or an apple peeler to make the process easier.', 'Making the Crust: The crust is an essential part of any apple pie, and making it from scratch is easier than you might think. You will need flour, butter, salt, and cold water to make the crust. Start by mixing the flour and salt in a bowl, then cut in the butter until the mixture resembles coarse crumbs. Add the cold water a little at a time, mixing until the dough comes together. Divide the dough in half and roll out each half on a floured surface. Place one half in the bottom of a pie dish and trim the edges.', 'Making the Filling: The filling is where the magic happens in an apple pie. To make the filling, you will need to mix your sliced apples with sugar, cinnamon, nutmeg, and a pinch of salt. You can also add a tablespoon of lemon juice to give the filling a tangy flavor. Once the filling is mixed, pour it into the prepared crust.', 'Baking the Pie: The final step in making an apple pie is baking it to perfection. Preheat your oven to 375 degrees Fahrenheit and place the pie on the middle rack. Bake for 45-50 minutes, or until the crust is golden brown and the filling is bubbling. Let the pie cool for at least 30 minutes before serving.', 'Conclusion: In conclusion, making an apple pie from scratch is a fun and rewarding experience. By following the steps outlined in this course, you will be able to make a delicious apple pie that will impress your family and friends. Remember to select the right apples, make a perfect crust, mix the filling with the right ingredients, and bake the pie to perfection. With a little practice, you will be able to make an apple pie that is just as good as any bakery.']))
