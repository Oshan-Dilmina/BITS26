import re
from rich.console import Console
from rich.table import Table

def frequency(text):
    freq = {}

    for char in text and re.findall(r'[a-z0-9]',text):
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    freq = dict(sorted(freq.items(),key =lambda x:x[1]))

    console = Console()
    table = Table(
        title = "Character Frequency Counter",
        title_style = 'bold magenta',
        header_style= "cyan"
    )

    table.add_column("Character",justify="center", style="bold green")
    table.add_column("Count",justify="right", style="yellow")

    for char,count in freq.items():
        table.add_row(char,str(count))
    
    console.print("\n")
    console.print(table)

text = input().lower()
frequency(text)

