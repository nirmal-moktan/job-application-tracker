# Job Application Tracker

A full-stack web application built with Python, Flask, SQLite, HTML, CSS, and JavaScript for tracking and managing job applications.

This project started as a Python command-line application and evolved into a full-stack web application. It was built to practice how a frontend interface, Flask backend, application logic, and database work together in a complete software project.

## Features

- Add new job applications through the web interface
- View saved applications in a structured table
- Edit existing application information
- Delete applications with confirmation
- Update application status directly from the table
- Store application data persistently using SQLite
- Validate text, dates, and application status
- Use a built-in date picker for application dates
- Use dropdown menus for application status
- Use modal windows for adding, editing, and deleting applications
- Keep stable application IDs even after records are deleted

## Application Information

Each job application stores:

- Company
- Job title
- Location
- Applied date
- Status
- Remarks

Supported application statuses include:

- Applied
- Interview
- Offer
- Accepted
- Rejected
- Withdrawn
- No Response

## Technologies

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Jinja
- Git
- GitHub

## Application Architecture

```text
Browser
↓
HTML / CSS / JavaScript
↓
Flask
↓
Python application logic
↓
SQLite database
```

The browser provides the user interface. Flask handles web requests and connects the frontend to the Python application logic. SQLite stores application data persistently.

## Project Structure

```text
job-application-tracker/
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── main.py
├── tracker.py
├── .gitignore
└── README.md
```

## Current Functionality

The application currently supports full CRUD functionality from the web interface:

- Create new job applications
- Read and display saved applications
- Update application information
- Update application status
- Delete applications
- Persist all changes in SQLite

The interface also includes:

- Add Application modal
- Edit Application modal with pre-filled application data
- Delete confirmation modal
- Status dropdowns
- Date picker input
- JavaScript-powered modal interactions

## Project Status

This project is actively being improved.

### Planned Improvements

- Improve the overall visual design
- Improve responsiveness for different screen sizes
- Add clearer user-facing validation messages
- Improve modal animations and interactions
- Add screenshots and project demonstrations
- Explore public deployment

## Purpose

The goal of this project is to build a practical tool while developing a stronger understanding of full-stack software development.

Through this project, I practiced:

- Connecting a frontend interface to a Python backend
- Handling browser requests with Flask
- Performing CRUD operations with SQLite
- Validating user input
- Passing data between Flask and Jinja templates
- Using JavaScript for client-side interactions
- Managing project changes with Git and GitHub

## Future Direction

The project will continue to be refined with improved styling, usability, and deployment options while keeping the application simple and practical.