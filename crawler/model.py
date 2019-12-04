#Cambrige Dictionary Model
def handle_examples(examples):
  example_array = []
  for example in examples:
    examp_content = example.find('span', attrs={'class': "eg deg"}).get_text()
    examp_trans = example.find('span', attrs={'class': "trans dtrans dtrans-se hdb"}).get_text()
    example_array.append((examp_content, examp_trans))
  return example_array

def handle_rank(rank):
  if rank:
    return rank.get_text()
  return rank

class Camdic_model:
    def __init__(self, title, label, audio_src, audio_symbol, rank, define, trans, examples):
      self.title = title.get_text()
      self.label = (label['title'], label.get_text())
      self.audio_src = 'https://dictionary.cambridge.org'+audio_src
      self.audio_symbol = audio_symbol.get_text()
      self.rank = handle_rank(rank)
      self.define = define.get_text()
      self.trans = trans.get_text()
      self.examples = handle_examples(examples)

#Oxford Dictionary Model
def handle_contents(contents):
  dealt_contents = []
  for content in contents:
    sub_title = content[0]
    define = content[1]
    examples = content[2]
    if sub_title:
      sub_title = sub_title.get_text()
    if define:
      define = content[1].get_text()
    if examples:
      examples = content[2]
    example_array = []
    for example in examples:
      example_array.append(example.get_text())
    dealt_contents.append((sub_title,define,example_array))
  return dealt_contents

class Oxfdic_model:
    def __init__(self, title, label, audio_src, audio_symbol, contents):
      self.title = title.get_text()
      self.label = label.get_text()
      self.audio_src = audio_src
      self.audio_symbol = audio_symbol.get_text()
      self.contents = handle_contents(contents)
