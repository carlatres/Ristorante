# Ristorante

Servizio con le entità Ristorante, Ricetta ed Ingrediente.

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

Crea i file necessari nella app core e dentro il progetto Django (copiare il contenuto delle cartelle ristoranteapi e core).

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

Per testare le API, ho usato Postman. Ecco un esempio.

Per creare un nuovo ristorante:

Metodo: POST
URL: http://localhost:8000/api/ristoranti/
Body (raw JSON):
```shell
{
    "nome": "Ristorante Italiano",
    "indirizzo": "Via Roma, 1"
}
```

Per alcuni tests cases a maggior profondità. I test sono nella cartella **tests**.
