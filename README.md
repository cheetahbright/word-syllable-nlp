# word-syllable-nlp

Utilities and experiments for computing basic readability statistics.

## Overview

The project provides a lightweight wrapper around the `readcalc` library
to calculate a handful of traditional readability metrics.  In addition
to the core code, the repository contains exploratory scripts and the
official Dale–Chall word list used to identify difficult vocabulary.

## Project layout

- `readability_calculator.py` – core module exposing the `Text` class for
  computing statistics and readability scores such as the Bormuth grade
  level and Degrees of Reading Power (DRP).
- `dalechallwords.py` – Python set of the 3,000 common words defined by
  the Dale–Chall readability formula.
- `mt_eda1.py`, `open-txt-file.py` – exploratory data-analysis scripts
  kept for reference.
- `tests/` – unit tests for the core module.

## Usage

```python
from readability_calculator import Text
from readcalc import readcalc

sample = "The quick brown fox jumps over the lazy dog."
calc = readcalc.ReadCalc(text=sample)
stats = Text(calc)
print(stats.get_DRP_units(calc))
```

## Development

Run the test suite with:

```bash
pytest
```

## License

Distributed under the terms of the MIT license.  See `LICENSE` for
details.

