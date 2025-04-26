"""
[
{ 駅名: {
    路線名: [
        {
            DIAGRAM
            RAILWAY
            DESTINATION
            NOTES
            DIRECTION
        },
        {
            DIAGRAM
            RAILWAY
            DESTINATION
            NOTES
            DIRECTION
        }
    ],
    路線名: [

    ]
  }
},
{ 駅名: {

  }
}
]
↓
{
	"type": "平日",
	"lineName": "名港線（金山行）",
	"stations": [
		{
			"ID": "E07",
			"name": "名古屋港",
			"time": ["5:30", "5:40", "5:48", "5:57", "6:09", "6:18", "6:32", "6:44", "6:51", "6:58", "7:05", "7:12", "7:19", "7:25", "7:32", "7:38", "7:44", "7:50", "7:56", "8:02", "8:08", "8:14", "8:20", "8:26", "8:32", "8:38", "8:44", "8:51", "8:58", "9:05", "9:13", "9:21", "9:29", "9:37", "9:47", "9:57", "10:07", "10:17", "10:27", "10:37", "10:47", "10:57", "11:07", "11:18", "11:27", "11:37", "11:47", "11:57", "12:07", "12:17", "12:27", "12:37", "12:47", "12:57", "13:07", "13:17", "13:27", "13:37", "13:47", "13:57", "14:07", "14:17", "14:27", "14:38", "14:47", "14:57", "15:07", "15:17", "15:27", "15:36", "15:39", "15:47", "15:55", "15:59", "16:05", "16:08", "16:16", "16:23", "16:30", "16:37", "16:44", "16:51", "16:58", "17:05", "17:12", "17:19", "17:26", "17:33", "17:40", "17:47", "17:54", "18:01", "18:08", "18:15", "18:22", "18:29", "18:36", "18:43", "18:50", "18:57", "19:04", "19:11", "19:18", "19:25", "19:32", "19:39", "19:46", "19:53", "20:00", "20:07", "20:14", "20:21", "20:28", "20:36", "20:43", "20:49", "20:56", "21:06", "21:12", "21:20", "21:30", "21:40", "21:46", "21:52", "22:02", "22:12", "22:22", "22:32", "22:42", "22:52", "23:02", "23:12", "23:22", "23:32", "23:42", "23:52"]
    	}
	]
}
"""
import json
import sys

station_name_to_CD = {
    '金山': 'M01',
    '東別院': 'M02',
    '上前津': 'M03',
    '矢場町': 'M04',
    '栄': 'M05',
    '久屋大通': 'M06',
    '名古屋城': 'M07',
    '名城公園': 'M08',
    '黒川': 'M09',
    '志賀本通': 'M10',
    '平安通': 'M11',
    '大曽根': 'M12',
    'ナゴヤドーム前矢田': 'M13',
    '砂田橋': 'M14',
    '茶屋ヶ坂': 'M15',
    '自由ヶ丘': 'M16',
    '本山': 'M17',
    '名古屋大学': 'M18',
    '八事日赤': 'M19',
    '八事': 'M20',
    '総合リハビリセンター': 'M21',
    '瑞穂運動場東': 'M22',
    '新瑞橋': 'M23',
    '妙音通': 'M24',
    '堀田': 'M25',
    '熱田神宮伝馬町': 'M26',
    '熱田神宮西': 'M27',
    '西高蔵': 'M28',

    '日比野': 'E02',
    '六番町': 'E03',
    '東海通': 'E04',
    '港区役所': 'E05',
    '築地口': 'E06',
    '名古屋港': 'E07',

    '高畑': 'H01',
    '八田': 'H02',
    '岩塚': 'H03',
    '中村公園': 'H04',
    '中村日赤': 'H05',
    '本陣': 'H06',
    '亀島': 'H07',
    '名古屋': 'H08',
    '伏見': 'H09',

    '新栄町': 'H11',
    '千種': 'H12',
    '今池': 'H13',
    '池下': 'H14',
    '覚王山': 'H15',

    '東山公園': 'H17',
    '星ヶ丘': 'H18',
    '一社': 'H19',
    '上社': 'H20',
    '本郷': 'H21',
    '藤が丘': 'H22',

    '上小田井': 'T01',
    '庄内緑地公園': 'T02',
    '庄内通': 'T03',
    '浄心': 'T04',
    '浅間町': 'T05',


    '大須観音': 'T08',
    '上前津': 'T09',
    '鶴舞': 'T10',
    '荒畑': 'T11',

    '川名': 'T13',
    'いりなか': 'T14',
    '八事': 'T15',
    '塩釜口': 'T16',
    '植田': 'T17',
    '原': 'T18',
    '平針': 'T19',
    '赤池': 'T20',

    '太閤通': 'S01',

    '国際センター': 'S03',
    '丸の内': 'S04',
    '久屋大通': 'S05',
    '高岳': 'S06',
    '車道': 'S07',

    '吹上': 'S09',
    '御器所': 'S10',
    '桜山': 'S11',
    '瑞穂区役所': 'S12',
    '瑞穂運動場西': 'S13',

    '桜本町': 'S15',
    '鶴里': 'S16',
    '野並': 'S17',
    '鳴子北': 'S18',
    '相生山': 'S19',
    '神沢': 'S20',
    '徳重': 'S21',

    '上飯田': 'K01'
}

