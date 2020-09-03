import os
import csv

from others_inserter.constant import AppPath
from others_inserter.translator.translator import translate

from elasticsearch import Elasticsearch


def inserter(c_file):
    with open(c_file, 'r', encoding='utf-8') as csv_file:
        es = Elasticsearch(
            [
                {'host': '192.168.220.165', 'port': 9200}
            ],
            timeout=3600
        )

        log_reader = csv.DictReader(csv_file)

        count = 0
        for line in log_reader:
            if line.get('ngaf_url.method') != 'GET':
                continue

            if not line.get('ngaf_url.uri').startswith('/report'):
                continue

            records = translate(line)

            if records:
                es.index(index='ngaf_url' + '-' + records['record_date'], doc_type='politics', body=records)
                count += 1

            if not (count % 100):
                print('{} inserted!'.format(count))


if __name__ == '__main__':
    if not os.path.exists(AppPath.CSV_DIR):
        print('{} is Empty!'.format(AppPath.CSV_DIR))

    for dir in os.listdir(AppPath.CSV_DIR):
        if dir == 'ngaf_url':
            path = os.path.join(AppPath.CSV_DIR, dir)

            for file in os.listdir(path):
                if file.endswith('.csv'):
                    cur_file = os.path.join(path, file)

                    try:
                        inserter(cur_file)
                    except Exception as e:
                        print(e)
                        os.rename(cur_file, cur_file + '.err')
                    else:
                        print('{} inserted succeed!'.format(cur_file))
                        os.rename(cur_file, cur_file + '.done')
