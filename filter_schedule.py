import json
from icalendar import Calendar, Event
from datetime import datetime

cal = Calendar()
cal.add('prodid', '-//EMF talks without recording//')
cal.add('version', '2.0')

talks_not_recorded = []

with open('schedule.json') as jfile:
    schedule = json.load(jfile)
    for talk in schedule:
        if talk['may_record']:
            talks_not_recorded.append(talk)
            event = Event()
            event.add('summary', "{0}, Venue: {1}, Type: {2}".format(talk['title'], talk['venue'], talk['type']))
            sd = datetime.strptime(talk['start_date'], "%Y-%m-%d %H:%M:%S")
            ed = datetime.strptime(talk['end_date'], "%Y-%m-%d %H:%M:%S")
            event.add('dtstart', sd)
            event.add('dtend',ed)
            event.add('url',talk['link'])
            cal.add_component(event)

file_ical = open('emf_no_recording.ics', 'wb')
file_ical.write(cal.to_ical())
file_ical.close()

with open('emf_no_recording.json', 'w') as file_json:
    json.dump(talks_not_recorded, file_json)
