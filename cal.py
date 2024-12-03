import calendar
from rich.console import Console
from rich.table import Table

console = Console()

def display_year_calendar(year):
    console.print(f"[bold cyan]Calendar for {year}[/bold cyan]\n")
    table = Table(show_lines=True)

    for month in range(1, 13):
        month_name = calendar.month_name[month]
        table.add_column(f"[bold magenta]{month_name}[/bold magenta]", justify="center")

    months = [calendar.monthcalendar(year, m) for m in range(1, 13)]
    max_weeks = max(len(month) for month in months)

    for week_index in range(max_weeks):
        row = []
        for month in months:
            if week_index < len(month):

                week = ["{:>2}".format(day) if day != 0 else "  " for day in month[week_index]]
                row.append(" ".join(week))
            else:
                row.append(" " * 20)  
        table.add_row(*row)

    console.print(table)

def display_month_calendar(year, month):
    """Display a specific month's calendar."""
    console.print(f"\n[bold cyan]{calendar.month_name[month]} {year}[/bold cyan]")
    month_calendar = calendar.monthcalendar(year, month)
    console.print("[bold magenta]Mo Tu We Th Fr Sa Su[/bold magenta]")
    for week in month_calendar:
        week_str = " ".join(["{:>2}".format(day) if day != 0 else "  " for day in week])
        console.print(week_str)

def main():
    console.print("[bold cyan]Welcome to the Dynamic Calendar Program![/bold cyan]\n")
    console.print("[bold yellow]1.[/bold yellow] Display full year calendar")
    console.print("[bold yellow]2.[/bold yellow] Display specific month calendar")
    console.print("[bold yellow]3.[/bold yellow] Exit\n")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            year = int(input("Enter the year: "))
            display_year_calendar(year)
        elif choice == "2":
            year = int(input("Enter the year: "))
            month = int(input("Enter the month (1-12): "))
            if 1 <= month <= 12:
                display_month_calendar(year, month)
            else:
                console.print("[bold red]Invalid month! Please enter a value between 1 and 12.[/bold red]")
        elif choice == "3":
            console.print("[bold green]Thank you for using the Calendar Program! Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]Invalid choice! Please select 1, 2, or 3.[/bold red]")

if __name__ == "__main__":
    main()

