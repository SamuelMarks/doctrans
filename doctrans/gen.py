"""
Functionality to generate classes, functions, and/or argparse functions from the input mapping
"""

import ast
from ast import Assign, FunctionDef, Import, ImportFrom, List, Load, Module, Name, Store
from inspect import getfile, isfunction
from itertools import chain
from operator import itemgetter
from os import path

from doctrans import emit, parse
from doctrans.ast_utils import get_at_root, maybe_type_comment, set_value
from doctrans.pure_utils import get_module
from doctrans.source_transformer import to_code


def gen(
    name_tpl,
    input_mapping,
    type_,
    output_filename,
    prepend=None,
    imports_from_file=None,
    emit_call=False,
    emit_default_doc=True,
    decorator_list=None,
):
    """
    Generate classes, functions, and/or argparse functions from the input mapping

    :param name_tpl: Template for the name, e.g., `{name}Config`.
    :type name_tpl: ```str```

    :param input_mapping: Import location of dictionary/mapping/2-tuple collection.
    :type input_mapping: ```str```

    :param type_: What type to generate.
    :type type_: ```Literal["argparse", "class", "function"]```

    :param output_filename: Output file to write to
    :type output_filename: ```str```

    :param prepend: Prepend file with this. Use '\n' for newlines.
    :type prepend: ```Optional[str]```

    :param imports_from_file: Extract imports from file and append to `output_file`.
        If module or other symbol path given, resolve file then use it.
    :type imports_from_file: ```Optional[str]```

    :param emit_call: Whether to emit a `__call__` method from the `_internal` IR subdict
    :type emit_call: ```bool```

    :param emit_default_doc: Whether help/docstring should include 'With default' text
    :type emit_default_doc: ```bool```

    :param decorator_list: List of decorators
    :type decorator_list: ```Optional[Union[List[Str], List[]]]```
    """
    extra_symbols = {}
    if imports_from_file is None:
        imports = ""
    else:
        if prepend:
            prepend_imports = get_at_root(
                ast.parse(prepend.strip()), (Import, ImportFrom)
            )
            eval(
                compile(
                    Module(body=prepend_imports, stmt=None, type_ignores=[]),
                    filename="<string>",
                    mode="exec",
                ),
                extra_symbols,
            )
            # This leaks to the global scope
            globals().update(extra_symbols)
        with open(
            imports_from_file
            if path.isfile(imports_from_file)
            else getfile(get_module(imports_from_file, extra_symbols=extra_symbols)),
            "rt",
        ) as f:
            imports = "".join(
                map(to_code, get_at_root(ast.parse(f.read()), (Import, ImportFrom)))
            )

    module_path, _, symbol_name = input_mapping.rpartition(".")
    input_mapping = getattr(
        get_module(module_path, extra_symbols=extra_symbols), symbol_name
    )
    input_mapping_it = (
        input_mapping.items() if hasattr(input_mapping, "items") else input_mapping
    )

    global__all__ = []
    content = "{prepend}{imports}\n{functions_and_classes}\n{__all}".format(
        prepend="" if prepend is None else prepend,
        imports=imports,  # TODO: Optimize imports programmatically (rather than just with IDE or autoflake)
        functions_and_classes="\n\n".join(
            print("Generating: {!r}".format(name))
            or global__all__.append(name_tpl.format(name=name))
            or to_code(
                getattr(
                    emit,
                    type_.replace("class", "class_").replace(
                        "argparse", "argparse_function"
                    ),
                )(
                    (
                        lambda is_func: getattr(
                            parse,
                            "function" if is_func else "class_",
                        )(
                            obj,
                            **{} if is_func else {"merge_inner_function": "__init__"}
                        )
                    )(
                        isinstance(obj, FunctionDef) or isfunction(obj)
                    ),  # TODO: Figure out if it's a function or argparse function
                    emit_default_doc=emit_default_doc,
                    **(
                        lambda _name: {
                            "class": {
                                "class_name": _name,
                                "decorator_list": decorator_list,
                                "emit_call": emit_call,
                            },
                            "function": {
                                "function_name": _name,
                            },
                            "argparse": {"function_name": _name},
                        }[type_]
                    )(name_tpl.format(name=name))
                )
            )
            for name, obj in input_mapping_it
        ),
        __all=to_code(
            Assign(
                targets=[Name("__all__", Store())],
                value=List(
                    ctx=Load(),
                    elts=list(map(set_value, global__all__)),
                    expr=None,
                ),
                expr=None,
                lineno=None,
                **maybe_type_comment
            )
        ),
    )

    parsed_ast = ast.parse(content)
    # TODO: Shebang line first, then docstring, then imports
    doc_str = ast.get_docstring(parsed_ast)
    whole = tuple(
        map(
            lambda node: (node, None)
            if isinstance(node, (Import, ImportFrom))
            else (None, node),
            parsed_ast.body,
        )
    )

    parsed_ast.body = list(
        filter(
            None,
            chain.from_iterable(
                (
                    parsed_ast.body[:1] if doc_str else iter(()),
                    sorted(
                        map(itemgetter(0), whole),
                        key=lambda import_from: getattr(import_from, "module", None)
                        == "__future__",
                        reverse=True,
                    ),
                    map(itemgetter(1), whole[1:] if doc_str else whole),
                ),
            ),
        )
    )

    with open(output_filename, "a") as f:
        f.write(to_code(parsed_ast))