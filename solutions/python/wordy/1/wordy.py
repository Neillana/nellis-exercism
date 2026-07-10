import operator


def _parse_text(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    content = question[8:-1]
    content = content.replace("multiplied by", "multiply_by").replace("divided by", "divide_by")
    cache = content.split()
    
    try:
        int(cache[0])
    except ValueError:
        raise ValueError("syntax error")
    
    return cache
    

TRANSLATIONS = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiply_by': operator.mul,
    'divide_by': operator.floordiv
}


def answer(question):
    parts = _parse_text(question)
    result = int(parts[0])
    
    for index in range(1, len(parts)):
        
        if index % 2 == 1:
            op_word = parts[index]
            
            if op_word not in TRANSLATIONS:
  
                if op_word.lstrip('-').isdecimal():
                    raise ValueError("syntax error")
                raise ValueError("unknown operation")
            
            if index + 1 >= len(parts):
                raise ValueError("syntax error")
                
        if index % 2 == 0:
            try:
                number = int(parts[index])
                op_func = TRANSLATIONS[parts[index - 1]]
                result = op_func(result, number)
            except ValueError:
                raise ValueError("syntax error")
                
    return result
