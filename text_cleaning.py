import os


def read_files():
    file_directory = "./data"
    file_list = []

    for file in os.listdir(file_directory):
        if os.path.isfile(os.path.join(file_directory, file)):
            if file[-3:] == 'txt':
                file_list = file_list + [f'{file_directory}/{file}']

    return file_list


def process_files(file_name):
    output_line = ''
    output_list = []
    with open(file_name, "r", encoding='utf8', errors='ignore') as file:
        with open(f'{file_name[:-4]}_modified.txt', "w", encoding='utf8', errors='ignore') as out_file:
            for line in file:
                # print(f"{str(line[:10]) == 'Downloaded'}")
                # print(f"{str(line[:10])}: test: {line} \n\n")

                if str(line[:10]) == 'Downloaded' and output_line != '':
                    # print(f'true')
                    output_line = output_line + ', ' + line
                    output_list = output_list + [f'{output_line}\n']
                    # out_file.write(output_line + "\n")
                elif (',' in line) or ('IP' in line):

                    loc_arg_num = line.split('-')[0].count(',')
                    if loc_arg_num == 1:
                        line = line[:line.split('-')[0].rfind(',')]+', ' + line[line.split('-')[0].rfind(','):]
                    if loc_arg_num == 0:
                        line = ', ' + ', ' + line
                    output_line = line.strip("\n")
                else:
                    output_line = ''

    output_list_set = [*set(output_list)]
    print(f' {file_name}: items removed: {len(output_list) - len(output_list_set)} of {len(output_list)}')

    with open(f'{file_name[:-4]}_modified.txt', "w", encoding='utf8', errors='ignore') as out_file:
        for item in output_list_set:
            out_file.write(str(item))


if __name__ == "__main__":
    file_list = read_files()
    print(file_list)
    for file in file_list:
        process_files(file)
