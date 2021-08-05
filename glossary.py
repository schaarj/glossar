#%%
import json
import re
from markdown import Markdown



#%%
class Term(dict):
   id = None

   def __init__(self, id="") -> None:
       super().__init__()
       self.id = id

   def set_item(self, item, data, lang='de', append=False):
       if lang not in self:
           self[lang] = {}
       if append and item in self[lang]:
           self[lang][item] += f" {data}"
       else:
           self[lang][item] = data
   
   def merge(self, term):
      for k, v in term.items():
         if k not in self:
            self[k] = v
   
   

#%%
class Glossary(dict):
   DEF_RE = re.compile(r'^[ ]{0,3}\[[ ]*id=([^\]]*)[ ]*\]')
   md = Markdown()

   def parse_markdown(self, filename, lang="de"):
      with open(filename, "r", encoding="utf-8") as fh:
         lines = fh.readlines()
         etree = self.md.parser.parseDocument(lines)
      terms = []
      current_term = None
      for item in etree.iter():

         if item.tag == 'h2':
            current_term = Term()
            terms.append(current_term)
            current_term.set_item('term', item.text.strip(), lang=lang)
         
         elif item.tag == 'p' and current_term:
            m = self.DEF_RE.search(item.text)
            if m:
                current_term.id = m.groups()[0].strip()
            else:
               current_term.set_item('definition', item.text, append=True, lang=lang)
      
      for t in terms:
         if t.id in self:
            self[t.id].merge(t)
         else:
            self[t.id] = t


# %%

if __name__ == '__main__':
    g = Glossary()
    g.parse_markdown('Glossar.md')
    g.parse_markdown('Glossary.md', lang='en')
    with open('glossary.json', 'w') as fh:
       json.dump({k: g[k] for k in sorted(g)}, fh, indent=2)
