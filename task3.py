import pandas as pd
usernames = pd.Series([' sanjana ', 'anju', ' Anita ', 'Anuja'])
cleaned = usernames.str.strip()
cleaned = cleaned.str.lower()

contains_a = cleaned.str.contains('a')
print("Cleaned Usernames:\n")
print(cleaned)