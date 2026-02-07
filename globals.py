# **
# global variable 1:
# 
# structure:
# - dict of:
#      - key: subdomain
#      - value: dict of:
#           - key: unique page (so no fragment)
#           - value: number of time that page has 
#             been visited
# 
# purpose:
# - report part #1
# - report part #4
# - avoiding traps (because the number of times a unique page has been visited could be compared to a threshold, and that could be a form of trap avoidance).
# 
# comments on current name:
# - “k” and “v” used for “outer dict”, which is more
#   necessary for this structure because it’s a 
#   layered dictionary whereas for a single-layered 
#   dict one can get away with normal english
# 
k_subdomain_v_unique_pages_and_visit_counts = {}

# **
# global variable 2:
# 
# structure:
# - set of:
#      - stop word
# 
# purpose:
# - enabling global variable 3
# 
stop_words = set()

# **
# global variable 3:
# 
# structure:
# - dict of:
#      - key: word
#      - value: count
# 
# purpose:
# - report part #3
# 
words_and_counts_no_stop_words = {}

# **
# global variable 4:
# 
# structure:
# - max word count (just an int)
# 
# purpose:
# - report part #2
# 
max_word_count
