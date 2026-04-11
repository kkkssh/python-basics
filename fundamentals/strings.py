# =========================
# STRINGS
# =========================

# SPLIT
fruit_text = "apple banana grape"
fruit_list = fruit_text.split()
print(fruit_list)    # ['apple', 'banana', 'grape']

# SPLIT WITH SEPARATOR
fruit_text_with_commas = "apple,banana,grape"
fruit_list_from_commas = fruit_text_with_commas.split(",")
print(fruit_list_from_commas)    # ['apple', 'banana', 'grape']

# REPLACE (STRING UPDATE)
sentence = "Today's special is pasta"
updated_sentence = sentence.replace("pasta", "pizza")
print(updated_sentence)  # Today's special is pizza
print(sentence)      # Today's special is pasta

age_range_text = "twenty-five to thirty"
age_range_text = age_range_text.replace("thirty", "thirty-five")
print(age_range_text)    # twenty-five to thirty-five