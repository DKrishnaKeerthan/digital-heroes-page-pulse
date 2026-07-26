# Failure Mode Analysis

## 1. External Website Timeout

Risk:

Target website is slow or unavailable.

Mitigation:

- 5-second timeout
- Return HTTP 408
- Structured error response

---

## 2. Traffic Burst

Risk:

500+ simultaneous requests overload server.

Mitigation:

- Semaphore concurrency limit
- Queue excess requests
- Horizontal scaling

---

## 3. Cache Failure

Risk:

Redis unavailable.

Mitigation:

- Fall back to direct fetch
- Log incident
- Continue serving requests