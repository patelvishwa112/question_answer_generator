
from pprint import pprint
from Questgen import main
import warnings
warnings.filterwarnings("ignore")


payload = {
            "input_text": "As (newly) expected, the Federal Open Market Committee (FOMC) raised the fed funds rate by 75 basis points, the first hike of that size since 1994. That puts the fed funds target range at 1.5%-1.75%. There was one dissent—Kansas City Fed President Esther George (typically a hawk)—in favor of a lesser 50-basis-point increase. The FOMC confirmed its previously laid-out plan on balance sheet reduction, which just began at the beginning of June—shrinking its holdings of Treasury and mortgage-backed securities by $47.5 billion per month until September, and then upping that to $95 billion per month thereafter."
            ,"max_questions": 10
        }


# Short Question and Answer
qg = main.QGen()
output = qg.predict_shortq(payload)
# pprint (output)

for i in range(len(output["questions"])):
    print("Question-> {}: Answer-> {}".format(output["questions"][i]["Question"], output["questions"][i]["Answer"]))# , output["questions"][i]["context"]))

# Simple Question Answer (Long answer)

answer = main.AnswerPredictor()

for i in range(len(output["questions"])):
    payload3 = {
        "input_text" : '''As (newly) expected, the Federal Open Market Committee (FOMC) raised the fed funds rate by 75 basis points, the first hike of that size since 1994. That puts the fed funds target range at 1.5%-1.75%. There was one dissent—Kansas City Fed President Esther George (typically a hawk)—in favor of a lesser 50-basis-point increase. The FOMC confirmed its previously laid-out plan on balance sheet reduction, which just began at the beginning of June—shrinking its holdings of Treasury and mortgage-backed securities by $47.5 billion per month until September, and then upping that to $95 billion per month thereafter.''',
        "input_question" : output["questions"][i]["Question"]
    
    }
    output = answer.predict_answer(payload3)

    print("Question-> {}: \nShort Answer-> {}".format(payload3["input_question"], output))
