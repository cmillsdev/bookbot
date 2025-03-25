def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for t in text:
        if t.lower() not in char_dict:
            char_dict[t.lower()] = 0
        char_dict[t.lower()] += 1

    return char_dict

def sort_char_dict(char_dict):
    char_list = []

    def sort_on(dict):
        return dict["count"]

    for c in char_dict:
        if c.isalpha():
            char_list.append({"char":c, "count":char_dict[c]})
    char_list.sort(reverse=True, key=sort_on)

    return char_list
    

