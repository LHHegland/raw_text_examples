''' Examples of raw text versus processed text. 
    See https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

    REGEX NOTE from https://docs.python.org/3/library/re.html
    "Regular expressions use the backslash character ('\') to indicate
    special forms or to allow special characters to be used without
    invoking their special meaning. This collides with Python’s usage
    of the same character for the same purpose in string literals;
    for example, to match a literal backslash, one might have to
    write '\\\\' as the pattern string, because the regular expression
    must be \\, and each backslash must be expressed as \\ inside a
    regular Python string literal. Also, any invalid escape sequences
    in Python’s usage of the backslash in string literals now generate
    a SyntaxWarning (i.e. Python 3.12+) and in the future this will
    become a SyntaxError. This behaviour will happen even if it is a
    valid escape sequence for a regular expression.

    The solution is to use Python’s raw string notation for regular
    expression patterns; backslashes are not handled in any special way in
    a string literal prefixed with 'r'. So r"\n" is a two-character string
    containing '\' and 'n', while "\n" is a one-character string containing
    a newline. Patterns should be expressed in Python code using raw string
    notation.
'''

examples = []
expected_results = []

examples.append('This is a line of processed text.\nThis is another line of text.')
examples.append(r'This is a line of raw text.\nThis is another line of text.')

examples.append(r'D:\path\to\dir\filename.ext (raw)')
examples.append('D:\path\to\dir\filename.ext (raw)') # SyntaxError: invalid escape sequence (\p) in string literal
                                                     # and interprets \t as tab and \f as form feed
examples.append('D:\\path\\to\\dir\\filename.ext (processed)')

examples.append(r'\A(.+)[.]+page[ ]\d+') # e.g.: chapter title.........page 34
examples.append('\A(.+)[.]+page[ ]\d+')  # -> SyntaxError: invalid escape sequences (\A and \d) in string literal
examples.append('\\A(.+)[.]+page[ ]\\d+')

for index in range(len(examples)):
    print(f'example #{index}: {examples[index]}\n')



import re

string_to_search = 'Everything Works Well.............page 47'
pattern_example1 = re.compile(r'\A([^.]+(?=[.]+))([.]+page )(\d+)')
pattern_example2 = re.compile('\A([^.]+(?=[.]+))([.]+page )(\d+)') # -> SyntaxError: invalid escape sequences (\A and \d) in string literal
pattern_example3 = re.compile('\\A([^.]+(?=[.]+))([.]+page )(\\d+)')

print(f'string_to_search: {string_to_search}\n')
print(f'example regex #1: {pattern_example1} -> {pattern_example1.findall(string_to_search)}\n')
print(f'example regex #3: {pattern_example3} -> {pattern_example3.findall(string_to_search)}\n')