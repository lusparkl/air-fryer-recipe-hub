headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def nutrion_facts_to_int(fact: str):
    return int(fact.replace("g", ""))

def pretiffy_strings_list(strings_list: list):
    list_pretiffied = [i.text.replace("\n", "").replace(u"\xa0", u" ").strip() for i in strings_list]
    return list_pretiffied

def time_details_in_minutes(raw_time: list):
    result = []
    for time in raw_time:
        time = time.strip()
        if ("hr" in time or "hrs" in time) and "mins" in time:
            if "hrs" in time:
                time_list_raw = time.split("hrs")
            else:
                time_list_raw = time.split("hr")
            time_list = [int(t.replace("mins", "").strip()) for t in time_list_raw if t.strip()]
            if len(time_list) == 2:
                result.append(time_list[0] * 60 + time_list[1])
            else:
                result.append(time_list[0])
        elif "hr" in time or "hrs" in time:
            t = int(time.replace("hrs", "").replace("hr", "").strip()) * 60
            result.append(t)
        elif "mins" in time:
            t = int(time.replace("mins", "").strip())
            result.append(t)
        else:
            result.append(0)
    return result
