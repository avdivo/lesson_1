from typing import List, Dict
import json


def remove_duplicates(list_dicts: List[Dict]) -> List[Dict]:
    """Удаляеение дубликатов из списка словарей"""
    list_dicts = list(set(map(json.dumps, list_dicts)))
    return list(map(json.loads, list_dicts))

a = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
print(remove_duplicates(a))