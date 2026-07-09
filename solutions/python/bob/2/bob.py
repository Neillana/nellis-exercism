"""
This approach feels more natural to me, since SQL was the first language I learned.
"""


def _is_silence(hey_bob):
    return hey_bob.strip() == ""


def _contains_letter(hey_bob):
    return any(char.isalpha() for char in hey_bob)


def _is_question(hey_bob):
    hey_bob = hey_bob.strip()
    return hey_bob.endswith("?")


def _is_yelling(hey_bob):
    hey_bob = hey_bob.strip()
    return _contains_letter(hey_bob) and hey_bob == hey_bob.upper()


def response(hey_bob):
    silence = _is_silence(hey_bob)
    yelling = _is_yelling(hey_bob)
    question = _is_question(hey_bob)

    match (silence, yelling, question):
        case (True, _, _):
            return "Fine. Be that way!"
        case (_, True, True):
            return "Calm down, I know what I'm doing!"
        case (_, True, False):
            return "Whoa, chill out!"
        case (_, False, True):
            return "Sure."
        case _:
            return "Whatever."
