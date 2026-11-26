"""Classify expiry dates from an offline certificate inventory at a fixed UTC instant."""
from datetime import datetime, timedelta, timezone


def renewal_status(expires, now, warning_days=30):
    if now.utcoffset() is None or expires.utcoffset() is None:
        raise ValueError("Supply timezone-aware datetimes")
    if warning_days < 0:
        raise ValueError("The warning interval must be non-negative")
    remaining = expires - now
    if remaining <= timedelta(0):
        return "expired"
    if remaining <= timedelta(days=warning_days):
        return "renew soon"
    return "current"


if __name__ == "__main__":
    now = datetime(2026, 1, 1, tzinfo=timezone.utc)
    for days, expected in [(0, "expired"), (30, "renew soon"), (31, "current")]:
        status = renewal_status(now + timedelta(days=days), now)
        assert status == expected
        print(f"Expiry in {days:2} days: {status}")
