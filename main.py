svg_path = 'M42.7,193l28.8,0l17.6,-142.8l-43.4,0l-15.8,24.2l27.4,0z'

path_name = 'hourGlyph02'

separators = ['M', 'm', 'L', 'l', 'C', 'c', 'Z']

for identifier in separators:
    svg_path = svg_path.replace(identifier, 'XX' + identifier)

split_svg_string = svg_path.split('XX')
for index, string in enumerate(split_svg_string):
    split_svg_string[index] = split_svg_string[index].replace('XX', '')
    print(split_svg_string[index])

for command in split_svg_string:
    parsed_command = ''
    if 'M' in command:
        position = command.replace('M', '').replace(',', ', ').replace(',', 'f,')
        parsed_command = f'{path_name}.moveTo({position}f)'
    if 'C' in command:
        list_of_coords = command.replace('C', '').split(' ')
        for index, position in enumerate(list_of_coords):
            list_of_coords[index] = position.replace(',', ', ')
        parsed_command = f'{path_name}.cubicTo({list_of_coords})'
        parsed_command = str(parsed_command)\
            .replace('[', '')\
            .replace(']', '')\
            .replace("'", "")\
            .replace(', )', ')')\
            .replace(',', 'f,')\
            .replace(')', 'f)')
    if 'Z' in command:
        parsed_command = f'{path_name}.close()'
    print(parsed_command)

