import typer
app = typer.Typer()


@app.command()
def hellow(name: str, d: int, state:bool = True):
    print(f"halo {name} {d}")
    if state==True:
        print(f"iq {d}")


@app.command()
def bye():
    print("bye")


if __name__ == "__main__":
    app()
