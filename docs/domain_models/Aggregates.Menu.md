# Domain Models

## Menu

```python
class Menu:
    @classmethod
    def create(cls) -> Menu: ...

    def add_dinner(dinner: Dinner) -> None: ...

    def remove_dinner(dinner: Dinner) -> None: ...

    def update_section(section: MenuSection) -> None: ...
```


```json
{
    "id": "000000000-0000-0000-0000-000000000000",
    "name": "Menu Name",
    "description": "A menu",
    "average_rating": 4.5,
    "sections": [
        {
            "id": "000000000-0000-0000-0000-000000000000",
            "name": "Section Name",
            "description": "Section Description",
            "items": [
                {
                    "id": "000000000-0000-0000-0000-000000000000",
                    "name": "food",
                    "description": "standard food",
                    "price": 5.99
                }
            ]
        }
    ],
    "created_date_time": "2024-03-30T00:00:00.0000000Z",
    "updated_date_time": "2024-03-30T00:00:00.0000000Z",
    "host_id": "000000000-0000-0000-0000-000000000000",
    "dinner_ids": ["000000000-0000-0000-0000-000000000000"],
    "menu_review_ids": ["000000000-0000-0000-0000-000000000000"],
}
```
