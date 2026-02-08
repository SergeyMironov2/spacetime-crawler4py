# report part 1
def print_unique_page_count():
    unique_page_count = 0
    for(subdomain, unique_pages_and_visit_counts in 
            k_subdomain_v_unique_pages_and_visit_counts):
        unique_page_count += 1
    print("Number of unique pages: ", unique_page_count)

# report part 2
def print_longest_page_by_words():
    url, count = non_unique_url_and_max_word_count
    print("Longest page by words:")
    print("\tURL:", url)
    print("\tWord count:", count)

# report part 3
def print_top_n_words(n = 50):

    # 
    print("Top", n, "words (ignoring stop words):")
    
    # 
    words_and_counts_sorted_dec_frequency = sorted(
        words_and_counts_no_stop_words.items(),
        key=lambda x: x[1],
        reverse=True
    )
    int i = 1
    for word, count in words_and_counts_sorted_dec_frequency[:n]:
        print("\t" + str(i) + ":" + word + ", " + count)
        i += 1

# report part 4
def print_uci_subdomains():
    
    # 
    print("Subdomains of uci.edu with unique page counts:")

    # 
    k_subdomain_v_unique_pages_and_visit_counts_sorted_by_sudomain_name =
        sorted(k_subdomain_v_unique_pages_and_visit_counts.items(), key=lambda x: x[0])
    for(subdomain, unique_page_and_visit_counts in
            k_subdomain_v_unique_pages_and_visit_counts_sorted_by_sudomain_name):
        print("\t" + subdomain + ", " + len(unique_page_and_visit_counts))