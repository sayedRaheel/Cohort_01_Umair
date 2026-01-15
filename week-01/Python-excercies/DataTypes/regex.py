import re

text = "Umair Ashraf is learning and Python"

result = re.findall("Python", text)
print(result)

pattern = r"\b\w{6}\b" # word with exactly 6 letters

matches = re.findall(pattern, text)
print(f'Match for the pattern: {matches}')
print(f'Number of matches: {len(matches)}')

print("----Replacing Strings----")
print("Original Text:", text)
result = text.replace("Umair", "Ashraf")
print("After replace:", result)

# Using regex to replace
print("----Replacing using regex----")
print("Original Text:", text)
result = re.sub(r"\bUmair\b", "", text)
print("After replace:", result)

text = "Umair Ashraf is learning and Python, UMAIR ASHRAF likes AI"
print("----Replacing using regex with flags----")
print("Original Text:", text)
result = re.sub(r"Umair", "", text, flags=re.IGNORECASE)
print("After replace:", result)
result = re.sub(r"\s+", "", result).strip()
print("After removing spaces:", result)

pattern = "Umair"
# using search to find first occurrence
matches = re.search(pattern,text)

print(matches)
if matches:
    print("Match found:", matches.group()) # prints the matched string
else:
    print("No match found")
