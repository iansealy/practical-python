# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """

    def headings(self, headers):
        print("<tr><th>", end="")
        print("</th><th>".join(headers), end="")
        print("</th></tr>")

    def row(self, rowdata):
        print("<tr><td>", end="")
        print("</td><td>".join(rowdata), end="")
        print("</td></tr>")


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == "txt":
        formatter = TextTableFormatter()
    elif name == "csv":
        formatter = CSVTableFormatter()
    elif name == "html":
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format {name}")
    return formatter


def print_table(portfolio, attributes, formatter):
    formatter.headings(attributes)
    for s in portfolio:
        rowdata = [str(getattr(s, attr)) for attr in attributes]
        formatter.row(rowdata)
