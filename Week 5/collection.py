# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889}

for author, date in authors.items():
    print ("%s died in %d." %(author, date))


"""
Errors caused by:

Line 12:
1. authrs is misspelled compared to authors used later: Name Error
2. The years are Strings which causes an error on Line 19: Type Error
3. No closing statement "}" for dictionary :Syntax Error

Line 18:
1. author date is missing a comma between author and date: Syntax Error
2. authors.items{} uses curly braces instead of parentheses: Syntax Error

Line 19:
1. The print s% and d% syntax is wrong: Syntax Error
2. authors refers to the entire dictionary instead of the individual author variable: Logic Error
3. %d expects an integer, but the dates in the dictionary are strings: Type Error
4. Date uses a capital letter, but the loop variable is date: Name Error
"""