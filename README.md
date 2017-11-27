![Imgur](https://i.imgur.com/ysh3akS.png)

# PytharkCLI

A Pythark CLI example based on Click, allowing us to search for delegates and make new transactions.


## Built with
- [Python](https://www.python.org/)
- [PythArk](https://github.com/Highjhacker/pythark/)
- [Click](http://click.pocoo.org)

## Installation

The first step is to clone this repository : 
```shell
$ git clone https://github.com/Highjhacker/PytharkCLI.git
```

Then go inside the cloned repository and create a virtualenvironment([How to create a VirtualEnvironment](http://virtualenv.readthedocs.io/en/stable/))
```shell
$ cd PytharkCLI
$ virtualenv venv 
# Or if you want to specify a python version
$ virtualenv -p python3.6 venv # If python3.6 is a correct command
```
When the virtualenv is created, all you need to do is to install the dependencies from the requirements.txt file
```shell
pip install -r requirements.txt
```

And you should be ready to run it
```
$ python main.py -- help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  make_transaction  Allow us to make a new transaction.
  search_delegate   Allow us to search for a delegate.

```

## Usage
```shell
$ python main.py make_transaction --recipient DTXXKSodtRs1ejxy4uZ7WyXpLXwUrXmAvn --amount 1000000     
> Passphrase : 
> Repeat for confirmation : 
> Are you sure you want to confirm this transaction ? [y/N]
> {'success': True, 'transactionIds': ['6c0ecc2a13fea4fccb1ceed5cb64debe290e4697e7afcb0579ba3443add370cf'], 'broadcast': '100.0%'}
```

```shell
$ python main.py search_delegate --name dr --limit 1
{'success': True, 'delegates': [{'username': 'dr10', 'address': 'ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9', 
'publicKey': '031641ff081b93279b669f7771b3fbe48ade13eadb6d5fd85bdd025655e349f008', 'vote': '152419468863195', 
'producedblocks': 33546, 'missedblocks': 207}]}
>
```

## Authors

- Jolan Beer - Highjhacker

## License

PytharkCLI is under MIT license. See the [LICENSE file](https://github.com/Highjhacker/PytharkCLI/blob/master/LICENSE) for more informations.
