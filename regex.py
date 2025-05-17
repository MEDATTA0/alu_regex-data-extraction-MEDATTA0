import re

text = """
user@example.com
firstname.lastname@company.co.uk
https://www.example.com
https://subdomain.example.org/page

(123) 456-7890 123-456-7890
123.456.7890

1234 5678 9012 3456
1234-5678-9012-3456
 thisIsNot#hashtag
14:30 (24-hour format)
2:30 PM (12-hour format)

#example

#ThisIsAHashtag
"""

# 1. Email
email_regex = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'

# 2. URL
url_regex = r'https?://[^\s]+'

# 3. Phone number
phone_regex = r'(\(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'

# 4. Credit card
credit_card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b'

# 5 HashTags
hash_tag_regex = r"\s(#\w+)"

# ?: inside () means `don't capture the content of this bracket`
# 6 Time
time_regex = r"\b((?:0?[1-9]|1[0-2]):(?:[0-5]\d) (?:AM|PM)|(?:[01]?\d|2[0-3]):(?:[0-5]\d))\b"

emails = re.findall(email_regex, text)
urls = re.findall(url_regex, text)
phones = re.findall(phone_regex, text)
cards = re.findall(credit_card_regex, text)
hash_tags = re.findall(hash_tag_regex, text)
times = re.findall(time_regex, text)

print("Emails found:", emails)
print("URLs found:", urls)
print("Phone numbers found:", phones)
print("Credit card numbers found:", cards)
print("Hash Tags found:", hash_tags)
print("Times:", times)