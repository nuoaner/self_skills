# Database Documentation

## 1. Database Status Enum

Database status must use only: `pending-design` / `designed` / `migrated` / `online` / `deprecated`.

## 2. Tables

| Table | Description | Status | Owner |
|---|---|---|---|
| example_table | TBD | pending-design | TBD |

## 3. Table Details

### example_table

- Description: TBD
- Status: pending-design

| Field | Type | Nullable | Default | Description |
|---|---|---|---|---|
| id | bigint | no | auto increment | Primary key |
| created_at | datetime | no | current timestamp | Created time |

## 4. Relationships

| Source Table | Field | Target Table | Target Field | Description |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## 5. Migration Records

| Version | Date | Change | Rollback | Status |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | pending-design |

## 6. Data Safety Notes

- Do not record production credentials or connection strings here.
- Use `.env.example` for variable names and placeholder values.
- Document rollback and backup requirements before destructive changes.
