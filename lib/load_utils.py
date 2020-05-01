import sys
import importlib


def load_python_module(module_path, module_name, verbose=0):
    """
    Load Python module from path

    :param str module_path: the path to the Python module
    :param str module_name: the name of the module to import

    :rtype: module
    :return: a Python module
    """
    sys.path.append(module_path)
    imported_module = importlib.import_module(module_name)
    sys.path.remove(module_path)
    assert module_path not in sys.path

    if verbose:
        print()
        print('imported module from')
        print('module path', module_path)
        print('module name', module_name)
        print('type imported module', type(imported_module))

    return imported_module


classes = load_python_module(module_path='../dep/multilingual-wiki-event-pipeline',
                                        module_name='classes',
                                        verbose=1)
native_api_utils = load_python_module(module_path='../dep/multilingual-wiki-event-pipeline',
                                        module_name='native_api_utils',
                                        verbose=1)
crawl_utils = load_python_module(module_path='../dep/multilingual-wiki-event-pipeline',
                                            module_name='crawl_utils',
                                            verbose=1)
spacy_to_naf = load_python_module(module_path='../dep/SpaCy-to-NAF',
                                            module_name='spacy_to_naf',
                                            verbose=1)
