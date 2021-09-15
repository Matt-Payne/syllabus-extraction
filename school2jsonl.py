import json
import jsonlines


def description2jsonl():
     try:
          path = input("Path of school json file: ")
          path_to_json = input("Path to new jsonl train file: ")
          with open(path) as f:
               f = json.load(f)
               with jsonlines.open(path_to_json, "w") as w:
                    for i in range(int(list(f.keys())[-1][7])): #Get last item for number of schools
                         f[f"school {str(i+1)} description"]
                         desc = f[f"school {str(i+1)} description"]
                         w.write({"prompt": f"{desc}", "completion": "<ideal generated text>"})
     except:
          print("Retry.")
     

description2jsonl()

with open("/Users/muduo/Documents/GitHub/syllabus-extraction/train.jsonl") as f:
     for line in f:
          print(line)