def reverseNumber(list):
    start = 0
    end = len(list) -1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
    return list
    

def reverseString(text):
    text_list = list(text)  
    start = 0
    end = len(text_list) -1
    while start < end:
        text_list[start], text_list[end] = text_list[end], text_list[start]
        start += 1
        end -= 1
    return ''.join(text_list)  # Convert list back to a string
