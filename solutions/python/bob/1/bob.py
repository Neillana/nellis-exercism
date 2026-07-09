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
    if _is_silence(hey_bob):
        return "Fine. Be that way!"
    if _is_question(hey_bob) and not _is_yelling(hey_bob):
        return "Sure."
    if _is_yelling(hey_bob) and not _is_question(hey_bob):
        return "Whoa, chill out!"
    if _is_yelling(hey_bob) and _is_question(hey_bob):
        return "Calm down, I know what I'm doing!"
    return "Whatever."
