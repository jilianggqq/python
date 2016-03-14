django restful framework test
======

```python
# runserver
python manage.py runserver

# luntch the shell
python manage.py shell
```

```httpie
http --json PUT http://127.0.0.1:8000/snippets/12/ code="print 12" title='new title'

http DELETE http://127.0.0.1:8000/snippets/12/

http GET http://127.0.0.1:8000/snippets/

http --json POST http://127.0.0.1:8000/snippets/ code="print \"jrf\""

<!-- with username:password -->
http -a guest:guest POST http://127.0.0.1:8000/snippets/ code="print 789"

http -a guest:guest PUT http://127.0.0.1:8000/snippets/1/ code="print 1234" title='python first ex'
```