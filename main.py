import database
from InquirerPy import inquirer
from rich.console import Console
import pyfiglet 
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

def showIntro()->None:
    console = Console()

    title = pyfiglet.figlet_format("Coffee Shop",font="big_money-ne")
    subtitle = Text(
        "☕ Manage | Products | Customers ",
        style="bold yellow"
        )
    panel =Panel.fit(
        Align.center(title),
        border_style="green"
    )
    console.clear()
    console.print(Align.center(panel),style="cyan")
    console.print(Align.center(subtitle))
    console.print("\n")

def showExit()->None:
    console = Console()

    goodbye = pyfiglet.figlet_format("Good Bye!",font="small")
    console.print("\n")
    console.print(goodbye,style="green")
    console.print("☕Thanks for Using Coffee Shop CLI☕",style="bold italic green")
    console.print("\n")

console = Console()
def customerMenu()->None:
    menu = {
        "View Customers" : database.viewCustomers,
        "Add Customers"  : addCustomerFlow ,
        "Delete Customer": deleteCustomerFlow,
        "Back"           : None 
    }
    runMenu(menu)

def addCustomerFlow()->None:
    name = inquirer.text(message="Customer name").execute()
    email = inquirer.text(message="Email").execute()
    phone = inquirer.text(message="Phone:").execute()
    database.addCustomers(name,email,phone)
    console.print("✅ Customer Added!",style="bold green")

def deleteCustomerFlow()->None:
    customerID = inquirer.text(message="Customer ID to delete").execute()
    database.deleteCustomers(customerID)
    console.print("Customer Deleted",style="bold red")

mainMenu = {
    "Customers" : customerMenu,
    "Product"   : None, #to be implemented
    "Orders"    : None, #to be implemented
    "Exit"      : None,
}

def runMenu(menu:dict):
    while True:
        choice = inquirer.select(
        message="☕ Coffee Shop CLI - Use arrows and enter to navigate.",
        pointer="👉",
        choices=list(menu.keys()),
        instruction="",
        long_instruction="",

        ).execute()
        
        if callable(menu[choice]):
            menu[choice]()
        else:
            break

def main()->int :
    showIntro()
    runMenu(mainMenu)
    showExit()
    return 0
if __name__ == "__main__":
    main()