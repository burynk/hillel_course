import string


def correct_sentence(text):
    textlist = text.split(". ")
    for i in range(len(textlist)):
        textlist[i] = textlist[i].capitalize()
        if not textlist[i].endswith("."):
            textlist[i] += "."
    return " ".join(textlist)


assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"
assert correct_sentence("greetings, friends.") == "Greetings, friends.", "Test5"
print("ОК")
