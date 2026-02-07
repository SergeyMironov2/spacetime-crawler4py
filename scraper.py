from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urldefrag
import re

# tracking unique urls
unique_url_set = set()

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content

    if resp.status != 200:
        return []

    #
    page_as_neater_object = BeautifulSoup(resp.raw_response.content, "lxml")
    current_url = resp.url
    next_urls_absolute = []

    # *source*: originally from chatgpt (supposedly 
    #      allowed by ed post #49) but later 
    #      refactored and tweaked by Sergey M.
    for anchor_tag in page_as_neater_object.find_all("a", href=True):
        next_url_relative = anchor_tag["href"]
        next_url_absolute = urljoin(current_url, next_url_relative)
        if is_valid(next_url_absolute):
            next_urls_absolute.append(next_url_absolute)

            # tracking unique urls
            url_with_fragment = next_url_absolute
            url_without_fragment, fragment = urldefrag(url_with_fragment)
            unique_url_set.add(url_without_fragment) # preventing duplicate entries auto-handled by "set" data structure

    #
    print("**")
    print("number of unique urls: " + str(len(unique_url_set)))
    print("**")
    
    return next_urls_absolute
        

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        
        # filter hostname to acceptable list - *my partner*
        acceptable_hostname_suffixes = ['.ics.uci.edu', '.cs.uci.edu', '.informatics.uci.edu', '.stat.uci.edu']
        acceptable = False
        for hostname_suffix in acceptable_hostname_suffixes:
            if parsed.hostname[-len(hostname_suffix):] == hostname_suffix:
                acceptable = True
                break
        if not acceptable:
            return False

        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
