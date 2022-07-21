# spam,
# toast
text = "eggs {spam} bacon {toast}"
#                                ^
# we want "eggs {} bacon {}", ("spam","toast")


def parse_template(template):
    capturing = False
    element = ""
    elements = []
    stripped_template = ""

    for char in template:

        if char == "{":
            capturing = True
            stripped_template += char
        elif char == "}":
            capturing = False
            elements.append(element)
            element = ""
            stripped_template += char
        elif capturing:
            element += char
        else:
            stripped_template += char

    # "eggs {} bacon {}", ("spam","toast")
    return stripped_template, tuple(elements)


stripped, elements = parse_template(text)

print(stripped)
print(elements)
