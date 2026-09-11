def add_applications(applications, new_application):
    next_id = len(applications) + 1
    applications[next_id] = new_application
    return f"New application added."

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
        application["company"] = company
    if job_title:
        application["job_title"] = job_title
    if location:
        application["location"] = location
    if deadline:
        application["deadline"] = deadline
    if status:
        if status in [
            "Applied",
            "Interview",
            "Offer",
            "Accepted",
            "Rejected",
            "Withdrawn"
        ]:
         application["status"] = status
        else:
            return "Invalid status."
    if start_date:
        application["start_date"] = start_date
    return "Application updated."
    

def delete_applications(applications, application_id):
    if application_id not in applications:
        return "Application not found."
    del applications[application_id]
    return f"Application {application_id} deleted."
    
