def recite(start_verse, end_verse):
    gifts = [
        ("first", "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves, "),
        ("third", "three French Hens, "),
        ("fourth", "four Calling Birds, "),
        ("fifth", "five Gold Rings, "),
        ("sixth", "six Geese-a-Laying, "),
        ("seventh", "seven Swans-a-Swimming, "),
        ("eighth", "eight Maids-a-Milking, "),
        ("ninth", "nine Ladies Dancing, "),
        ("tenth", "ten Lords-a-Leaping, "),
        ("eleventh", "eleven Pipers Piping, "),
        ("twelfth", "twelve Drummers Drumming, ")
    ]

    verses = []

    for verse in range(start_verse, end_verse + 1):
        first_line = f"On the {gifts[verse - 1][0]} day of Christmas my true love gave to me: "

        parts = []
        for index in range(verse - 1, -1, -1):
            if index == 0 and verse > 1:
                parts.append("and " + gifts[0][1])
            else:
                parts.append(gifts[index][1])

        lines = first_line + "".join(parts)
        verses.append(lines)

    return verses
