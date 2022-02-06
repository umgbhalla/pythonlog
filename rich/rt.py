from rich import print
from rich import pretty
from rich import inspect
from rich.console import Console
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
from rich.console import Console
from rich.traceback import install
install(show_locals=True)
console = Console()

try:
    do_something()
except Exception:
    console.print_exception(show_locals=True)


for step in track(range(100)):
    sleep(0.1)
    step

pretty.install()
print("halo [red] world [/red]")
print(locals())
inspect("halo",methods=True)

console.print("Hello", "World!", style="bold italic blue")
console.log("Hello", "World!", style="italic green")

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)

console.print(table)

sdasda
