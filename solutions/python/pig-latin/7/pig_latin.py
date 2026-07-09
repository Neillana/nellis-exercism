"""
Translate English words into Pig Latin by treating regex-captured word parts.

The module models each Pig Latin rule as a combination of a regex pattern
that decomposes a word into LEGO bricks (capturing groups) and a
transformation function that rearranges these bricks into their Pig Latin
configuration. The RULES list acts as a pipeline: the first pattern that
fully matches a word determines which bricks are extracted and how they are
snapped together to form the final output. Sentence translation is achieved
by applying this LEGO-style assembly process to each word independently.
"""

import re


def _apply_vowel(word_match):
    """Transform a vowel-starting word using LEGO-style Pig Latin.

    The entire word is treated as a single LEGO brick (group 0) and
    simply extended by attaching the 'ay' brick at the end.
    """
    return word_match.group(0) + "ay"


def _apply_consonant(word_match):
    """Transform a consonant-starting word using LEGO-style Pig Latin.

    The regex splits the word into two LEGO bricks: the leading
    consonant cluster (group 1) and the remaining word (group 2).
    The bricks are rearranged by snapping group 2 in front of group 1,
    and the 'ay' brick is attached at the end.
    """
    return word_match.group(2) + word_match.group(1) + "ay"


RULES = [
    (re.compile(r"(?:[aeiou]|xr|yt)(.*)"), _apply_vowel),
    (re.compile(r"([^aeiou]*qu)(.*)"), _apply_consonant),
    (re.compile(r"([^aeiou]+)(y.*)"), _apply_consonant),
    (re.compile(r"([^aeiou]+)(.*)"), _apply_consonant),
]


def _translate_word(word):
    """Translate a single word into Pig Latin using LEGO-style rules.

    Each regex pattern defines how the word is decomposed into LEGO
    bricks. The first matching rule determines which bricks are
    extracted and how they are rearranged by the corresponding
    transformation function.
    """
    for pattern, transform in RULES:
        if word_match := re.fullmatch(pattern, word):
            return transform(word_match)
    raise ValueError(
        f"No Pig Latin rule matched for word: {word!r}. "
        "This indicates an incomplete RULES pipeline."
    )


def translate(text):
    """Translate a full sentence into Pig Latin using LEGO-style word assembly.

    Each word is independently decomposed into LEGO bricks according
    to the Pig Latin rules, transformed, and then reassembled into a
    space-separated output string.
    """
    return " ".join(_translate_word(word) for word in text.split())
