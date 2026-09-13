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

def view_applications():
    connection = sqlite3.connect("job_tracker.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from applications") #select every element from the applications table
    applications = cursor.fetchall()

    for application in applications:
        print(application)
    connection.close()
            
def update_applications(application_id, company ="", job_title="",location="", 
                        deadline ="", status="", start_date=""):
    try:
        application_id = int(application_id)
    except (ValueError, TypeError):
        return "Application id must be an integer."  
    connection = sqlite3.connect("job_tracker.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM applications WHERE id = ?",(application_id,))
    application = cursor.fetchone()
    if application is None:
        connection.close()
        return "Application not found."
    
    if company:
        validate_text(company)
        cursor.execute("UPDATE applications SET company = ? WHERE id = ?",(company,application_id))
    if job_title:
        validate_text(job_title)
        cursor.execute("UPDATE applications SET job_title = ? WHERE id = ?",(job_title, application_id))
    if location:
        validate_text(location)
        cursor.execute("UPDATE applications SET location = ? WHERE id = ?",(location, application_id))
    if deadline:
        validate_date(deadline)
        cursor.execute("UPDATE applications SET deadline = ? WHERE id = ?",(deadline, application_id))
    if status:
        status = validate_status(status)
        cursor.execute("UPDATE applications SET status = ? WHERE id = ?",(status, application_id))
    if start_date:
        validate_date(start_date)
        cursor.execute("UPDATE applications SET start_date = ? WHERE id = ?",(start_date, application_id))
    connection.commit()
    connection.close()    
    return "Application updated."
    

def delete_applications(application_id):
    try:
        application_id = int(application_id)
    except ValueError:
        return "Application id must be an integer."
    connection = sqlite3.connect("job_tracker.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM applications WHERE id = ?",(application_id,)) #the trailing comma means it is a tuple containing one item
    #sqlite also only deletes if id is present if non existent id is passes accidently no row will be deleted
    if cursor.rowcount == 0: #no row deleted
        connection.close()
        return "Application id not found"
    connection.commit()
    connection.close()
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