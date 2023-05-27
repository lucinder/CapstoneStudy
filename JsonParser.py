import json
def loadJson():
    path = ""
    trial_max = 8
    path = "FCI_Data_Raw.json"
    out = ""
    with open(path) as user_file:
        qs = json.load(user_file)
    for q in qs:
        qn = q["Question #"]
        out += "\n<li>"
        out += "\n<p><b>Question Number: </b>" + qn+"<p>"
        out += "\n<p><b>Transcribed Question: </b>" + q["Transcribed Question"]+"<p>"
        out += "\n<p><b>Correct Letter Response: </b>" + q["Correct Answer"]+"<p>"
        out += "\n</li>"
        for i in range (1,trial_max):
            out += "\n<li>"
            out += "\n<a class=\"btn btn-secondary btn-sm\" data-bs-toggle=\"collapse\" href=\"#FCIQ"+qn+"T"+i+"\" role=\"button\" aria-expanded=\"false\" aria-controls=\"#FCIQ"+qn+"T"+i+"\">"+(i<6?"":"Variant ")+"Trial "+(i<6?i:(i-5))+"</a>"
            out += "\n<div class=\"collapse\" id=\"#FCIQ"+qn+"T"+i+"\">"
            out += "\n<p><b>GPT Letter Response: </b>" + q["T"+i+" Answer"]+"<p>"
            out += "\n<p><b>GPT Explanation: </b>" + q["T"+i+" Explanation"]+"<p>"
            out += "\n</div>"
            out += "\n</li>"
    return out
if __name__ == "__main__":
    return loadJson()