# Ristorante

Servizio con entità Ristorante, Ricetta ed Ingrediente.

## Requisiti

* Python 3.11
* Django 5.0.6
* DjangoRestFramework 3.15.2 

### Configurazione Django e Django Framework per questo esercizio

Installa Django e Django Rest Framework

```shell
pip install django djangorestframework
```

Crea un nuovo progetto Django

```shell
django-admin startproject ristoranteapi
cd ristoranteapi
```

Crea una nuova app all'interno del progetto

```shell
python manage.py startapp core
```

Crea i file necessari nella app core e dentro il progetto Django (copiare il contenuto dei folder ristoranteapi e core).

Esegui la migrazione al database 

```shell
python manage.py makemigrations
python manage.py migrate
```

Avvia il server di sviluppo
```shell
python manage.py runserver
```

### Ora il servizio dovrebbe essere in esecuzione su http://localhost:8000/api/ 

## Testing 

Per testare le API, ho usato Postman. Ecco alcuni esempi.

[<img alt="POST" src="https://drive.google.com/file/d/1L_-4s7e63cAKrcpOeI7y0W94HNi1F6tB/view?usp=sharing">]

## Unitest

The tests are contained in the **tests** folder.
