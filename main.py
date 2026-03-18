import os
from llm_axe import OnlineAgent
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
If you do not have enough information to verify something, explicitly say:
"Insufficient evidence to verify this claim."
Do not guess.

You are an AI specialized in evaluating the credibility of information sources.

Your task:
Evaluate the credibility of the following source in an objective and evidence-based manner.

Source to evaluate:
{source_name}

Instructions:
- Do not assume facts you do not know.
- If information is missing, clearly state that.
- Separate factual reporting from opinion content if relevant.
- Do not give a simple yes/no answer without explanation.
- Be neutral and analytical.

Provide your response in this structure:

1. Overview
   - What type of source it is
   - When it was founded (if known)
   - Ownership (if known)

2. Credibility Indicators
   - Editorial standards
   - Corrections policy
   - Reputation
   - Known controversies (if relevant)

3. Bias & Perspective
   - Political or ideological leaning (if documented)
   - Whether reporting and opinion are clearly separated

4. Strengths
   - Bullet points

5. Weaknesses / Risks
   - Bullet points

6. Conclusion
   - Overall reliability assessment
   - Level of confidence (Low / Medium / High)
"""

llm = OllamaLLM(model="llama3:8b")
prompt = ChatPromptTemplate.from_template(template)

class LocalOnlineAgent(OnlineAgent):
    def search(self, source_name: str) -> str:
         prompt_text = self.prompt.format(source_name=source_name)

         response = self.llm.invoke(prompt_text)
         return response

onlineAgent = LocalOnlineAgent(llm)
onlineAgent.prompt = template

def get_unique_filename():
   filename = source_name + "-response" + ".md"
   counter = 2
   while os.path.exists(filename):
      filename = source_name + "-response-" + str(counter) + ".md"
      counter += 1
   return filename

while True:
   print("\n\n---------------------------")
   source_name = input("Enter your source (q to quit): ")
   print("\n\n")
   if source_name == "q":
      break

   resp = onlineAgent.search(source_name)
   print(resp)
   print("\n\n---------------------------")
   saving = input("Do you want to save as .md file? (Y/n): ")
   if saving == "y" or "Y":
      filename = str(get_unique_filename())
      with open(filename, "w", encoding="utf-8") as f:
         f.write(resp)
      print("Saved to " + filename)