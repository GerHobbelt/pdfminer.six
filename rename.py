from pathlib import Path


def main():
    for path in Path(__file__).parent.joinpath("pdfminer").glob("*.py"):
        if path.name != "__init__.py":
            path.rename(str(path.absolute()) + "x")


if __name__ == '__main__':
    main()
