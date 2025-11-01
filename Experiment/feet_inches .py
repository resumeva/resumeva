from Experiment.convert import convert
from Experiment.parses import parse

feet_inches = input('Enter feet and inches:')

parse(feet_inches)
result = (convert(feet_inches))


if result < 1:
    print('Kid is too short')

else:
    print("He can go to other palce")