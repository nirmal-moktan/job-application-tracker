def add_applications(applications, new_application):
    next_id = len(applications) + 1
    applications[next_id] = new_application

def view_applications(applications):
    for application_id, application in applications.items():
        print(f"Application {application_id}")
        for title, information in application.items():
            print(f"{title}: {information}")
            
def update_applications(applications, update):
    application_update = []
    

def delete_applications(applications):
    pass
applications = {
    1: {
        "company": "Jacksonville State University",
        "job_title": "Software Engineering Intern",
        "location": "Jacksonville, AL",
        "deadline": "2026-10-01",
        "status": "Applied",
        "start_date": "2027-01-15"
    },

    2: {
        "company": "Regions Bank",
        "job_title": "Technology Intern",
        "location": "Birmingham, AL",
        "deadline": "2026-10-15",
        "status": "Interview",
        "start_date": "2027-05-20"
    },

    3: {
        "company": "Southern Company",
        "job_title": "Software Developer Intern",
        "location": "Atlanta, GA",
        "deadline": "2026-09-20",
        "status": "Rejected",
        "start_date": "2027-05-15"
    }
}

new_application = {
    "company": "Blue Cross Blue Shield of Alabama",
    "job_title": "IT Intern",
    "location": "Birmingham, AL",
    "deadline": "2026-11-01",
    "status": "Applied",
    "start_date": "2027-05-25"
}
