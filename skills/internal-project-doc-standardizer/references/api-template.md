# API Documentation

## 1. API Status Enum

API status must use only: `pending-design` / `pending-implementation` / `implemented` / `pending-joint-debugging` / `online` / `deprecated`.

## 2. API List

| API ID | Method | Path | Description | Status | Owner |
|---|---|---|---|---|---|
| API-001 | GET | /api/example | TBD | pending-design | TBD |

## 3. API Details

### API-001 TBD

- Method: GET
- Path: `/api/example`
- Status: pending-design
- Auth: TBD
- Permission: TBD

#### Request Params

| Field | Type | Required | Description | Example |
|---|---|---|---|---|
| id | string | yes | TBD | TBD |

#### Request Body

```json
{
  "example": "TBD"
}
```

#### Success Response

```json
{
  "code": 0,
  "message": "ok",
  "data": {}
}
```

#### Error Response

| Code | Meaning | Handling |
|---|---|---|
| TBD | TBD | TBD |

## 4. Joint Debugging Notes

| Item | Status | Notes |
|---|---|---|
| Endpoint confirmed | pending | TBD |
| Field mapping confirmed | pending | TBD |
| Error format confirmed | pending | TBD |
