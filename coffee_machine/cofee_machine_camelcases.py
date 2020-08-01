camel_case = input()
for chars in camel_case:
    if chars.isupper():
        camel_case = camel_case.replace(chars, "_" + chars.lower())
print(camel_case)
