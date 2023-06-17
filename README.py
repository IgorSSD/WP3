def merge_files(file_names, output_file):
    files = []
    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            file_info = {
                'name': file_name,
                'line_count': len(lines),
                'content': lines
            }
            files.append(file_info)

    sorted_files = sorted(files, key=lambda f: f['line_count'])

    with open(output_file, 'w') as output:
        for file_info in sorted_files:
            file_name = file_info['name']
            line_count = file_info['line_count']
            content = file_info['content']

            output.write(f'{file_name}\n')
            output.write(f'{line_count}\n')
            output.writelines(content)

file_names = ['1.txt','2.txt','3.txt' ]
output_file = 'result.txt'

merge_files(file_names, output_file)

