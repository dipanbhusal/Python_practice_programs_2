def case_converter(camelcase, seperator):
    output_words = camelcase[0].lower()
    for letter in camelcase[1:]:
        if letter.isupper():
            output_words += seperator + letter.lower()
        else:
            output_words += letter 
    return output_words

result = case_converter('DipanIsMyName', '-')
print(result)