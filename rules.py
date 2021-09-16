from typing import Text
import spacy
from spacy.matcher import Matcher
from txt_processing import get_info
from txt_processing import text

nlp = spacy.load("en_core_web_trf")

import os
os.chdir('/Users/muduo/Documents/syllabus-extraction')

class match_with_rules(object):
     wlist = ("Grade", "graduate", "undergraduate", "course", "class", 'late', 'late work', "syllabus", "withdraw policy", "course withdraw", "withdrawing from course", "weekly", "assignments", "week", "day", "content", "description", "materials", "outcomes", "assignment", "grade", "university")

     noun_adp_noun = [
          {"POS": {"IN": ["NOUN", "PROPN"]}, "LOWER": {"NOT_IN": wlist}, "LEMMA": {"NOT_IN": wlist}},
          {"POS": {"IN": ["ADP"]}},
          {"POS": {"IN": ["NOUN","PROPN"]}, "LOWER": {"NOT_IN": wlist}, "LEMMA": {"NOT_IN": wlist}},
          {}
     ]

     noun_noun= [
          {"POS": {"IN": ["NOUN", "PROPN"]}, "LOWER": {"NOT_IN": wlist}, "LEMMA": {"NOT_IN": wlist}},
          {"POS": {"IN": ["NOUN", "PROPN"]}, "LOWER": {"NOT_IN": wlist}, "LEMMA": {"NOT_IN": wlist}}
     ]

     verb_pobj = [
          {"POS": "verb", "LOWER": {"NOT_IN": wlist}, "LEMMA": {"NOT_IN": wlist}},
          {"DEP": "pobj", "LOWER": {"NOT_IN": wlist}, "LEMMA": {'NOT_IN': wlist}}
          ]

     verb_pobj_dobj = [
          {"POS": "verb", "LOWER": {"NOT_IN": wlist}, "LEMMA": {"NOT_IN": wlist}},
          {"DEP": "compound"},
          {"DEP": "dobj", "LOWER": {"NOT_IN": wlist}, "LEMMA": {'NOT_IN': wlist}}
          ]


     m_tool = Matcher(nlp.vocab)
     m_tool.add('noun_adp_p/noun', [noun_adp_noun])
     m_tool.add("noun_noun", [noun_noun])
     m_tool.add("object of preposition", [verb_pobj])
     m_tool.add("direct object", [verb_pobj_dobj])

     def __init__(self, doc):
          self.doc = doc
          self.get_matches()

     def get_matches(self):
          doc = nlp(text)
          matches = self.m_tool(doc)
          for match_id, start, end in set(matches):
               string_id = nlp.vocab.strings[match_id]
               span = doc[start:end]  # The matched span
               print(f"rule: {string_id}",  span.text) ########### "print"

match_with_rules(text)

get_info("studying for government policies")

spacy.explain("dobj")



FOCUS ON KEYWORDS

`An general introduction to using POS POS in...`


### Matt rules:
# this is a creative writing course
course = [

          {"LOWER": "this"},
          {"LOWER": "is"},
          {"LOWER": {"IN": ["a", "the"]}},
          {"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}},
          {"POS": {"IN": ["NOUN", "PROPN"]}},
          {"LOWER": {"IN": ["course", "class"]}}
]

# this course presents topics in proportional reasoning
presents = [
            {"LOWER": "this"},
            {"LOWER": {"IN": ["course", "class"]}},
            {"LEMMA": {"IN": ["presents", "present"]}},
            {"LOWER": "topics"},
            {"LOWER": {"IN": ["in", "on", "about", "with", "by", "for", "at"]}},
            {"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}},
            {"POS": {"IN": ["NOUN", "PROPN"]}}
]

# Study the concepts of injury prevention
study = [
         {"LOWER": {"IN": ["study", "analyze", "define", "evaluate"]}},
         {"LEMMA": {"IN": ["the", "a", "in"]}},
         {"LOWER": {"IN": ["concepts", "concept"]}},
         {"LEMMA": {"IN": ["of", "on", "in", "related"]}},
         {"POS": {"IN": ["NOUN", "PROPN", "ADJ"]}},
         {"POS": {"IN": ["NOUN", "PROPN"]}}
]
