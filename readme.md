### Створення віртуального оточення

```
python3 -m venv .venv
source .venv/bin/activate

deactivate
```

Згенерувати requirements.txt за допомогою pip
```
pip freeze > requirements.txt
```


Встановити пакети, перелічені у requirements.txt
```
pip install -r requirements.txt
```

Список встановлених пакетів з версіями
```
pip freeze
pip list
```

```
which python
```