# Dictionary
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30,
        'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}

month = 'Jan'

# old style
print('%s has %d days' % (month, days[month]))

# format function
print('{0} has {1} days'.format(month, days[month]))

# using f-string
print(f'{month} has {days[month]} days')
