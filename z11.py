def month(n):
    n -= 1
    months = [
        "January",
        "Febuary", 
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    return months[n]

print(month(12))