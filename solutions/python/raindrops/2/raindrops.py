def convert(number):
    raindrops = []
    
    if number % 3 == 0:
        raindrops.append("Pling")
    if number % 5 == 0:
        raindrops.append("Plang")
    if number % 7 == 0:
        raindrops.append("Plong")
    if not any(number % factor == 0 for factor in (3, 5, 7)):
        return str(number)
    
    return "".join(raindrops)
