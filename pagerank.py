import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    pages = dict()

    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    prob_distribution = {}
    num_pages = len(corpus)
    num_links = len(corpus[page])

    if num_links == 0:
        for page_name in corpus:
            prob_distribution[page_name] = 1 / num_pages
    else:
        for page_name in corpus:
            prob_distribution[page_name] = (1 - damping_factor) / num_pages

        for linked_page in corpus[page]:
            prob_distribution[linked_page] += damping_factor / num_links

    return prob_distribution


def sample_pagerank(corpus, damping_factor, n):
    page_ranks = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))

    for _ in range(n):
        page_ranks[current_page] += 1
        probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(probabilities.keys()), weights=probabilities.values())[0]

    for page in page_ranks:
        page_ranks[page] /= n

    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    num_pages = len(corpus)
    init_rank = 1 / num_pages
    new_ranks = {page: init_rank for page in corpus}
    iterating = True

    while iterating:
        max_diff = 0
        for page in corpus:
            prev_rank = new_ranks[page]
            new_rank = (1 - damping_factor) / num_pages
            for possible_page, linked_pages in corpus.items():
                if page in linked_pages:
                    num_links = len(linked_pages)
                    new_rank += damping_factor * new_ranks[possible_page] / num_links
            new_ranks[page] = new_rank
            max_diff = max(max_diff, abs(new_rank - prev_rank))
        if max_diff < 0.001:
            iterating = False

    return new_ranks


if __name__ == "__main__":
    main()

