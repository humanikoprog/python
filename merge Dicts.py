def merge_dictionaries(first_dict, second_dict):
   merged = first_dict.copy()
   merged.update(second_dict)
   return merged
   
d1 = { "A": "Auron", "B": "Braska", "C": "Crusaders" }
d2 = { "C": "Cid", "D": "Dona" }
print(merge_dictionaries(d1,d2))
# {'A': 'Auron', 'B': 'Braska', 'C': 'Cid', 'D': 'Dona'} 
