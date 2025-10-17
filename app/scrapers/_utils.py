headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def nutrion_facts_to_int(fact: str):
    return int(fact.replace("g", ""))

def pretiffy_strings_list(strings_list: list):
    list_pretiffied = [i.text.replace("\n", "").replace(u"\xa0", u" ").strip() for i in strings_list]
    return list_pretiffied

def time_details_in_minutes(raw_time: list) -> list[int]:
    result = []
    for time in raw_time:
        time = time.strip()
        total_minutes = 0

        # Handle days
        if "day" in time:
            day_split = time.split("day")
            days = int(day_split[0].strip())
            total_minutes += days * 24 * 60
            time = day_split[1].strip() if len(day_split) > 1 else ""

        # Handle hours
        if "hr" in time or "hrs" in time:
            if "hrs" in time:
                hr_split = time.split("hrs")
            else:
                hr_split = time.split("hr")
            hours = int(hr_split[0].strip())
            total_minutes += hours * 60
            time = hr_split[1].strip() if len(hr_split) > 1 else ""

        # Handle minutes
        if "mins" in time:
            mins = int(time.replace("mins", "").strip())
            total_minutes += mins

        result.append(total_minutes if total_minutes > 0 else 0)

    return result
