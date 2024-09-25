pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
three_decimal_places = f'Pi to three decimal places is {pi :.3f}'
print(three_decimal_places)
#.3f indicates that it is a floating point value


# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
five_decimal_places = f'Pi to five decimal places is {pi :.5f}'
print(five_decimal_places)

score = 16

max_score = 26

score_as_decimal = score / max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
new_score = f'You scored {score_as_decimal}'
print(new_score)

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
new_percentage_score = f'You scored {score_as_decimal * 100 :.6f}%'
print(new_percentage_score)

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
new_two_decimal_score = f'You scored {score_as_decimal * 100 :.2f}%'
print(new_two_decimal_score)
#you don't need to manually * 100 to create a percentage, you can factor it into the f-string
print(f'You scored {score_as_decimal:.2%}')  #it doesn't need the f to denote floating point as we can use the percentage sign
#to denote the precision required for a percentage

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
new_no_decimal_score = f'You scored {score_as_decimal:.0%}'
print(new_no_decimal_score)