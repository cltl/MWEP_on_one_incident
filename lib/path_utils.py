import os
from shutil import rmtree
from pathlib import Path

def create_output_dir(settings, verbose=0):
    out_dir = settings['paths']['out_dir']
    if os.path.exists(out_dir):
        rmtree(out_dir)
        if verbose:
            print(f'removed existing folder {out_dir}')

    if verbose:
        print(f'created output dir {out_dir}')

    out_dir = Path(out_dir)
    out_dir.mkdir()

    os.mkdir(settings['paths']['naf_dir'])
    os.mkdir(settings['paths']['bin_dir'])

    for language in settings['chosen_languages']:
        lang_dir = os.path.join(settings['paths']['naf_dir'],
                                language)
        os.mkdir(lang_dir)



