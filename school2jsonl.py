import json
import jsonlines

path = input("path")

with open(path) as f:
     f = json.load(f)
     with jsonlines.open("train.jsonl", "w") as w:
          # iterate over each json-object
          for item in f["_default"].items():
               i=1
               desc = item[f"school {str(0+i)} description"]
               target = "ideal generated text"
               w.write({f"{desc}": target})
               i+=1

