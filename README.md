# spacy-pos-evaluation

Evaluation of spaCy models across different POS tags

## spaCy models

The [spaCy models](https://spacy.io/models) are from version `>=3.2,<3.3`.

## Evaluation data

All of the evaluation data comes from the [Universal Dependencies project](https://universaldependencies.org/) through the [Hugging Face datasets API](https://huggingface.co/datasets/universal_dependencies), of which this uses data from [v2.7](https://universaldependencies.org/#download) of the Universal Dependencies project.

**Note** that when downloading the data through the Hugging Face datasets API it will be stored in the default cache directory: `~/.cache/huggingface/datasets/universal_dependencies`


## Requirements

Tested on Python 3.10

General requirements:

``` bash
pip install -r requirements.txt
```

## Development

Development requirements:

``` bash
pip install -r dev_requirements.txt
```

### Running linters

```
isort scripts/
flake8
mypy
```

