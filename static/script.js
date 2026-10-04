const addButton = document.getElementById("add-application-button");
const addModal = document.getElementById("add-modal");

addButton.addEventListener("click", function () {
    addModal.hidden = false;
});

const cancelButton = document.getElementById("cancel-add-button");
const applicationForm = document.getElementById("add-application-form");
cancelButton.addEventListener("click", function(){
    applicationForm.reset();
    addModal.hidden = true;
});

const editButtons = document.querySelectorAll(".edit-button");
const editModal = document.getElementById("edit-modal");

editButtons.forEach(function (button){
    button.addEventListener("click", function(){
        document.getElementById("edit-company").value = button.dataset.company;
        document.getElementById("edit-job-title").value = button.dataset.jobTitle;
        document.getElementById("edit-location").value = button.dataset.location;
        document.getElementById("edit-date").value = button.dataset.date;
        document.getElementById("edit-status").value = button.dataset.status;
        document.getElementById("edit-remark").value = button.dataset.remark;
        
        editModal.hidden = false;

    });
}); 
const cancelEditButton = document.getElementById("cancel-edit-button");
cancelEditButton.addEventListener("click",function(){
    editModal.hidden = true;
});


