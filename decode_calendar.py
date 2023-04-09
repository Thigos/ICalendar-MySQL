import pytz
import log
import icalendar

def read_calendar_file(path):
    try:
        with open(path, 'rb') as calendar_file:
            bytes_file = calendar_file.read()
            return bytes_file
    except FileNotFoundError:
        log.e('Não Foi Possivel Encontrar o Arquivo: ' + path)
    except PermissionError:
        log.e('Permissão de Leitura Negada: '  + path)
    
    
def normalize_text(text):
    text = text.replace('\xa0', '').replace('\t', '').replace('\\n', '\n').replace('\\', '')
    return text
    
def decode(path):
    calendar = icalendar.Calendar.from_ical(read_calendar_file(path))

    calendar_dict = {}

    i = 0

    for event in calendar.walk():
        if event.name == "VEVENT":
            dtend_utc = event.get('DTEND').dt
            tz_utc3 = pytz.timezone('America/Sao_Paulo')
            dtend_utc3 = dtend_utc.astimezone(tz_utc3).replace(tzinfo=None)

            summary = event.get('SUMMARY').to_ical().decode('utf-8')
            summary = normalize_text(summary)

            description = event.get('DESCRIPTION').to_ical().decode('utf-8')
            description = normalize_text(description)

            calendar_dict[i] = {
                'UID': event.get('UID').to_ical().decode('utf-8'),
                'SUMMARY': summary,
                'DESCRIPTION': description,
                'DTEND': dtend_utc3.isoformat(),
                'CATEGORIES': event.get('CATEGORIES').to_ical().decode('utf-8')
            }

        i += 1

    return calendar_dict