dummy = {
        "DIAGRAM": {
            "土休日": {"0": []}, 
            "平日": {"0": []}
        },
        "DESTINATION": {
            "土休日": {"0": []}, 
            "平日": {"0": []}
            }, 
        "NOTES": {}, 
        "DIRECTION": ""
        }

def load_json_obj(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)

def get_station(json_obj, station_name):
    return [item.get(station_name) for item in json_obj if item.get(station_name) is not None][0]

def get_diagram(station_obj, rosen_name, direction):
    """
    direction: str 上り or 下り
    """
    rosen_obj = station_obj.get(rosen_name)
    diagram = [diagram for diagram in rosen_obj if diagram.get('DIRECTION') == direction]
    return diagram[0] if len(diagram) else dummy

def get_time_list(diagram_obj, day_type, func):
    """
    day_type: str
        平日 or 土休日

    func: Function
        時刻の接頭辞でフィルターする. funcがTrueのとき、その時刻を残す
        func(時刻) -> boolean
    """

    hours = diagram_obj['DIAGRAM'][day_type].keys() # キーは文字の数字で昇順とは限らない
    hours_sorted = sorted([24 + int(key) if int(key) < 5 else int(key) for key in hours]) # 0時、1時は24時、25時に変換する（4時は28時）
    
    diagram     = diagram_obj['DIAGRAM'][day_type]
    destination = diagram_obj['DESTINATION'][day_type]

    time_list = []

    for hour in hours_sorted:
        if hour == 24:
            min_list = diagram.get('0')
            dest_list = destination.get('0')
        elif hour == 25:
            min_list = diagram.get('1')
            dest_list = destination.get('1')
        elif hour == 26:
            min_list = diagram.get('2')
            dest_list = destination.get('2')
        elif hour == 27:
            min_list = diagram.get('3')
            dest_list = destination.get('3')
        elif hour == 28:
            min_list = diagram.get('4')
            dest_list = destination.get('4')
        else:
            min_list = diagram.get(str(hour))
            dest_list = destination.get(str(hour))

        if len(min_list) > 0: # 2023/9/16の桜通線のダイア改正で、運行していない時間も空のリストが含まれるようになったので、それを除外する
            dest_min_list = [n1 + n2 for n1, n2 in zip(dest_list, min_list)]

            filtered = [item for item in dest_min_list if func(item[0])] # func(item[0])がTrueの項目だけリストに残す
            hh_mm = [f'{hour}:{item[-2:]}' if len(item) > 2 else f'{hour}:{item}' for item in filtered]
            time_list.append(hh_mm)
    
    return [item for lst in time_list for item in lst]

def make_json_stations_value(station_name, time_list):
    """
    {
        "ID": "M01",
        "name: "金山",
        "time": ["5:53", "6:04", ...]
    }
    のような文字列を返す
    """
    ID = station_name_to_CD.get(station_name)
    time_str = ', '.join([f'"{item}"' for item in time_list])
    json_stations_value = f"""
\t\t\t"ID": "{ID}",
\t\t\t"name": "{station_name}",
\t\t\t"time": [{time_str}]
    """
    return '{' + json_stations_value + '\t}'

def make_json_str(json_obj, template):
    """
    {
        "type": "平日",
        "lineName": "名城線（左回り）",
        "stations": [
            {
                "ID": "M01",
                "name": "金山",
                "time": ["5:53", "6:04", "6:18", ...]
            },
            {
                "ID": "M02",
                "name": "東別院",
                "time": ["5:50", "6:01", ...]
            }
        ]
    }
    のような文字列を返す
    """
    rosen_name_list = template.keys()

    result = []
    for rosen_name in rosen_name_list:
        for key, value in template.get(rosen_name).items():
            # key = '平日・名城線（左回り）・上り'
            # value = ([駅名, 駅名, ...], func)
            splited = key.split('・')
            day_type = splited[0]
            line_name = splited[1]
            direction = splited[2]
            station_name_list = value[0]
            func = value[1]

            stations = []
            for station_name in station_name_list:
                station_obj = get_station(json_obj, station_name)
                diagram_obj = get_diagram(station_obj, rosen_name,direction)
                time_list = get_time_list(diagram_obj, day_type, func)
                stations_value = make_json_stations_value(station_name, time_list)
                stations.append(stations_value)
            stations_str = ',\n\t\t'.join(stations)

            if day_type == '土休日':
                day_type = '土日休'

            json_rosen_lines = [
                f'\n\t"type": "{day_type}",',
                f'\t"lineName": "{line_name}",'
            ]

            if line_name in ['名城線（右回り）', '名城線（左回り）']:
                json_rosen_lines.append('\t"loop": true,')

            json_rosen_lines.append(f'\t"stations": [\n\t\t{stations_str}\n\t]')

            json_rosen = "\n".join(json_rosen_lines)

            result.append(json_rosen)

    return '{' + '\n},\n{'.join(result) + '\n}'


