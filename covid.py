import requests
from warcio.archiveiterator import ArchiveIterator

f = open("april-march-warc.paths.txt", "r")
print("https://commoncrawl.s3.amazonaws.com/" + f.readline())
print("https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-16/segments/1585370490497.6/warc/CC-MAIN-20200328074047-20200328104047-00000.warc.gz")

covid_urls = []
def print_records(url):
    resp = requests.get(url, stream=True)

    for record in ArchiveIterator(resp.raw, arc2warc=True):
        if record.rec_type == 'warcinfo':
            print(record.raw_stream.read())

        elif record.rec_type == 'response':
            if record.http_headers != None and record.http_headers.get_header('Content-Type') == 'text/html':
                # print(record.http_headers)
                url = record.rec_headers.get_header('WARC-Target-URI')
                a = record.content_stream().read().decode("utf-8", "replace")
                if "COVID" in a and "Economy" in a:
                    print(url)
                    covid_urls.append(url)
                # print('\n')

# print_records("https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-16/segments/1585370490497.6/warc/CC-MAIN-20200328074047-20200328104047-00000.warc.gz")

# print(covid_urls)
# s = "https://commoncrawl.s3.amazonaws.com/" + str(f.readline())
# print_records(s)

def get_records(warc_file):
    resp = requests.get(warc_file, stream=True)
    lst = []
    records = ArchiveIterator(resp.raw, arc2warc=True)
    for i in range(1000):
        lst.append(next(records))
    return lst

def mapFunc(url):
    if 
    return (url, 1)

def 
# print(get_records("https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-16/segments/1585370490497.6/warc/CC-MAIN-20200328074047-20200328104047-00000.warc.gz"))

# print(url)
# print(text)