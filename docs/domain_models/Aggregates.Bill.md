# Domain Aggregates

## Bill

```python
class Bill:
    @classmethod
    def create(cls) -> Bill: ...
```

```json
{
    "id": "000000000-0000-0000-0000-000000000000",
    "dinner_id": "000000000-0000-0000-0000-000000000000",
    "guest_id": "000000000-0000-0000-0000-000000000000",
    "host_id": "000000000-0000-0000-0000-000000000000",
    "price": {
        "amount": 10.99,
        "currency": "USD"
    },
    "created_date_time": "2024-03-30T00:00:00.0000000Z",
    "updated_date_time": "2024-03-30T00:00:00.0000000Z",
}
```
