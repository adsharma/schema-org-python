"""Lazy loading for schema_models.

Importing ``schema_models`` (or any submodule) must NOT import all ~900
model modules: each module only needs its real dependency closure.
Names accessed as ``schema_models.X`` are resolved on demand via a single
PEP 562 ``__getattr__`` driven by the generated static map in
``_registry.py``.

``validator()`` needs forward refs (e.g. ``"Person"``) resolved. The
rebuild machinery lives in ``fquery.pydantic`` (which owns the
``__pydantic_namespace__`` hook); this package only supplies domain data:
the generated static transitive closures in ``_namespaces.py``. The first
``validator()`` call for a model bulk-imports its closure and rebuilds
exactly once; pydantic caches the result, so later calls pay nothing.
"""

import importlib

from schema_models._namespaces import _NAMESPACES
from schema_models._registry import _MODULE_FOR
from schema_models.thing import Thing

__all__ = sorted(_MODULE_FOR)


def __getattr__(name):
    try:
        mod = _MODULE_FOR[name]
    except KeyError:
        raise AttributeError(f"module 'schema_models' has no attribute {name!r}")
    return getattr(importlib.import_module(f"schema_models.{mod}"), name)


def _namespace_for(cls):
    """fquery namespace hook: bulk-import ``cls``'s static closure."""
    ns = {}
    for name in _NAMESPACES.get(cls.__name__, ()):
        if name not in ns and name in _MODULE_FOR:
            try:
                ns[name] = getattr(
                    importlib.import_module(f"schema_models.{_MODULE_FOR[name]}"),
                    name,
                )
            except ImportError:
                pass
    return ns


# All models descend from Thing, so setting the hook once covers every
# subclass via inheritance (fquery only sets the attribute when a class
# passes its own ``namespace=``, otherwise it is inherited).
Thing.__pydantic_namespace__ = _namespace_for
