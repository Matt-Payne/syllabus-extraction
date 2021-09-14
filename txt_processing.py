import spacy
import pdf2text

text = pdf2text.read_pdf("/Users/muduo/Downloads/CCJS_497_6380_Correctional_Administration_2215_CCJS_497_Summer_2021.pdf")

nlp = spacy.load("en_core_web_trf")

def get_info(dox):
     doc = nlp(dox)
     for token in doc:
          print(token.text, token.lemma_, token.pos_, "\n", token.tag_, token.dep_,
               token.shape_, token.is_alpha, token.is_stop," \n")