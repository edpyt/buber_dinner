# Domain Aggregates

## Guest

```python
class Guest:
    first_name: str
    last_name: str
    profile_image: str

    average_rating: AverageRating
    user_id: UserId

    _upcoming_dinner_ids: list[Dinner]
    _past_dinner_ids: list[Dinner]
    _bill_ids: list[Bill]
    _menu_review_ids: list[MenuReview]
    _ratings: list[Rating]

    created_date_time: datetime
    updated_date_time: datetime
```

```json
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "John",
    "last_name": "Doe",
    "profile_image": "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp",
    "average_rating": 4.5,
    "user_id": "00000000-0000-0000-0000-000000000000",
    "upcoming_dinner_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "past_dinner_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "pending_dinner_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "bill_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "menu_review_ids": [
        "00000000-0000-0000-0000-000000000000"
    ],
    "ratings": [
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "host_id": "00000000-0000-0000-0000-000000000000",
            "dinner_id": "00000000-0000-0000-0000-000000000000",
            "rating": 4,
            "created_date_time": "2024-03-30T00:00:00.0000000Z",
            "updated_date_time": "2024-03-30T00:00:00.0000000Z"
        }
    ],
    "createdDateTime": "2024-03-30T00:00:00.0000000Z",
    "updatedDateTime": "2024-03-30T00:00:00.0000000Z"
}
```
