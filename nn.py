import markovify, json

# Get raw text as string.
with open("out.txt") as f:
    text = f.read().replace("'", "SINGLE_QUOTE").replace("\"", "DOUBLE_QUOTE").replace("(", "OPEN_PAREN").replace(")", "CLOSE_PAREN").replace("[", "OPEN_SQBRAK").replace("]", "CLOSE_SQBRAK")


# Build the model.
text_model = markovify.NewlineText(text)

def makeSentence(mod):
    return mod.make_sentence().replace("SINGLE_QUOTE", "'").replace("DOUBLE_QUOTE", "\"").replace("OPEN_PAREN", "(").replace("CLOSE_PAREN", ")").replace("OPEN_SQBRAK", "[").replace("CLOSE_SQBRAK", "]")


# Print five randomly-generated sentences
def printSentence():
    success = False
    while not success:
        try:
            print(json.loads(makeSentence(text_model)))
            success = True
        except json.JSONDecodeError:
            pass

while True:
    print("\n\n")
    printSentence()
    print("\n\n---------------------------")
    input()