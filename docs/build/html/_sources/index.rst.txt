Welcome to weirdtext's documentation!
=====================================

Installation 
^^^^^^^^^^^^

To install weirdtext package run the following command::
    
    python3 -m pip install dist/weirdtext_tools-0.0.1-py3-none-any.whl

Functions
^^^^^^^^^

There are 2 main functions available:
Encode::

    def encode(plaintext: str) -> (str, list)

Decode::

    def decode(weirdtext: str, original_words: list) -> str

Usage
^^^^^

To see how it works run your python shell and import desired functions.
Let's see encoding: ::
    
    >> from weirdtext import encoder
    >> encoder.encode("This is Sparta!")
    ('\n--weird--\nTihs is Stpraa!\n--weird--\n', ['Sparta', 'This', 'is'])

Function `encode` returns a tuple with weirdtext and list of original words. Both of those arguments need to be passed to the opposite function - `decode`.::

    >> from weirdtext import decoder
    >> decoder.decode('\n--weird--\nTihs is Stpraa!\n--weird--\n',['Sparta', 'This', 'is']) 
    'This is Sparta!'

Decoder rebuilds the original message relying on list of original words.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
