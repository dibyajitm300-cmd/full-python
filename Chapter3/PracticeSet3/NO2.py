#To fill a name in a given template
letter = '''Dear <|Name|>,
            You are selected !
            <|Date|> '''
print(letter.replace("<|Name|>","BABY").replace("<|Date|>","27 Feb 2026"))

print("THANKU")