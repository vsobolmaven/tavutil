# Public Domain (-) 2004-2011 The Tavutil Authors.
# See the Tavutil UNLICENSE file for details.

"""I/O Helper Utilities."""

from __future__ import absolute_import
import sys

from textwrap import TextWrapper
from six.moves import input

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

# ------------------------------------------------------------------------------
# Some Constants
# ------------------------------------------------------------------------------

# Colours -- dedicated to Saritah who loves pretty colours.
# The beautiful colours!

CODES = {

        'reset':'\x1b[0m',
        'black':'\x1b[30m',
         'blue':'\x1b[34;01m',
         'bold':'\x1b[01m',    # will differ in various terms
        'brown':'\x1b[33;06m',
     'darkblue':'\x1b[34;06m',
    'darkgreen':'\x1b[32;06m',
     'darkgrey':'\x1b[30;01m',
      'darkred':'\x1b[31;06m',
        'green':'\x1b[32;01m',
         'grey':'\x1b[37;06m',
      'magenta':'\x1b[35;01m',
       'purple':'\x1b[35;06m',
          'red':'\x1b[31;01m',
         'teal':'\x1b[36;06m',
    'turquoise':'\x1b[36;01m',
       'yellow':'\x1b[33;01m',
        'white':'\x1b[37;01m',
         'null':'',

    }

if sys.platform == 'win32':
    from collections import defaultdict
    CODES = defaultdict(str)

# ------------------------------------------------------------------------------
# Terminal Formatters
# ------------------------------------------------------------------------------

def wrap_text(text, maxwidth=80, leadpadding=0):
    """Wrap the given ``text`` into lines of specific length."""
    wrap = TextWrapper(width=maxwidth)
    if leadpadding:
        wrap.subsequent_indent = ' ' * leadpadding
    return wrap.fill(text)

def print_text(colour, text):
    """Return text in the specified colour."""
    return CODES[colour] + text + CODES['reset']

def print_reset():
    return CODES['reset']

def print_error(text):
    return print_text('darkred', '\n' + text)

def print_message(text, width=80, pad=0, col1='darkgrey', col2='red', footer=1):
    return (
        print_text(col1, '-' * width) + '\n' + 
        print_text(col2, wrap_text(text, width, pad)) + '\n' +
        (footer and print_text(col1, '-' * width))
        )

def print_query(
    text, default, extra='', options=[], width=80, pad=4,
    col1='darkgrey', col2='red'
    ):
    return input(
        print_message('%s ' % text, width, pad, col1, col2, footer='') + 
        extra + 
        print_text(col2, '\n    [') +
        default +
        print_text(col2, '] ')
        ) or default

def print_note(text, col1='green', col2='white', end='\n', start='\n'):
    return print_text(col1, '%s  * ' % start) + print_text(col2, text) + end

# ------------------------------------------------------------------------------
# /dev/null
# ------------------------------------------------------------------------------

class DevNull:
    """Provide a file-like interface emulating /dev/null."""

    def __call__(self, *args, **kwargs):
        pass

    def flush(self):
        pass

    def log(self, *args, **kwargs):
        pass

    def write(self, input):
        pass

DEVNULL = DevNull()

# ------------------------------------------------------------------------------
# Utility Classes
# ------------------------------------------------------------------------------

class IteratorParser:
    """A straightforward parser that lets you move backwards with ease."""

    def __init__(self, sequence):
        self.sequence = iter(sequence)
        self._store = []

    def __iter__(self):
        return self

    def push(self, value):
        self._store.append(value)

    def next(self):
        if self._store:
            return self._store.pop()
        else:
            return next(self.sequence)
