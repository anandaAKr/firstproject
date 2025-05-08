from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def wishing(request):
    dt=datetime.now().date()
    tm=datetime.now().time()
    hr=tm.hour 

    if 6<= hr < 12:
        greetings="Good Morning"
    elif 12<=hr<16:
        greetings="Good Afternoon"
    elif 16<= hr<23:
        greetings="Good Evening"
    else:
        greetings="Go to sleep,Good Night"

        msg =f"""
         <html>
         <body bgcolor='yellow'text='red'>
      <center>
         <h1>Welcome to Django Web Development</h1>
         <h2>Date:{dt}</h2>
         <h2>time{tm.strftime('%H:%M:%S')}</h2>
         <h2>{greetings}</h2>
    </center>
   </body>
   </html> 
    """
        return HttpResponse(msg)
    
def StudentMarkList(response):
    data = [
        ["Sunil", 45, 49, 50], ["Jayaraj", 55, 51, 61],
        ["Reena", 91, 34, 87], ["Sheena", 60, 62, 67],
        ["Sony", 39, 38, 40], ["Bijoy", 85, 86, 89]
    ]
    
    # Setting table headings
    msg = """
    <html>
    <body>
    <center>
        <table width="600px" height="450px" cellpadding="10px" border="2" bgcolor="pink">
            <tr bgcolor="yellow">
                <td colspan="7" align="center"><b>Student Mark List</b></td>
            </tr>
            <tr bgcolor="cyan">
                <td><b>Name</b></td>
                <td><b>Mark-1</b></td>
                <td><b>Mark-2</b></td>
                <td><b>Mark-3</b></td>
                <td><b>Total</b></td>
                <td><b>Result</b></td>
                <td><b>Grade</b></td>
            </tr>
    """

    # Processing data to calculate total, result, and grade
    for row in data:
        sname, m1, m2, m3 = row
        tot = m1 + m2 + m3  # Calculating total marks

        # Determining pass/fail result
        result = "Failed" if m1 < 35 or m2 < 35 or m3 < 35 or tot < 120 else "Passed"

        # Determining grade
        if result == "Passed":
            if tot >= 240:
                grade = "O"
            elif tot >= 180:
                grade = "E"
            elif tot >= 150:
                grade = "G"
            else:
                grade = "A"
        else:
            grade = "-"  # Dash for failed students

        # Adding student data to the table
        msg += f"""
            <tr>
                <td>{sname}</td>
                <td>{m1}</td>
                <td>{m2}</td>
                <td>{m3}</td>
                <td>{tot}</td>
                <td>{result}</td>
                <td>{grade}</td>
            </tr>
        """

    msg += """
        </table>
    </center>
    </body>
    </html>
    """
    return HttpResponse(msg)