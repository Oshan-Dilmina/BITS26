from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def getbaseprefix(base):
    if base == 2:
        return 'b'
    if base == 10:
        return 'd'
    if base == 16:
        return 'x'
    
def todecimalsteps(numstr,base):
    numstr = numstr.upper()
    remchar = "0123456789ABCDEF"
    total = 0
    power = len(numstr-1)

    table = Table(title=f"Base {base} to base 10", show_lines=True)
    table.add_column("Digit", justify='center',style='cyan')
    table.add_column("Positinal Value", justify='center',style='yellow')
    table.add_column("Calculations", justify='left',style='green')

    for char in numstr:
        val = remchar.index(char)
        c = val*(base**power)
        table.add_row(char,f"{base}^{power}",f"{val} x {base}^{power} = {c}")
        total = total + c
        power = power - 1

    console.print(table)
    console.print(f"sum of all values is {total}")

def fromdecimalsteps(decimalval,target):
    remchar = "0123456789ABCDEF"
    temp = decimalval

    table = Table(title=f"Base 10 to base {target}", show_lines=True)
    table.add_column("Division", justify='left',style='cyan')
    table.add_column("Quotient", justify='center',style='yellow')
    table.add_column("Calculations", justify='center',style='green')

    steps=[]
    if temp == 0:
        table.add_row(f"0 / {target}",'0','0')
    
    while temp>0:
        rem = temp % target
        quotient = temp // target
        charrem = remchar[rem]
        table.add_row(f"{temp} / {target}", str(quotient),f"{rem} ({charrem})")
        steps.append(charrem)
        temp = quotient

    result = "".join(reversed(steps))
    console.print(table)
    console.print(result)

def main():
    console.clear()
    console.print(Panel.fit("[bold violet] Number Base Converter[/bold violet]",border_style='violet'))

    modes = {'1' : (2, 'Binary'),'2' : (10, 'Decimal'),'3' : (16, 'Hexadecimal')}

    console.print("[bold]Input format[/bold]")
    console.print('1. Binary')
    console.print('2. Decimal')
    console.print('3. Hexadecimal')

    inputchoice = Prompt.ask("Choose 1-3", choices=['1','2','3'])
    inputbase, inputname = modes[inputchoice]

    while True:
        userinput = Prompt.ask(f"Enter {inputname} number")
        try:
            decimalval = int(userinput,inputbase)
            break
        except ValueError:
            console.print(f"[bold red]invalid {inputname} number[/bold red]")

    console.print("[bold]Output format[/bold]")
    console.print('1. Binary')
    console.print('2. Decimal')
    console.print('3. Hexadecimal')

    outputchoice = Prompt.ask("Choose 1-3", choices=['1','2','3'])
    outputbase, outputname = modes[outputchoice]

    if inputbase == outputbase:
        console.print(f'Base are identivical nothing to convert, result is {userinput}')
        return

    console.print("[bold yellow] STEPS [/bold yellow]")

    if inputbase != 10:
        todecimalsteps(userinput,inputbase)
    
    if outputbase != 10:
        fromdecimalsteps(decimalval,outputbase)
        prefix = getbaseprefix(outputbase)
        finaloutput = format(decimalval,prefix).upper()
    else:
        finaloutput = str(decimalval)

    final = (
        f"Input {inputname}: [bold yellow]{userinput}[/bold yellow]\n"
        f"Output {outputname}: [bold green]{finaloutput}[/bold green]"
    )
    console.print(Panel(final,title='Final Output',border_style='magenta'))

main()