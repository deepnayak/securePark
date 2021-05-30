def get_bigrams(string):
    """
    Take a string and return a list of bigrams.
    """
    s = string.lower()
    return [s[i:i+2] for i in list(range(len(s) - 1))]

def string_similarity(str1, str2):
    """
    Perform bigram comparison between two strings
    and return a percentage match in decimal form.
    """
    pairs1 = get_bigrams(str1)
    pairs2 = get_bigrams(str2)
    union  = len(pairs1) + len(pairs2)
    hit_count = 0
    for x in pairs1:
        for y in pairs2:
            if x == y:
                hit_count += 1
                break
    return (2.0 * hit_count) / union

if __name__ == "__main__":
    """
    Run a test using the example taken from:
    http://www.catalysoft.com/articles/StrikeAMatch.html
    """
    w1 = 'Healed'
    words = ['Heard', 'Healthy', 'Help', 'Herded', 'Sealed', 'Sold']

    for w2 in words:
        print('Healed --- ' + w2)
        print(string_similarity(w1, w2))
        print()