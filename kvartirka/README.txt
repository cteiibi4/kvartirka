Проект запускается стандартным python manage.py runserver

Примеры запросов:
1. Добавление статьи: curl -H "Content-Type: application/json" --request POST --data '{"title":"Статья №1", "body":"Lorem ipsum "}' http://127.0.0.1:8000/api/article/
2. Добавление комментария: curl -H "Content-Type: application/json" --request POST --data '{"article_id":"1", "body": "test"}' http://127.0.0.1:8000/api/comment/
3. Добавление ответа на комментарий: curl -H "Content-Type: application/json" --request POST --data '{"article_id":"1", "parent_comment_id":1, "body": "test2"}' http://127.0.0.1:8000/api/comment/
4. Получение всех комментариев до 3 уровня к статье: curl --request GET http://127.0.0.1:8000/api/article/<article_id>
5. Получение всех вложенных комментариев для комментария 3-его уровня: curl --request GET http://127.0.0.1:8000/api/comment/<comment_id>