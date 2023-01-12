import json

config_file = open('/Users/entropik/PycharmProjects/pythonproject/config.json')
data = json.load(config_file)
create_block_file1 = open(r'/Users/entropik/Downloads/create_block.json')
data1 = json.load(create_block_file1)


config_data = data['properties']
create_block_data = data1['properties']


def update_high_level():
    for i in config_data.keys():
        for j in create_block_data.keys():
            if i == j:
                if i == 'block_properties':
                    pass
                else:
                    for k in config_data[i]:
                        if k in create_block_data[j]:
                            create_block_data[j][k] = config_data[i][k]


def update_block_properties():
    if 'block_properties' not in config_data.keys():
        return
    if 'block_properties' not in create_block_data.keys():
        return
    config_block_properties_data = config_data['block_properties']['properties']
    create_block_block_properties_data = create_block_data['block_properties']['properties']
    for k in config_block_properties_data.keys():
        for l in create_block_block_properties_data.keys():
            if k == l:
                if k == 'options':
                    pass
                else:
                    for m in config_block_properties_data[k]:
                        if m in create_block_block_properties_data[l]:
                            create_block_block_properties_data[l][m] = config_block_properties_data[k][m]


def update_block_properties_options():
    if 'block_properties' not in config_data.keys():
        return
    if 'options' not in config_data['block_properties']['properties'].keys():
        return
    if 'block_properties' not in create_block_data.keys():
        return
    config_options_data = config_data['block_properties']['properties']['options']
    create_block_options_data = create_block_data['block_properties']['properties']['options']
    for a in config_options_data.keys():
        if a == 'items':
            for b in config_options_data[a]:
                if b == 'properties':
                    for c in config_options_data[a][b]:
                        for d in config_options_data[a][b][c]:
                            if d in create_block_options_data[a][b][c]:
                                create_block_options_data[a][b][c][d] = config_options_data[a][b][c][d]
        elif a in create_block_options_data.keys():
            create_block_options_data[a] = config_options_data[a]


def write_files():
    updated_file = open(r'/Users/entropik/Downloads/create_block.json', 'w')
    json.dump(data1, updated_file, indent=3)
    create_block_file1.close()


def main():
    update_high_level()
    update_block_properties()
    update_block_properties_options()
    write_files()


if __name__ == '__main__':
    main()