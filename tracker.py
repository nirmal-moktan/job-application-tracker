from datetime import datetime
import sqlite3
#CRUD Create, Read, Update and Delete items in the database
def create_database(): #makes sure the database file and table structure exist
    connection = sqlite3.connect("job_tracker.db") #creates a database if it does not exist
    cursor = connection.cursor() #doorway to our database, used when executing sql commands and managing and fetching results
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        job_title TEXT NOT NULL,
        location TEXT NOT NULL,
        deadline TEXT NOT NULL,
        start_date TEXT NOT NULL,
        status TEXT NOT NULL
        )
    """)
    connection.commit() #saves the table
    connection.close()

def add_applications(new_application):
    validate_text(new_application["company"])
    validate_text(new_application["job_title"])
    validate_text(new_application["location"])
    validate_date(new_application["deadline"])
    validate_date(new_application["start_date"])
    new_application["status"] = validate_status(new_application["status"])
    connection = sqlite3.connect("job_tracker.db") #opens the database to insert data
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO applications
    (company, job_title, location, deadline, start_date, status)
    VALUES (?,?,?,?,?,?)
    """,(
        new_application["company"],
        new_application["job_title"],
        new_application["location"],
        new_application["deadline"],
        new_application["start_date"],
        new_application["status"]   
    ))
    connection.commit()
    connection.close()
    
    #next_id = max(applications, default=0) + 1
    #applications[next_id] = new_application
    return "New application added."

def view_applications(applications):
    for application_id, application in applications.items():
        print(f"Application {application_id}")
        for title, information in application.items():
            print(f"{title}: {information}")
            
def update_applications(applications, application_id, company ="", job_title="",location="", 
                        deadline ="", status="", start_date=""):
    if application_id not in applications:
        return "Application not found."  
    application = applications[application_id]
    if company:
        validate_text(company)
        application["company"] = company
    if job_title:
        validate_text(job_title)
        application["job_title"] = job_title
    if location:
        validate_text(location)
        application["location"] = location
    if deadline:
        validate_date(deadline)
        application["deadline"] = deadline
    if status:
        application["status"] = validate_status(status)
    if start_date:
        validate_date(start_date)
        application["start_date"] = start_date
    return "Application updated."
    

def delete_applications(applications, application_id):
    if application_id not in applications:
        return "Application not found."
    del applications[application_id]
    return f"Application {application_id} deleted."
    
def validate_text(value: str): #validates company name, job title and location inputs
    if not value.strip():
        raise ValueError('This entry cannot be empty!')
def validate_date(date): #validates start date and deadline inputs
    try:
        datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        raise ValueError('Please enter date in correct format: YYYY-MM-DD')
def validate_status(status: str): #validates status input from the allowed options
    valid_status = {'Applied','Interview','Offer','Accepted','Rejected','Withdrawn','No Response'}
    cleaned_status = status.title().strip()
    if cleaned_status not in valid_status:
        raise ValueError('Invalid status: please enter Applied, Interview, Offer, Accepted, Rejected, Withdrawn, or No Response')
    return cleaned_status