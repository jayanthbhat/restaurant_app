# restaurant_app

Create a Restaurant Application using Django or DRF.
Create Views (the response should be a json data) or API's as per your convenience.
Create API's to get Food category (Indian Cuisine), Food items (Idli,Dosa,etc) , Food attribute
(Sweet,Spicy,etc)
The application should include the following functions:
1. Sign Up
2. Sign In
3. Get Food category
4. Get Food Items when a category is passed
5. When a food attribute and category is passed, the related food items of that category should be
obtained and
if there is no category, all the food items related to the attribute is obtained.
6. Prince Range filter - When a price range is passed, all food items between the range should be
obtained.
7. Search option - Food category or food item details is obtained on search.

## Answers
1. Sign Up
http://127.0.0.1:8000/api/register/

2. Sign In
http://127.0.0.1:8000/api/login/

3. Get Food category
http://127.0.0.1:8000/api/list-categories/

4.Get Food Items when a category is passed

http://127.0.0.1:8000/api/list-fooditems-categories/?category_id=1

Response:
[
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Sweet"
        },
        "name": "Kesari Bath",
        "price": 50
    },
    {
        "id": 2,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Sambar",
        "price": 15
    },
    {
        "id": 3,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Tangy"
        },
        "name": "Rasam",
        "price": 20
    },
    {
        "id": 4,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Khara Bath",
        "price": 40
    }
]

5.
a.When a food attribute and category is passed, the related food items of that category should be
obtained

http://127.0.0.1:8000/api/list-fooditems-categories/?category_id=1&attribute_id=1

Response:

[
    {
        "id": 2,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Sambar",
        "price": 15
    },
    {
        "id": 4,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Khara Bath",
        "price": 40
    }
]

5.
b.if there is no category, all the food items related to the attribute is obtained

Response:
[
    {
        "id": 2,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Sambar",
        "price": 15
    },
    {
        "id": 4,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Khara Bath",
        "price": 40
    },
    {
        "id": 5,
        "category": {
            "id": 2,
            "name": "Chinese"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Gobi Manchurian",
        "price": 30
    }
]

6. Prince Range filter - When a price range is passed, all food items between the range should be
obtained.

http://127.0.0.1:8000/api/list-fooditems-categories/?price_start=30&price_end=50

Response:
[
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Sweet"
        },
        "name": "Kesari Bath",
        "price": 50
    },
    {
        "id": 4,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Khara Bath",
        "price": 40
    },
    {
        "id": 5,
        "category": {
            "id": 2,
            "name": "Chinese"
        },
        "attributes": {
            "name": "Spicy"
        },
        "name": "Gobi Manchurian",
        "price": 30
    }
]

7. Search option - Food category or food item details is obtained on search.

http://127.0.0.1:8000/api/list-fooditems-categories/?qs=rasa

[
    {
        "id": 3,
        "category": {
            "id": 1,
            "name": "Indian Cuisine"
        },
        "attributes": {
            "name": "Tangy"
        },
        "name": "Rasam",
        "price": 20
    }
]
