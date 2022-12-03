# Python Exploit Pattern Tool
Vanilla python, testing above python 3.6.
## Installation

    $ pip install -e .

## Generate Pattern

    $ pattc -l 100
    aaaaabaacaadaaeaafaagaahaaiaajaakaalaamaanaaoaapaaqaaraasaataauaavaawaaxaayaazaaAaaBaaCaaDaaEaaFaaGa
    $ pattc -l 100 -b "aeiou"
    bbbbbcbbdbbfbbgbbhbbjbbkbblbbmbbnbbpbbqbbrbbsbbtbbvbbwbbxbbybbzbbAbbBbbCbbDbbEbbFbbGbbHbbIbbJbbKbbLb
    $ pattc -l 100 -o output

## Search for a pattern

    $ patts -l 100 -qc oaap
    pattern found with offset 44 in payload
    $ patts -l 100 -q 6f616170
    pattern found with offset 44 in payload