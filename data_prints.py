# on sourcing: we wrote the original code,
#      but after I (Sergey) made some structural
#      changes (reflecting the dropping of url 
#      fragments), I used ChatGPT to refactor it

import globals

# report part 1
def print_unique_page_count():
    unique_page_count = sum(
        len(url_set) for url_set in globals.k_subdomain_v_set_of_unique_pages.values()
    )
    print("Number of unique pages (ignoring differences in fragments):")
    print("\t" + str(unique_page_count))


# report part 2 (unchanged)
def print_longest_page_by_words():
    url, count = globals.non_unique_url_and_max_word_count
    print("Longest page by words:")
    print("\tURL:", url)
    print("\tWord count: " + str(count))


# report part 3 (unchanged)
def print_top_n_words(n=50):
    print("Top", n, "words (ignoring stop words):")
    sorted_words = sorted(
        globals.words_and_counts_no_stop_words.items(),
        key=lambda x: x[1],
        reverse=True
    )
    for i, (word, count) in enumerate(sorted_words[:n], start=1):
        print(f"\t{i}: {word}, {count}")


# report part 4
def print_uci_subdomains():
    print("Subdomains of uci.edu with unique page counts:")

    # sort subdomains alphabetically
    for subdomain in sorted(globals.k_subdomain_v_set_of_unique_pages.keys()):
        total_unique_pages = len(globals.k_subdomain_v_set_of_unique_pages[subdomain])
        print(f"\t{subdomain}, {total_unique_pages}")