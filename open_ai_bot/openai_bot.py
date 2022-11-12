from cmd import PROMPT
import os
import openai

openai.api_key = "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"


input_usr = ""

while input_usr != "no":
    prompt = input("Enter something... ")
    if input_usr == "no":
        break
    else:
      response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=3990,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
      )
      result = response.choices[0].text
      print(result + "\n")
      input_usr = input("Do you want to continue? type yes/no ")
