import datetime

from data_access import get_upcoming_event

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)


def create_time_data(d: dict[str, any]):
    keys = {
        "Race": ["date", "time"],
        "Free Practice 1": ["fp1_date", "fp1_time"],
        "Free Practice 2": ["fp2_date", "fp2_time"],
        "Free Practice 3": ["fp3_date", "fp3_time"],
        "Qualifying": ["quali_date", "quali_time"],
        "Sprint": ["sprint_date", "sprint_time"],
    }

    data = {}

    for key, key_group in keys.items():
        date_times = [d.get(k) for k in key_group]
        if not date_times[0] and not date_times[1]:
            continue

        full_date = datetime.datetime.strptime(
            str(date_times[0]) + " " + str(date_times[1]), TIME_FORMAT
        )

        data.update({key: utc_to_local(full_date).strftime(TIME_FORMAT)})

    return data


def process_upcoming_event_data():
    event = get_upcoming_event()[0]

    data = {
        "raceId": event.get("raceId"),
        "race": event.get("name"),
        "year": event.get("year"),
        "round": event.get("round"),
        "url": event.get("url"),
        "time_data": create_time_data(event),
    }
    return data


def calculate_upcoming_sub_event():
    event_data = process_upcoming_event_data()
    time_data = event_data.pop("time_data")
    now = datetime.datetime.now()

    dates = {"past": {}, "upcoming": {}, "current": {}}

    for event, date in time_data.items():
        diff = datetime.datetime.strptime(date, TIME_FORMAT) - now

        # This is a mess
        if diff <= datetime.timedelta(days=-1, seconds=82800):
            dates.get("past").update({event: date})
        elif diff >= datetime.timedelta(days=0):
            dates["upcoming"].update({event: date})
        else:
            dates["current"].update({event: date})

    if not dates:
        return {}

    key = min(dates["upcoming"], key=dates["upcoming"].get)
    dates.update({"next": {key: dates["upcoming"].get(key)}})

    return {"race": event_data, "events": dates}


def get_upcoming_events_as_table():
    race = get_upcoming_event()[0]
    time_data = create_time_data(race)
    formatted = []

    print(time_data)

    for key, value in time_data.items():
        date, time = value.split(" ")[0], value.split(" ")[1]

        formatted.append({"event_name": key, "date": date, "time": time})

    return formatted
