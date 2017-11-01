# table.py

Format plaintext or (eventually) CSVs into an ASCII table that expands/contracts to the input data. Expected input from plaintext files:

```
First line (first column header)
Second line (first row of first column)
Third line (second row of first column)
...
(newline)
Second line (second column header)
...
(final line must be a newline, this indcates the final column)
```

## Usage

In your terminal emulator of choice, within the directory of `table.py` and the input file:

`python table.py <sample-table.txt>`

## TODO

* Turn this into a proper CLI tool
* Add feature to customize the style of the separators
* Add support for CSVs

