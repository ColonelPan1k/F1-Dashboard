import datetime

from data_access import get_upcoming_event

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)


def create_time_data(d: dict[str, any]):
    keys = [
        ["date", "time"],
        ["fp1_date", "fp1_time"],
        ["fp2_date", "fp2_time"],
        ["fp3_date", "fp3_time"],
        ["quali_date", "quali_time"],
        ["sprint_date", "sprint_time"],
    ]

    data = {}

    for key_group in keys:
        date_times = [d.get(k) for k in key_group]
        if not date_times[0] and not date_times[1]:
            continue

        full_date = datetime.datetime.strptime(
            str(date_times[0]) + " " + str(date_times[1]), TIME_FORMAT
        )

        data.update({key_group[0]: utc_to_local(full_date).strftime(TIME_FORMAT)})

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
    now = datetime.datetime.now()

    dates = {}
    for event, date in event_data.get("time_data").items():
        diff = datetime.datetime.strptime(date, TIME_FORMAT) - now
        dates.update({event: diff})

    return {
        min(dates, key=dates.get): event_data["time_data"].get(
            min(dates, key=dates.get)
        )
    }
