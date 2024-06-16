import click
from models.product import create_connection
from helpers import add_product, view_products, update_product, view_suppliers

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', prompt='Product name', help='The name of the product.')
@click.option('--quantity', prompt='Product quantity', type=int, help='The quantity of the product.')
@click.option('--supplier', prompt='Supplier name', help='The name of the supplier.')
def add(name, quantity, supplier):
    add_product(name, quantity, supplier)

@click.command()
def view():
    view_products()

@click.command()
@click.option('--id', prompt='Product ID', type=int, help='The ID of the product to update.')
@click.option('--name', help='New name for the product.')
@click.option('--quantity', type=int, help='New quantity for the product.')
@click.option('--quantity_sold', type=int, help='Quantity sold.')
@click.option('--supplier', help='New supplier for the product.')
def update(id, name, quantity, quantity_sold, supplier):
    update_product(id, name, quantity, quantity_sold, supplier)

@click.command()
def suppliers():
    view_suppliers()

cli.add_command(add)
cli.add_command(view)
cli.add_command(update)
cli.add_command(suppliers)

if __name__ == '__main__':
    cli()
