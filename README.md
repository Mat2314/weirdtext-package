# Weirdtext
It is a python script to encode and decode messages to a weird form of the text. 

##Endcoder

Encoder is encoding given plaintext to a weirdtext form and returns tuple containing
- encoded text
- list of sorted original words from the plaintext

## Decoder
Decoder decodes given weirdtext to original version. It returns a string which is the final decoded value.

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