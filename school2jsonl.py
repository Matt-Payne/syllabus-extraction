import json
import jsonlines

path = input("path: ")

def description2jsonl(path):
     with open(path) as f:
          f = json.load(f)
          with jsonlines.open("train.jsonl", "w") as w:
               for i in range(int(list(f.keys())[-1][7])): #Get last item for number of schools
                    f[f"school {str(i+1)} description"]
                    desc = f[f"school {str(i+1)} description"]
                    target = "ideal generated text"
                    w.write({f"{desc}": target})

description2jsonl(path)