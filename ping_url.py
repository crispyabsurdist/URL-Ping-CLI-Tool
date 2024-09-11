#!/usr/bin/env python3
# Author: Markus Hedenborn
# GitHub: https://github.com/crispyabsurdist

import requests
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint
import sys
import time

console = Console()


def ping_url(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        status_msg = f"URL: {url}\nHTTP Status Code: {status_code}"

        if status_code >= 200 and status_code < 300:
            status_color = "green"
        elif status_code >= 400 and status_code < 500:
            status_color = "yellow"
        elif status_code >= 500:
            status_color = "red"
        else:
            status_color = "blue"

        console.print(
            Panel(
                f"[bold {status_color}]{status_msg}[/bold {status_color}]",
                title="Ping Result",
                border_style="bold blue",
            )
        )

    except requests.exceptions.RequestException as e:
        console.print(
            Panel(
                f"[bold red]Error: {str(e)}[/bold red]",
                title="Ping Error",
                border_style="bold red",
            )
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        rprint("[bold red]Usage: python ping_url.py <URL>[/bold red]")
    else:
        url = sys.argv[1]
        while True:
            ping_url(url)
            console.print(
                Panel(
                    f"[bold cyan]Waiting for 5 minutes before the next ping...[/bold cyan]",
                    border_style="bold magenta",
                )
            )
            time.sleep(300)
