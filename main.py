from secrets import secrets
from reporter import Reporter


def get_state():
    return [
        ("test-state-1", 1.0, "celcius"),
        ("test-state-2", 23789347, None),
        ("test-state-3", -3.4, "percent"),
    ]


r = Reporter(secrets, get_state)
r.run()
