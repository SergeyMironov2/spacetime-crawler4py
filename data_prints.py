import globals

# report part 1
def print_unique_page_count():
    unique_page_count = 0
    for subdomain, non_fragment_dict in globals.l0_search_space_l1_subdomain_l2_non_fragment_unique_l3_fragment_unique.items():
        for non_fragment_url, fragment_set in non_fragment_dict.items():
            unique_page_count += len(fragment_set)  # count all URLs with unique fragments
    print("Number of unique pages (ignoring differences in fragments):")
    print("\t" + str(unique_page_count))


# report part 2
def print_longest_page_by_words():
    url, count = globals.non_unique_url_and_max_word_count
    print("Longest page by words:")
    print("\tURL:", url)
    print("\tWord count: " + str(count))


# report part 3
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
    for subdomain in sorted(globals.l0_search_space_l1_subdomain_l2_non_fragment_unique_l3_fragment_unique.keys()):
        non_fragment_dict = globals.l0_search_space_l1_subdomain_l2_non_fragment_unique_l3_fragment_unique[subdomain]
        total_unique_pages = sum(len(fragment_set) for fragment_set in non_fragment_dict.values())
        print(f"\t{subdomain}, {total_unique_pages}")