import decode_calendar, database, get_calendar
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', '-u', nargs='?')
parser.add_argument('--path', '-p')

args = parser.parse_args()

url, path = args.url, args.path

if args.url != None:
    sucess_download = get_calendar.download(url, path)
    if sucess_download:
        calendar_dict = decode_calendar.decode(path)
        database.db_write(calendar_dict)
else:
    calendar_dict = decode_calendar.decode(path)
    database.db_write(calendar_dict)