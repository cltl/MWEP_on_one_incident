"""
Crawl Wikipedia sources of one Wikidata item.

Usage:
  crawl_ref_texts_of_one_event_instance.py\
   --config_path=<config_path>
   --verbose=<verbose>

Options:
    --config_path=<config_path>
    --verbose=<verbose> 0 --> no stdout 1 --> general stdout 2 --> detailed stdout

Example:
    python crawl_ref_texts_of_one_event_instance.py\
     --config_path="../config/v0.json"\
      --verbose=2
"""
from docopt import docopt
import json
import os
import pickle
from datetime import datetime
import spacy_utils
import load_utils
import api_utils
import path_utils

arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

verbose = int(arguments['--verbose'])
settings = json.load(open(arguments['--config_path']))

# load relevant Python modules
from load_utils import classes, native_api_utils, crawl_utils, spacy_to_naf

# create output directory
path_utils.create_output_dir(settings, verbose=verbose)

# load relevant dictionaries
lang_to_model = spacy_utils.load_models(settings['spacy']['models'],
                                        verbose=verbose)

# Instantiate IncidentCollection and add one Incident
inc_coll_obj = classes.IncidentCollection(incident_type=settings['wikidata_item_info']['incident_type'],
                                          incident_type_uri=settings['wikidata_item_info']['incident_type_uri'],
                                          languages=settings['chosen_languages'])

inc_obj = classes.Incident(incident_type=settings['wikidata_item_info']['incident_type'],
                           wdt_id=settings['wikidata_item_info']['incident_uri'])
inc_coll_obj.incidents.append(inc_obj)

assert len(inc_coll_obj.incidents) == 1

# obtain set of URIs of primary reference texts
all_links = api_utils.obtain_all_links(native_api_utils,
                                       settings['lang_to_wiki_title'],
                                       verbose=verbose)

# crawl links
if verbose >= 5:
    all_links = list(all_links)[:5]

start, end = settings['newsplease']['num_chars_range']
num_chars_range = range(start, end)
url_to_info = crawl_utils.get_ref_text_obj_of_primary_reference_texts(urls=all_links,
                                                                      timeout=settings['newsplease']["timeout"],
                                                                      startswith=settings['newsplease']["startswith"],
                                                                      accepted_languages=settings['chosen_languages'],
                                                                      excluded_domains=settings['newsplease']['excluded_domains'],
                                                                      title_required=settings['newsplease']['title_required'],
                                                                      num_chars_range=num_chars_range,
                                                                      illegal_substrings=settings['newsplease']['illegal_substrings'],
                                                                      illegal_chars_in_title=settings['newsplease']['illegal_chars_in_title'],
                                                                      verbose=verbose)

# add ReferenceTexts
for url, ref_text_obj in url_to_info.items():
    inc_obj.reference_texts.append(ref_text_obj)

assert len(url_to_info) == len(inc_obj.reference_texts)

# process with spaCy
for ref_text_obj in inc_obj.reference_texts:
    dct = ref_text_obj.creation_date
    if dct is None:
        dct = datetime(1,1,1) # year 1 to indicate that we do not know!
    doc = spacy_to_naf.text_to_NAF(text=ref_text_obj.content,
                                   nlp=lang_to_model[ref_text_obj.language],
                                   dct=dct,
                                   layers=settings['spacy']['settings']['layers'],
                                   naf_version=settings['spacy']['settings']['naf_version'],
                                   replace_hidden_characters=settings['spacy']['settings']['replace_hidden_characters'],
                                   cdata=settings['spacy']['settings']['cdata'],
                                   title=ref_text_obj.name,
                                   uri=ref_text_obj.web_archive_uri,
                                   language=ref_text_obj.language,
                                   map_udpos2naf_pos=False)

    output_path = os.path.join(settings['paths']['naf_dir'],
                               ref_text_obj.language,
                               f'{ref_text_obj.name}.naf')

    print(output_path)
    spacy_to_naf.NAF_to_file(doc,
                             output_path)

# save inc_coll_obj to disk
bin_path = os.path.join(settings['paths']['bin_dir'],
                        f"{settings['wikidata_item_info']['incident_uri']}.bin")
with open(bin_path, 'wb') as outfile:
    pickle.dump(inc_coll_obj, outfile)
if verbose:
    print(f'saved IncidentCollection to {bin_path}')
