# Create Menu

## Create Menu Requst

```
POST /hosts/{host_id}/menus
```

```json
{
  "name": "First Menu",
  "description": "My First Menu!!",
  "sections": [
    {
      "name": "Appetizers",
      "description": "Starters",
      "items": [
        {
          "name": "Fried Pickles",
          "description": "Deep fried pickles"
        }
      ]
    }
  ]
}
```
