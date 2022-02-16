from typing import Callable, Dict, Union

import datasets
from datasets import load_dataset
import fr_core_news_sm


def dataset_statistics(dataset: datasets.arrow_dataset.Dataset,
                       ) -> Dict[str, Union[str, int, float]]:
    statistics: Dict[str, Union[str, int, float]] = {}
    statistics['Universal Dependencies version'] = dataset.info.version
    statistics['Dataset Split'] = dataset.split
    statistics['Download Size'] = f'{dataset.info.download_size / (1024 ** 2):.2f} MB'
    statistics['Dataset Size'] = f'{dataset.info.size_in_bytes / (1024 ** 2):.2f} MB'
    statistics['Number of sentences'] = len(dataset)
    token_count = 0
    for sentence in dataset:
        token_count = len(sentence['tokens'])
    statistics['Number of tokens'] = token_count
    return statistics


dataset = load_dataset('universal_dependencies', 'fr_gsd', split='test')
assert isinstance(dataset, datasets.arrow_dataset.Dataset)
print(dataset_statistics(dataset))

upos_int_2_str: Callable[[int], str] = dataset.features['upos'].feature.int2str
for sentence in dataset:
    upos = upos_int_2_str(sentence['upos'])
    print(upos)
    text = sentence['text']
    nlp = fr_core_news_sm.load()
    output = nlp(text)
    print([token.pos_ for token in output])
    break
