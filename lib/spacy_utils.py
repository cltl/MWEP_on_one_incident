import spacy

def load_models(lang_to_modelname, verbose=0):
    lang_to_model = {}
    for lang, modelname in lang_to_modelname.items():
        model = spacy.load(modelname)
        lang_to_model[lang] = model

        if verbose >= 2:
            print(f'loaded spacy model: {modelname}')
    return lang_to_model