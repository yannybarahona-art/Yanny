import re

searcg_string = "the price is $100 dollars"
regex_pattern = r"\$\d{3}"
regex_match = re.search(regex_pattern, searcg_string)
if regex_match:
    print(f"Match found: {regex_match.group()}")

    search_string = "You can reach me at 555-123-1234 or at 255-789-7894"

    regex_pattern = r"\d{3}-\d{3}-\d{4}"
    regex_matches = re.findall(regex_pattern, search_string)
    if regex_matches:
        print(f"Matches found: {regex_matches}")

search_string = "Error at line 10. Error at line 60."
regex_match = r"Error"
# ?if match in re.finditer(regex_match, search_string):
# ?   print(f"Match found at position: {match.start()} - {match.end()}")

search_string = "4224 4224 4224 42241"
regex_pattern = r"\d{4}"
replacement_string = "****"
masked_string = re.sub(regex_pattern, replacement_string, search_string)
print(f"Masked String: {masked_string}")

search_string = "apples, oranges, bananas grapes! pears"
search_string.split(",")
regex_pattern = "[,;\s!]+"
fruits = re.split(regex_pattern, search_string)
print(f"Fruits: {fruits}")


# regex_pattern=re.compile(r"\d{3}-\d{3}-\d{4}")
