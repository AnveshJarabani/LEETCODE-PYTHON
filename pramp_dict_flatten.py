"""
Flatten a Dictionary
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).
"""


def flatten_dictionary(dct):
    result = {}

    def bt(dct, key):
        if not isinstance(dct, dict):
            result[key] = dct
            return
        for sub_key, val in dct.items():
            if sub_key != "":
                if key != "":
                    bt(val, key + "." + sub_key)
                else:
                    bt(val, sub_key)
            else:
                bt(val, key)

    bt(dct, "")
    return result


dct = {"Key1": "1", "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": {"": "1"}}}}
print(flatten_dictionary(dct))
