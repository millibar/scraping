import scrapy
import json
import re

station_id_dict = {
    40: '東別院',
    41: '上前津',
    42: '矢場町',
    43: '栄',
    44: '久屋大通',
    45: '名古屋城',
    46: '名城公園',
    47: '黒川',
    48: '志賀本通',
    49: '大曽根',
    24: 'ナゴヤドーム前矢田',
    25: '砂田橋',
    26: '茶屋ヶ坂',
    27: '自由ヶ丘',
    28: '本山',
    29: '名古屋大学',
    30: '八事日赤',
    31: '八事',
    32: '総合リハビリセンター',
    33: '瑞穂運動場東',
    34: '新瑞橋',
    35: '妙音通',
    36: '堀田',
    37: '熱田神宮伝馬町',
    38: '熱田神宮西',
    39: '西高蔵',
    23: '金山',
    22: '日比野',
    21: '六番町',
    20: '東海通',
    19: '港区役所',
    18: '築地口',
    17: '名古屋港',
    69: '高畑',
    68: '八田',
    67: '岩塚',
    66: '中村公園',
    65: '中村日赤',
    64: '本陣',
    63: '亀島',
    62: '名古屋',
    61: '伏見',
    60: '新栄町',
    59: '千種',
    58: '今池',
    57: '池下',
    56: '覚王山',
    55: '東山公園',
    54: '星ヶ丘',
    53: '一社',
    52: '上社',
    51: '本郷',
    50: '藤が丘',
    109: '上小田井',
    108: '庄内緑地公園',
    107: '庄内通',
    106: '浄心',
    105: '浅間町',
    104: '大須観音',
    103: '鶴舞',
    102: '荒畑',
    101: '川名',
    100: 'いりなか',
    99: '塩釜口',
    98: '植田',
    97: '原',
    96: '平針',
    95: '赤池',
    86: '太閤通',
    85: '国際センター',
    84: '丸の内',
    83: '高岳',
    82: '車道',
    81: '吹上',
    80: '御器所',
    79: '桜山',
    78: '瑞穂区役所',
    77: '瑞穂運動場西',
    76: '桜本町',
    75: '鶴里',
    74: '野並',
    73: '鳴子北',
    72: '相生山',
    71: '神沢',
    70: '徳重',
    2: '上飯田',
    1: '平安通'
}

from routemap.items import RoutemapItem

BASE_URL = 'https://www.kotsu.city.nagoya.jp/STATION_DATA/station_subway_infos/diagrams/'


class MeijoSpider(scrapy.Spider):
    name = 'diagrams'
    allowed_domains = ['www.kotsu.city.nagoya.jp']
    start_urls = [f'{BASE_URL}{station_id}.json' for station_id in station_id_dict]

    
    def parse(self, response):

        station_id = re.findall(f'{BASE_URL}(.*).json', response.url)
        station_name = station_id_dict.get(int(station_id[0]))

        item = RoutemapItem()
        item['station_name'] = station_name
        item['body'] = json.loads(response.body)

        yield item

        
