"""Build an audit record from approved event types and outcomes."""
import json


def audit_record(event):
    actions = {"login", "logout"}
    outcomes = {"success", "failure"}
    if event.get("action") not in actions or event.get("outcome") not in outcomes:
        raise ValueError("Unrecognised audit action or outcome")
    return {"action": event["action"], "outcome": event["outcome"]}


if __name__ == "__main__":
    event = {"action": "login", "outcome": "success", "session": "synthetic-example"}
    record = audit_record(event)
    assert record == {"action": "login", "outcome": "success"}
    print(json.dumps(record, sort_keys=True))
