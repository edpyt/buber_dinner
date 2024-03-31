# Domain Aggregates

## Dinner

```python
class Dinner:
    id: DinnerId
    name: str
    description: str
    start_date_time: datetime
    end_date_time: datetime
    is_public: bool
    max_guests: int
    image_url: str

    price: Price
    status: Status
    location: Location

    host_id: HostId
    menu_id: MenuId

    _reservations: list[Reservation]

    started_date_time: datetime | None
    ended_date_time: datetime | None

    created_date_time: datetime
    updated_date_time: datetime

    @property
    def reservations(self) -> tuple[Reservation]:
        return tuple(self._reservations)
```

```json
{
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Dinner name",
    "description": "A dinner",
    "start_date_time": "2024-03-30T00:00:00.0000000Z",
    "end_date_time": "2024-03-30T00:00:00.0000000Z",
    "started_date_time": null,
    "ended_date_time": null,
    "status": "upcoming", // upcoming, in_progress, ended, cancelled,
    "is_public": "true",
    "max_guests": 10,
    "price": {
        "amount": 10.99,
        "currency": "USD"
    },
    "host_id": "00000000-0000-0000-0000-000000000000",
    "menu_id": "00000000-0000-0000-0000-000000000000",
    "image_url": "https://image.com",
    "location": {
        "name": "Bob's Dinner",
        "address": "Moscow, Russia",
        "latitude": 55.751244,
        "longitude": 37.618423
    },
    "reservations": [
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "guests_count": 2,
            "reservation_status": "reserved", // penging_guest_confirmation, reserved, cancelled
            "guest_id": "00000000-0000-0000-0000-000000000000",
            "bill_id": "00000000-0000-0000-0000-000000000000",
            "arrival_date_time": null,
            "created_date_time": "2024-03-30T00:00:00.0000000Z",
            "updated_date_time": "2024-03-30T00:00:00.0000000Z"
        }
    ],
    "created_date_time": "2024-03-30T00:00:00.0000000Z",
    "updated_date_time": "2024-03-30T00:00:00.0000000Z"
}
```
