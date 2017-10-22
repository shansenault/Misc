def create_column(column_data):
    result = ''

    padding = len(max(column_data, key=len)) + 2
    
    # write header
    result += '+' + '-' * (padding + 1) + '+\n' 
    result += '|{:^{pad}}'.format(column_data[0], pad=padding + 1) + '|\n'
    result += '+' + '-' * (padding + 1) + '+\n' 

    # write rows
    for row in column_data[1:]:
        result += '| {:{pad}}'.format(row, pad=padding) + '|\n'

    # write footer
    result += '+' + '-' * (padding + 1) + '+' 

    return result

def parse_file(text_file):
    table = []
    lines = []

    with open(text_file, 'r') as f:
        for line in f:
            if line == '\n': # this requires the text file to end with a newline
                table.append(list(lines)) # pass by value instead of by reference - just copy lines
                lines[:] = []
            else:
                lines.append(line.replace('\n', ''))

    return table

column_list = []
result = ''

columns = parse_file('sample-table.txt')
longest_column_length = len(max(columns, key=len))

# any columns that are shorter than the longest column, add blank lines to make sure the height is uniform
for column in columns:
    if len(column) < longest_column_length:
        for x in range(0, longest_column_length - len(column)):
            column.append('')

# create columns
for column in columns:
    column_list.append(create_column(column))

# determine the height of the lines by finding how long vertically a column is by counting newline characters
max_lines = len(column_list[0].split('\n'))

# for every line that needs to be written
for x in range(0, max_lines):
    # go through each column
    for y in range(0, len(column_list)):
        # then get the line for the column and append it to the result
        # if the column isn't the first one, cut out the first character of each newline
        # to avoid duplicate characters
        if y != 0:
            result += column_list[y].split('\n')[x][1:]
        else:
            result += column_list[y].split('\n')[x]
    # once every x line of every column has been added to the result, add a newline and continue
    result += '\n'

print result

