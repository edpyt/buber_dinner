# Domain Aggregates

## Host

```python
class Host:
    first_name: str
    last_name: str
    profile_image: str

    average_rating: AverageRating
    user_id: UserId

    _menu_ids: list[MenuId]
    _dinner_ids: list[DinnerId]

    created_date_time: datetime
    updated_date_time: datetime
```

```json
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Tiffany",
    "last_name": "Doe",
    "profile_image": "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp",
    "average_rating": 4.5,
    "user_id": "00000000-0000-0000-0000-000000000000",
    "menu_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "dinner_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "created_date_time": "2024-03-30T00:00:00.0000000Z",
    "updated_date_time": "2024-03-30T00:00:00.0000000Z"
}
```