def output_json(file_name, json_str):

    with open(file_name, 'w', encoding='utf_8') as f:
        f.write('[' + json_str + ']')
        print(f'{file_name}に書き込みました')

def filter_all(prefix):
    return True

def filter_meikou(prefix):
    return prefix == '港'

def filter_not_meikou(prefix):
    return prefix != '港'
    


if __name__ == '__main__':

    
    meijo = ['金山','東別院','上前津','矢場町','栄','久屋大通','名古屋城','名城公園','黒川','志賀本通','平安通','大曽根','ナゴヤドーム前矢田','砂田橋','茶屋ヶ坂','自由ヶ丘','本山','名古屋大学','八事日赤','八事','総合リハビリセンター','瑞穂運動場東','新瑞橋','妙音通','堀田','熱田神宮伝馬町','熱田神宮西','西高蔵']
    meijo_meikou = ['新瑞橋','瑞穂運動場東','総合リハビリセンター','八事','八事日赤','名古屋大学','本山','自由ヶ丘','茶屋ヶ坂','砂田橋','ナゴヤドーム前矢田','大曽根','平安通','志賀本通','黒川','名城公園','名古屋城','久屋大通','栄','矢場町','上前津','東別院','金山','日比野','六番町','東海通','港区役所','築地口','名古屋港']
    meikou = ['名古屋港','築地口','港区役所','東海通','六番町','日比野','金山']
 
    sakuradori = ['太閤通', '名古屋', '国際センター', '丸の内', '久屋大通', '高岳', '車道', '今池', '吹上', '御器所', '桜山', '瑞穂区役所', '瑞穂運動場西', '新瑞橋', '桜本町', '鶴里', '野並', '鳴子北', '相生山', '神沢', '徳重']
    higashiyama = ['高畑','八田','岩塚','中村公園','中村日赤','本陣','亀島','名古屋','伏見','栄','新栄町','千種','今池','池下','覚王山','本山','東山公園','星ヶ丘','一社','上社','本郷','藤が丘']
    tsurumai = ['上小田井','庄内緑地公園','庄内通','浄心','浅間町','丸の内','伏見','大須観音','上前津','鶴舞','荒畑','御器所','川名','いりなか','八事','塩釜口','植田','原','平針','赤池']
    kamiiida = ['上飯田','平安通']
    

    template = {
        '名城線・名港線': {
            '平日・名城線（右回り）・上り'    : (meijo, filter_all),
            '平日・名城線（左回り）・下り'    : (reversed(meijo), filter_not_meikou),
            '平日・名城線（名古屋港行）・下り': (meijo_meikou, filter_meikou),
            '平日・名港線（金山行）・上り'    : (meikou, filter_all),
            '平日・名港線（名古屋港行）・下り': (reversed(meikou), filter_all),
            '土休日・名城線（右回り）・上り'    : (meijo, filter_all),
            '土休日・名城線（左回り）・下り'    : (reversed(meijo), filter_not_meikou),
            '土休日・名城線（名古屋港行）・下り': (meijo_meikou, filter_meikou),
            '土休日・名港線（金山行）・上り'    : (meikou, filter_all),
            '土休日・名港線（名古屋港行）・下り': (reversed(meikou), filter_all)
        },
        '桜通線': {
            '平日・桜通線（徳重行）・下り': (sakuradori, filter_all),
            '平日・桜通線（太閤通行）・上り': (reversed(sakuradori), filter_all),
            '土休日・桜通線（徳重行）・下り': (sakuradori, filter_all),
            '土休日・桜通線（太閤通行）・上り': (reversed(sakuradori), filter_all)
        },
        '東山線': {
            '平日・東山線（藤が丘行）・下り': (higashiyama, filter_all),
            '平日・東山線（高畑行）・上り': (reversed(higashiyama), filter_all),
            '土休日・東山線（藤が丘行）・下り': (higashiyama, filter_all),
            '土休日・東山線（高畑行）・上り': (reversed(higashiyama), filter_all)
        },
        '鶴舞線': {
            '平日・鶴舞線（赤池行）・下り': (tsurumai, filter_all),
            '平日・鶴舞線（上小田井行）・上り': (reversed(tsurumai), filter_all),
            '土休日・鶴舞線（赤池行）・下り': (tsurumai, filter_all),
            '土休日・鶴舞線（上小田井行）・上り': (reversed(tsurumai), filter_all)
        },
        '上飯田線': {
            '平日・上飯田線（平安通行）・下り': (kamiiida, filter_all),
            '平日・上飯田線（上飯田行）・上り': (reversed(kamiiida), filter_all),
            '土休日・上飯田線（平安通行）・下り': (kamiiida, filter_all),
            '土休日・上飯田線（上飯田行）・上り': (reversed(kamiiida), filter_all)
        },
    }

    

    json_obj = load_json_obj('all.json')

    
    json_str = make_json_str(json_obj, template)

    output_json('timetable.json', json_str)






    
    