# Perftest for Build Run Go

Build Run Go:  [Repo](https://github.com/sakethramanujam/build-run-go)

**Current End Points**:
 - [https://build-compose-go-fjne2mwvbq-an.a.run.app/fib/{number}](https://build-compose-go-fjne2mwvbq-an.a.run.app/fib/)
 - [https://build-compose-go-fjne2mwvbq-an.a.run.app/square/{number}](https://build-compose-go-fjne2mwvbq-an.a.run.app/square/<number>)
 - [https://build-compose-go-fjne2mwvbq-an.a.run.app/cube/{number}](https://build-compose-go-fjne2mwvbq-an.a.run.app/cube/)
 - [https://build-compose-go-fjne2mwvbq-an.a.run.app/quad/{number}](https://build-compose-go-fjne2mwvbq-an.a.run.app/quad/{number})

## Setup
- Install the requirements with 

```bash
$ pip install -r requirements.txt
```
or just use the virtualenv as
```bash
$ source performance/bin/activate
```

## Usage:
```bash
$ chmod +x run.sh (optional)
$ ./run.sh
```

The locustio server runs on `:8089` where ever it's running.