"""OWLAPY

loosely based on OWL API

many help texts copied from OWL API [1]
OWLAPI licence: LGPL and Apache

[1] https://github.com/owlcs/owlapi
"""


__version__ = '0.0.7'

# the import order must be fixed otherwise there are circular import errors
import owlapy.model  # noqa: F401
