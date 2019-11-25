import pynmea2

def nmea_get(filepath):
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
            dict_for_list['type'] = item.sentence_type
            dict_for_list['time'] = item.timestamp
            dict_for_list['coordinates'] = '%02d°%07.4f′' % (item.latitude, item.latitude_minutes) + item.lat_dir + \
                                           ' / ' + '%02d°%07.4f′' % (item.longitude, item.longitude_minutes)  + item.lon_dir
            dict_for_list['altitude'] = item.altitude
        elif item.sentence_type == 'RMC':
            dict_for_list['speed'] = item.spd_over_grnd
            data.append(dict_for_list)

    return data


def nmea_filter(data, height, diff_height, speed, diff_speed):
    filtered_data = []

    for item in data:
        try:
            if ((diff_height == 'more') and (item['altitude'] >= float(height))) \
                    or ((diff_height == 'less') and (item['altitude'] <= float(height))):
                filtered_data.append(item)
        except ValueError:
            pass

        try:
            if ((diff_speed == 'more') and (item['speed'] < float(speed))) \
                    or ((diff_speed == 'less') and (item['speed'] > float(speed))):
                if item in filtered_data:
                    filtered_data.remove(item)
            else:
                if ((not height) and (not diff_height)):
                    filtered_data.append(item)
        except ValueError:
            pass

    return filtered_data
