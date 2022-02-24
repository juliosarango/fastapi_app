Para ejecutar el script de creación de usuarios primero ejecutar
```
export PYTHONPATH=$PWD
luego ejecutar el comando
```

```
alembic revision -m "comment"
alembia upgrade head
```