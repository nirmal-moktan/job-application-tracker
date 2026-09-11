from tracker import add_applications
from tracker import view_applications
from tracker import update_applications
from tracker import delete_applications

################ Sample Data #####################
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

def main():
    view_applications(applications)


if __name__ == "__main__":
    main()