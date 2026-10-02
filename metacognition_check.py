actual_score = 6
before_estimate = 9
after_estimate = 6

before_error = abs(before_estimate - actual_score)
after_error = abs(after_estimate - actual_score)

change = after_error - before_error

if change < 0:
    print("Improved")
elif change > 0:
    print("Deteriorated")
else:
    print("No change")