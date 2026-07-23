#! list[]
credit_scores = [740, 680, 720, 690, 710]
# credit_scores[0]= 750
# print(credit_scores)
# print(f"Credit score: {credit_scores[1]}")
credit_scores2: list[int] = []
credit_scores2.append(750)
print(f"Credit score: {credit_scores2[0]}")

user_input = "-final champion"
user_input = user_input.replace("-final", "Barcelona")
print(user_input)

raw_credit_input = "   \t  Alejandro Moj\u00c3\u00adca  |  555 - 01 - 9999   \t"
raw_credit_input = raw_credit_input.encode("latin-1").decode("utf-8")
print(f"Raw Input: {raw_credit_input}")
raw_credit_input = raw_credit_input.strip()  # Remove leading/trailing whitespace
print(f"Trimmed Input: {raw_credit_input}")
