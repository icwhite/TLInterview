from warcio import ArchiveIterator
import requests
import json
warc_url = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-16/segments/1585370490497.6/warc/CC-MAIN-20200328074047-20200328104047-00000.warc.gz'
wat_url = warc_url.replace('/warc/', '/wat/').replace('warc.gz', 'warc.wat.gz')
print(wat_url)
# r = requests.get(warc_url, stream=True)
# records = ArchiveIterator(r.raw)
# print(r.raw)
# record = next(records)
# assert record.rec_type == 'warcinfo'
# # skip the warcinfo
# record = next(records)
# # Headers tell us what the record is about (e.g. source url)
# print(record.rec_headers.headers)
# print(record.content_stream().read())
# # metadata = json.loads(record.content_stream().read())