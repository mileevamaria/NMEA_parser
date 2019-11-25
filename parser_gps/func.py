import pynmea2

def nmea(filepath):
    f = open(filepath, 'r', encoding='unicode_escape')
    text = f.read()
    text = text.split('\n')
    clean_data = []
    for line in text:
        try:
            msg = pynmea2.parse(line)
            clean_data.append(msg)
        except:
            pass

    data = []
    for item in clean_data:
        if item.sentence_type == 'GGA':
            dict_for_list = {}
            dict_for_list[item.sentence_type] = item
        elif item.sentence_type == 'RMC':
            dict_for_list[item.sentence_type] = item
            data.append(dict_for_list)
        else:
            dict_for_list[item.sentence_type] = item

    return data