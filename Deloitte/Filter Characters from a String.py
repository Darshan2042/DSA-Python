def filter_string(target,reference):
    result = ""

    for ch in target:
        if ch not in reference:
            result += ch
        else:
            None
    return result


target = "HelloSir"
reference = "oir"
print(filter_string(target,reference))
