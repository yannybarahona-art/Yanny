# --- EXPERIAN SIMULATED MESSY INPUT ---
# Problem 1: Name contains "MojÃ­ca" instead of "Mojíca" due to a UTF-8/Latin-1 mismatch.
# Problem 2: SSN has accidental spaces and a trailing tab '\t'.
raw_credit_input = (
    "   \t  Alejandro Moj\u00c3\u00adca  |  555 - 01 - 9999   \t"
)
#raw_credit_input = raw_credit_input.encode("latin-1").decode("utf-8")
#print(f"Raw Input: {raw_credit_input}")

#raw_credit_input = raw_credit_input.strip()  # Remove leading/trailing whitespace
#print(f"Trimmed Input: {raw_credit_input}")

credit_input_split = raw_credit_input.split("|")
#print(f"Split Data Split by '|': {credit_input_split}")

consumer=credit_input_split[0].encode("latin-1").decode("utf-8")
#print(f"Split Data Decoded: {consumer}")

consumer=consumer.strip()
#print(f"Split Data Consumer Trimmed: {consumer}")

ssn=credit_input_split[1].strip().replace(" ", "")
#print(f"Split Data SSN Trimmed: {ssn}")
ssn_masked=f"XXX-XX-{ssn[-4:]}"
#print(f"Split Data SSN Masked: {ssn_masked}")
account_status="verified"

bureau_fstring_record=f"STATUS: [{account_status.upper()}] | consumer: {consumer} | SSN: {ssn_masked}"

# --- STEP 1: Normalize the Encoding & Split Data ---
# Extracting the raw chunks first by splitting on the pipe '|'

# Fix the encoding artifact in the name ("MojÃ­ca" -> "Mojíca")

# --- STEP 2: Clean Leading/Trailing Whitespace & Formatting ---
# Strip the edges of the name


# Strip the SSN, and remove internal spaces to standardize the format


# --- STEP 3: Format into Standard Experian Bureau Output ---
# We mask the first 5 digits of the SSN for data security (FCRA compliance)

# --- VERIFY THE BUREAU DATA ---
print("--- Experian Data Ingestion Process ---")
print(f"Raw Input:      {raw_credit_input}")
print(f"Bureau Record:  {bureau_fstring_record}")

"""
EXPECTED OUTCOME:

--- Experian Data Ingestion Process ---
Raw Input:         	  Alejandro MojÃ­ca  |  555 - 01 - 9999   	
Bureau Record:  STATUS: [VERIFIED] | consumer: Alejandro Mojíca | SSN: XXX-XX-9999
"""