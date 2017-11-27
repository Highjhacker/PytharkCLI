import click
from pythark import Delegate, Transport


@click.group()
def delegate():
    pass


@delegate.command()
@click.option('--name', help="Name of the delegate.")
@click.option('--limit', help='Number of delegates.')
def search_delegate(name, limit):
    """ Allow us to search for a delegate.

    :param name: Name of the delegate we want to search.
    :param limit: Limit of results of the query.
    :return: List of delegate(s) informations.
    """
    delegate = Delegate()
    click.echo(delegate.search_delegates(query=name, limit=limit))


@click.group()
def transport():
    pass


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@transport.command()
@click.option('--recipient', help="Address of the recipient.")
@click.option('--amount', help="Amount of token to transfer.")
@click.option('--passphrase', prompt=True, hide_input=True, confirmation_prompt=True, help="Your personal Ark passphrase.")
@click.option('--yes', is_flag=True, callback=abort_if_false, expose_value=False, prompt="Are you sure you want to confirm this transaction ?")
def make_transaction(recipient, amount, passphrase):
    """ Allow us to make a new transaction.

    :param recipient: Ark address of the recipient.
    :param amount: Amount of token you want to transfer.
    :param passphrase: Your personnal passphrase.
    :return: A new transaction on the network.
    """
    transport = Transport()
    resp = transport.post_transaction("dark", recipient, amount, passphrase)
    if resp['success']:
        click.echo(click.style(str(resp), fg='green'))
    else:
        click.echo(click.style(str(resp), fg='red'))
    return resp

cli = click.CommandCollection(sources=[delegate, transport])

if __name__ == '__main__':
    cli()