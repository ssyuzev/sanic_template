# Simple Sanic API template


## Run locally with docker

Use docker-compose
```
docker-compose build
docker-compose up
```


## Initialise environment variables. 

Save `.env.example`  as a `.env` file.


## Run migrations

```
fab init_db
```

## Batteries:

- sanic  https://sanic.readthedocs.io/en/latest/
- secure  https://github.com/TypeError/secure.py
- environs  https://github.com/sloria/environs
- sanic-envconfig  https://github.com/jamesstidard/sanic-envconfig
- databases  https://github.com/encode/databases
