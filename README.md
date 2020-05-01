# Tram Aanslag Utrecht

The goal of this repository is represent texts one Wikidata item.
### Prerequisites
Python 3.6 was used to create this project. It might work with older versions of Python.

## Python modules
A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

## Resources
Please run the following command to download the required resources:
```bash
bash install.sh
```

## How to use
Step 1. Edit **config/v0.json**
Step 2. Call for help:
```bash 
cd lib
python crawl_ref_texts_of_one_event_instance.py -h
```

Call the Python module with instructions from the command line.
    
## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
