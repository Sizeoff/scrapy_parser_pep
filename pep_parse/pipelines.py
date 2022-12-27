import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
FILENAME = 'status_summary_{now_format}.csv'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_format = now.strftime(DT_FORMAT)
        file_path = result_dir / f'status_summary_{now_format}.csv'
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file,
                                dialect=csv.unix_dialect,
                                quoting=csv.QUOTE_MINIMAL
                                )
            writer.writerows([('Статус', 'Количество'),
                              *self.results.items(),
                              ('Всего', sum(self.results.values()))])
