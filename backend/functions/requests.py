import openai
from decouple import config

# env variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPENAI_API_KEY")

# Get response from openai
# generate custom email
def generate_email_sequence(name, theme):

  prompt = f"Generate an email about {theme} to recipient with name {name} from a sender named Arthur."

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=250,
    n=1,
    stop=None,
    temperature=0.5,
  )

  sequence = response["choices"][0]["text"]

  return sequence
    