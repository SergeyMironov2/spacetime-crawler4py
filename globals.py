# **
# global variable 1:
# 
# structure:
# - dict of:
#      - key: subdomain
#      - value: dict of:
#           - key: unique page (not counting fragment)
#           - value: set of:
#                - unique page (counting fragment)
# 
# purpose:
# - report part #1
# - report part #4
# - avoiding traps (because the number of times a unique page has been visited could be compared to a threshold, and that could be a form of trap avoidance).
# 
l0_search_space_l1_subdomain_l2_non_fragment_unique_l3_fragment_unique = {}

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
stop_words = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
    "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during",
    "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't",
    "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
    "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i",
    "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's",
    "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself",
    "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
    "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such",
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves",
    "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
    "they've", "this", "those", "through", "to", "too", "under", "until", "up",
    "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
    "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
    "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would",
    "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
}

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
# - tuple of:
#      - 0: non_unique_url
#      - 1: max_word_count
# 
# purpose:
# - report part #2
# 
non_unique_url_and_max_word_count = ("", -1)

# **
# global variable 5:
# 
# structure:
# - unique page max visit count (just an int)
# 
# purpose:
# - trap detection
# 
unique_page_max_visit_count = 10