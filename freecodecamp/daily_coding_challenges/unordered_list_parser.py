"""
Given the string of a valid unordered list in Markdown,
return the equivalent HTML string.
"""
def parse_unordered_list(markdown):
    list_items = []
    for line in markdown.plit("\n"):
        list_item = line[2:].strip()
        list_items.append(f"<li>{list_item}</li>")

    unordered_list = f"<ul>{''.join(list_items)}</ul>"
    return unordered_list