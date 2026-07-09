import re
# Translate english words into Pig Latin using regex-based rule matching.
# Regex capturing groups turn word parts into LEGO-style building blocks we can move around.
# Each rule extracts specific segments (bricks: prefix, rest) so the word
# can be rearranged (append brick: "ay") according to Pig Latin transformation rules.

# LEGO-bricks: ? vowel, xr, yt + rest
RULE_1 = r"^(?:[aeiou]|xr|yt)(.*)$"

# LEGO-bricks: consonants + rest
RULE_2 = r"^([^aeiou]+)(.*)$"

# LEGO-bricks: consonants + qu + rest
RULE_3 = r"^([^aeiou]*qu)(.*)$"

# LEGO-bricks: consonants before y + rest
RULE_4 = r"^([^aeiou]+)(y.*)$"


# Helper functions for applying the Pig Latin transformation rules.

# Each function uses the capturing groups from the regex pattern
# to rearrange the word parts (prefix + rest) — like LEGO-style
# building blocks — and appends "ay" as required.

# Input: a word that matches the corresponding regex rule.
# Output: the transformed Pig Latin word.

# starts with vowel/xr/yt -> no rearranging, just append "ay"
def _apply_rule_1(word):
    return word + "ay"


# consonant cluster → move + "ay"
def _apply_rule_2(word):
    word_match = re.match(RULE_2, word)
    return word_match.group(2) + word_match.group(1) + "ay"


# consonants + qu → move + "ay"
def _apply_rule_3(word):
    word_match = re.match(RULE_3, word)
    return word_match.group(2) + word_match.group(1) + "ay"


# consonants before y → move + "ay"
def _apply_rule_4(word):
    word_match = re.match(RULE_4, word)
    return word_match.group(2) + word_match.group(1) + "ay"


def _translate_word(word):
    """
    Selects the appropriate rule and rebuilds the word from its
    LEGO‑style components using the corresponding helper function.
    
    Input: a word.
    Output: its Pig Latin form.
    """
    match word:
        case _ if re.match(RULE_1, word):
            return _apply_rule_1(word)
        case _ if re.match(RULE_3, word):
            return _apply_rule_3(word)
        case _ if re.match(RULE_4, word):
            return _apply_rule_4(word)
        case _ if re.match(RULE_2, word):
            return _apply_rule_2(word)


def translate(text):
    """
    Translate a full string into Pig Latin by applying the
    LEGO‑style word transformation to each individual word.
    """
    words = text.split()
    return " ".join(_translate_word(word) for word in words)
