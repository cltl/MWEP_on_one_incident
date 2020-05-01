


def obtain_all_links(native_api_utils,
                     lang_to_wiki_title,
                     verbose=0):

    if verbose >= 2:
        print()

    all_links = set()
    num_links = 0
    for lang, wiki_title in lang_to_wiki_title.items():
        links = native_api_utils.obtain_primary_rt_links(wiki_title,
                                                         lang)

        if verbose >= 2:
            print(f'obtained {len(links)} for {lang}')

        all_links.update(links)
        num_links += len(links)

    if verbose >= 2:
        print(f'found total of {len(all_links)} Wikipedia source URIs')
        print(f'of which {num_links - len(all_links)} overlapping')

    return all_links
