"""
Mocks for docstrings
"""

from copy import deepcopy

from doctrans.defaults_utils import remove_defaults_from_intermediate_repr

intermediate_repr = {
    "name": None,
    "type": "static",
    "doc": "Acquire from the official tensorflow_datasets model "
    "zoo, or the ophthalmology focussed ml-prepare "
    "library",
    "params": [
        {
            "default": '"mnist"',
            "doc": 'name of dataset. Defaults to "mnist"',
            "name": "dataset_name",
            "typ": "str",
        },
        {
            "default": '"~/tensorflow_datasets"',
            "doc": 'directory to look for models in. Defaults to "~/tensorflow_datasets"',
            "name": "tfds_dir",
            "typ": "Optional[str]",
        },
        {
            "default": '"np"',
            "doc": 'backend engine, e.g., `np` or `tf`. Defaults to "np"',
            "name": "K",
            "typ": "Literal['np', 'tf']",
        },
        {
            "doc": "Convert to numpy ndarrays",
            "name": "as_numpy",
            "typ": "Optional[bool]",
        },
        {
            "doc": "pass this as arguments to data_loader function",
            "name": "data_loader_kwargs",
            "typ": "dict",
        },
    ],
    "returns": {
        "name": "return_type",
        "doc": "Train and tests dataset splits. Defaults to (np.empty(0), np.empty(0))",
        "default": "(np.empty(0), np.empty(0))",
        "typ": "Union[Tuple[tf.data.Dataset, tf.data.Dataset], "
        "Tuple[np.ndarray, np.ndarray]]",
    },
}

docstring_str = """
Acquire from the official tensorflow_datasets model zoo, or the ophthalmology focussed ml-prepare library

:param dataset_name: name of dataset. Defaults to "mnist"
:type dataset_name: ```str```

:param tfds_dir: directory to look for models in. Defaults to "~/tensorflow_datasets"
:type tfds_dir: ```Optional[str]```

:param K: backend engine, e.g., `np` or `tf`. Defaults to "np"
:type K: ```Literal['np', 'tf']```

:param as_numpy: Convert to numpy ndarrays
:type as_numpy: ```Optional[bool]```

:param data_loader_kwargs: pass this as arguments to data_loader function
:type data_loader_kwargs: ```**data_loader_kwargs```

:return: Train and tests dataset splits. Defaults to (np.empty(0), np.empty(0))
:rtype: ```Union[Tuple[tf.data.Dataset, tf.data.Dataset], Tuple[np.ndarray, np.ndarray]]```
"""

docstring_google_str = """
Acquire from the official tensorflow_datasets model zoo, or the ophthalmology focussed ml-prepare library

Args:
  dataset_name (str): name of dataset. Defaults to "mnist"
  tfds_dir (Optional[str]): directory to look for models in. Defaults to "~/tensorflow_datasets"
  K (Literal['np', 'tf']): backend engine, e.g., `np` or `tf`. Defaults to "np"
  as_numpy (Optional[bool]): Convert to numpy ndarrays
  data_loader_kwargs (dict): pass this as arguments to data_loader function

Returns:
  Union[Tuple[tf.data.Dataset, tf.data.Dataset], Tuple[np.ndarray, np.ndarray]]:
   Train and tests dataset splits. Defaults to (np.empty(0), np.empty(0))
"""

# https://github.com/tensorflow/tensorflow/blob/7ad2723/tensorflow/python/keras/losses.py#L803-L840
docstring_google_tf_squared_hinge_str = """
Computes the squared hinge loss between `y_true` and `y_pred`.
`loss = square(maximum(1 - y_true * y_pred, 0))`
`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are
provided we will convert them to -1 or 1.
Standalone usage:
>>> y_true = [[0., 1.], [0., 0.]]
>>> y_pred = [[0.6, 0.4], [0.4, 0.6]]
>>> # Using 'auto'/'sum_over_batch_size' reduction type.
>>> h = tf.keras.losses.SquaredHinge()
>>> h(y_true, y_pred).numpy()
1.86
>>> # Calling with 'sample_weight'.
>>> h(y_true, y_pred, sample_weight=[1, 0]).numpy()
0.73
>>> # Using 'sum' reduction type.
>>> h = tf.keras.losses.SquaredHinge(
...     reduction=tf.keras.losses.Reduction.SUM)
>>> h(y_true, y_pred).numpy()
3.72
>>> # Using 'none' reduction type.
>>> h = tf.keras.losses.SquaredHinge(
...     reduction=tf.keras.losses.Reduction.NONE)
>>> h(y_true, y_pred).numpy()
array([1.46, 2.26], dtype=float32)
Usage with the `compile()` API:
```python
model.compile(optimizer='sgd', loss=tf.keras.losses.SquaredHinge())
```
"""

docstring_numpydoc_str = """
Acquire from the official tensorflow_datasets model zoo, or the ophthalmology focussed ml-prepare library

Parameters
----------
dataset_name : str
    name of dataset. Defaults to "mnist"
tfds_dir : Optional[str]
    directory to look for models in. Defaults to "~/tensorflow_datasets"
K : Literal['np', 'tf']
    backend engine, e.g., `np` or `tf`. Defaults to "np"
as_numpy : Optional[bool]
    Convert to numpy ndarrays
data_loader_kwargs : dict
    pass this as arguments to data_loader function

Returns
-------
Union[Tuple[tf.data.Dataset, tf.data.Dataset], Tuple[np.ndarray, np.ndarray]]
    Train and tests dataset splits. Defaults to (np.empty(0), np.empty(0))

"""

