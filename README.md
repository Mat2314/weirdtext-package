# Weirdtext
It is a python script to encode and decode messages to a weird form of the text. 

## Package installation

To install weirdtext package go to root directory of a project and run the following command: `python3 -m pip install dist/weirdtext_tools-0.0.1-py3-none-any.whl`

## Endcoder

Encoder function: `def encode(plaintext: str) -> (str, list)`
Encoder is encoding given plaintext to a weirdtext form and returns tuple containing
- encoded text
- list of sorted original words from the plaintext

## Decoder

Decoder function: `def decode(weirdtext: str, original_words: list) -> str`
Decoder decodes given weirdtext to original version. It returns a string which is the final decoded value.

## Usage

To test the package functions run your python interpreter and type the following commands:

`from weirdtext import encoder`

`encoder.encode("This is Sparta!")`

This function will encode given message to some weirdtext.

To test decode function do the following:

`from weirdtext import decoder`

`decoder.decode('\n--weird--\nTihs is Stpraa!\n--weird--\n',['Sparta', 'This', 'is'])`

The decode function will analyze the weirdtext and decode it thanks to given list of original words. 

## Running tests
To run the tests run the following command:
`python3 -m unittest tests/*_tests.py`

## Error interpretation
While decoding message there might be 3 different versions of errors which might appear.

Error | Description |
------|-------------|
Weirdtext does not contain a magic separator | Given weirdtext does not have prefix and suffix equal to `\n--weird--\n`. To fix this error, simply add this magic separator at the beginning and the end of your message.
Words length in both versions differ | Built in validator checks if the amount of words in given weirdtext is equal to amount of words in given original words array. If not, the exception will be raised.
One of the first words length differ | Built in validator checks if up to 5 first words in given original words list and weirdtext have the same length. If any length of 2 compared words differ, the exception is raised. 
