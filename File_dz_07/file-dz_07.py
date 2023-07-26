import os


def group_rename(file_name, count_number, expansion, expansion_end, diapasone=(0,1)):
    list_file = os.listdir()
    st, end = diapasone[0], diapasone[1]

    for num, file in enumerate(list_file, 1):
        t, exp = file.split('.')
        name = f" {t[st:end]}{file_name}{'0' * (count_number - len(str(count_number))) + str(num)}.{expansion_end}"
        if exp == expansion:
            os.rename(file, name)
            print(file)

group_rename('test' , 4, 'txt', 'csv', (1, 3))




