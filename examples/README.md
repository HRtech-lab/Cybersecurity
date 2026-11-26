# Runnable examples

Run these commands from the repository root.

## Certificate renewals

The example fixes the reference time at midnight UTC on 1 January 2026 and uses a 30-day renewal window. A certificate expiring at that instant is labelled `expired`. One with exactly 30 days left is labelled `renew soon`, and one with 31 days left is labelled `current`.

```sh
python examples/certificate_renewals.py
```

## Structured audit log

Build an audit record from approved event types and outcomes.

```sh
python examples/structured_audit_log.py
```
