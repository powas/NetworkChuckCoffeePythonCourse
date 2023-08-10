supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Cristal Lake", 404, 95.5, 10, False]

supplies.extend(["toilet paper", "bidet"])

print("Este elemento acaba de ser eliminado " + supplies.pop(0))

supplies.pop(0)

print(supplies)