import re

text = "Umair Ashraf is learning and Python"

# result = re.findall("Python", text)
# print(result)

# pattern = r"\b\w{6}\b"
# matches = re.findall(pattern, text)
# print(matches)

# result = text.replace("Umair", "Ashraf")
# print(result)

# result = re.sub(r"\bUmair\b", "", text)
# print(result)

# text = "Umair Ashraf is learning and Python, UMAIR ASHRAF likes AI"

# result = re.sub(r"Umair", "", text, flags=re.IGNORECASE)
# print(result)
# result = re.sub(r"\s+", "", result).strip()
# print(result)

pattern = "Umair"

matches = re.search(pattern,text)

print(matches)
if matches:
    print("Match found:", matches.group())
else:
    print("No match found")