docstring_numpydoc_only_params_str = """
Parameters
----------
dataset_name : str
    name of dataset. Defaults to "mnist"
tfds_dir : Optional[str]
    directory to look for models in. Defaults to "~/tensorflow_datasets"
K : Literal['np', 'tf']
    backend engine, e.g., `np` or `tf`. Defaults to "np"
as_numpy : Optional[bool]
    Convert to numpy ndarrays
data_loader_kwargs : dict
    pass this as arguments to data_loader function
"""

docstring_numpydoc_only_returns_str = """
Returns
-------
Union[Tuple[tf.data.Dataset, tf.data.Dataset], Tuple[np.ndarray, np.ndarray]]
    Train and tests dataset splits. Defaults to (np.empty(0), np.empty(0))

"""

docstring_numpydoc_only_doc_str = """
Acquire from the official tensorflow_datasets model zoo, or the ophthalmology focussed ml-prepare library
"""

intermediate_repr_no_default_doc_or_prop = remove_defaults_from_intermediate_repr(
    deepcopy(intermediate_repr), emit_defaults=False
)

intermediate_repr_no_default_doc = {
    "name": None,
    "type": "static",
    "doc": "Acquire from the official tensorflow_datasets model "
    "zoo, or the ophthalmology focussed ml-prepare "
    "library",
    "params": [
        {
            "default": '"mnist"',
            "doc": "name of dataset.",
            "name": "dataset_name",
            "typ": "str",
        },
        {
            "default": '"~/tensorflow_datasets"',
            "doc": "directory to look for models in.",
            "name": "tfds_dir",
            "typ": "Optional[str]",
        },
        {
            "default": '"np"',
            "doc": "backend engine, e.g., `np` or `tf`.",
            "name": "K",
            "typ": "Literal['np', 'tf']",
        },
        {
            "doc": "Convert to numpy ndarrays",
            "name": "as_numpy",
            "typ": "Optional[bool]",
        },
        {
            "doc": "pass this as arguments to data_loader function",
            "name": "data_loader_kwargs",
            "typ": "dict",
        },
    ],
    "returns": {
        "default": "(np.empty(0), np.empty(0))",
        "doc": "Train and tests dataset splits.",
        "name": "return_type",
        "typ": "Union[Tuple[tf.data.Dataset, tf.data.Dataset], "
        "Tuple[np.ndarray, np.ndarray]]",
    },
}

intermediate_repr_extra_colons = {
    "name": None,
    "params": [
        {"doc": "Example: foo", "name": "dataset_name", "typ": "str"},
    ],
    "returns": None,
    "doc": "Some comment",
    "type": "static",
}

intermediate_repr_only_return_type = {
    "name": None,
    "type": "static",
    "doc": "Some comment",
    "params": [
        {
            "doc": "Example: foo",
            "name": "dataset_name",
        }
    ],
    "returns": {
        "doc": "Train and tests dataset splits.",
        "name": "return_type",
        "typ": "Union[Tuple[tf.data.Dataset, tf.data.Dataset], "
        "Tuple[np.ndarray, np.ndarray]]",
    },
}

docstring_str_no_default_doc = """
Acquire from the official tensorflow_datasets model zoo, or the ophthalmology focussed ml-prepare library

:param dataset_name: name of dataset.
:type dataset_name: ```str```

:param tfds_dir: directory to look for models in.
:type tfds_dir: ```Optional[str]```

:param K: backend engine, e.g., `np` or `tf`.
:type K: ```Literal['np', 'tf']```

:param as_numpy: Convert to numpy ndarrays
:type as_numpy: ```Optional[bool]```

:param data_loader_kwargs: pass this as arguments to data_loader function
:type data_loader_kwargs: ```**data_loader_kwargs```

:return: Train and tests dataset splits.
:rtype: ```Union[Tuple[tf.data.Dataset, tf.data.Dataset], Tuple[np.ndarray, np.ndarray]]```
"""

docstring_str_extra_colons = """
Some comment

:param dataset_name: Example: foo
:type dataset_name: ```str```
"""

docstring_str_only_return_type = """
Some comment

:param dataset_name: Example: foo

:return: Train and tests dataset splits.
:rtype: ```Union[Tuple[tf.data.Dataset, tf.data.Dataset], Tuple[np.ndarray, np.ndarray]]```
"""

__all__ = [
    "docstring_str",
    "docstring_str_extra_colons",
    "docstring_str_no_default_doc",
    "docstring_numpydoc_str",
    "docstring_numpydoc_only_params_str",
    "docstring_numpydoc_only_returns_str",
    "docstring_numpydoc_only_doc_str",
    "docstring_google_str",
    "intermediate_repr",
    "intermediate_repr_no_default_doc_or_prop",
    "intermediate_repr_no_default_doc",
]
