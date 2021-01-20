from warcio.archiveiterator import ArchiveIterator
import requests

warc_file = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-16/segments/1585370490497.6/wet/CC-MAIN-20200328074047-20200328104047-00000.warc.et.gz'

resp = requests.get(warc_file, stream=True)
records = ArchiveIterator(resp.raw)
# List any of the WARC files found in the data folder


# Process each of the WARC files we found
files_processed = 0
record = next(records)
print(record)
url = record.rec_headers.get_header("WARC-Target-URI")
if url:
    text = record.payload.read()
text = None
#
print(url)
print(text)
print
print