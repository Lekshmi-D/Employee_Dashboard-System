// const pending_list = document.querySelector("#pending");
// const completed_list = document.querySelector("#completed");

// const pending_tab =   document.getElementById("pending_tab");
// const completed_tab = document.getElementById("completed_tab");



//  pending_tab.addEventListener("click"  , ()=>{
//     console.log("pending");
//     pending_list.style.display  ="block";
//     completed_list.style.display = "none";
// });

//  completed_tab.addEventListener("click"  , ()=>{
//     console.log("completed");
//     pending_list.style.display  ="none";
//     completed_list.style.display = "block";
// });


const tasks = document.getElementsByClassName("singleTask");

const taskView = document.querySelector(".viewTask");

var csrftoken = getCookie('csrftoken');


console.log("hello world")

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

Array.from(tasks).forEach((element) => {

    element.addEventListener("click", (event) => {

        console.log(event.target.className);
        if (event.target.className == "singleTask") {


            console.log("clicked on ", event.target)

            console.log("showing");

            // taskView.style.display = "flex";
            console.log(element.getElementsByClassName("title")[0].textContent);
            taskView.getElementsByClassName("task_title")[0].textContent = `Title:       ${element.getElementsByClassName("title")[0].textContent}`;
            taskView.getElementsByClassName("task_due_date")[0].textContent = `Due:         ${element.getElementsByClassName("due_date")[0].textContent}`;
            taskView.getElementsByClassName("task_assigned_by")[0].textContent = `assigned by: ${element.getElementsByClassName("assigned_by")[0].textContent}`;
            taskView.getElementsByClassName("task_status")[0].textContent = `status       ${element.getElementsByClassName("select_status")[0].value}`;
            taskView.getElementsByClassName("task_description")[0].textContent = `${element.getElementsByClassName("description")[0].textContent}`;

            taskView.style.display = "flex";
        }
    })


    var status_select = element.getElementsByClassName("select_status")[0];
    status_select.addEventListener("change", () => {

        let confirm_button = element.getElementsByClassName("confirm")[0];
        confirm_button.style.display = "flex";

        confirm_button.addEventListener("click", async (event) => {

            event.preventDefault();

            let data = {
                "type": "update",
                "id": element.id,
                "status": status_select.value,
                // "username":"navadeep_satheesh"
            }

            let params = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    'X-CSRFToken': csrftoken
                },
                credentials: 'same-origin',
                body: JSON.stringify(data)
            }

            await fetch("/employees/operations", params).then((response) => {
                return response.text()
            }).then((data) => {
                console.log(data)
                if (data == "done") {
                    
                    if(document.querySelector(".page_heading").innerText!="Assigned"){
                        console.log("removing")
                        element.remove();
                    }
                    confirm_button.style.display = "none";

                }
            })


        })
    })

});

const close_task_view = document.querySelector(".close_task_view");
close_task_view.addEventListener("click", () => {
    taskView.style.display = "none";
})

const change_password = document.getElementById("change_password");
const changePasswordBox = document.querySelector(".changePassword");

change_password.addEventListener("click", () => {
    console.log("openign change password");
    changePasswordBox.style.display = "flex";
})

const change_password_button = document.getElementById("change_password_button");
change_password_button.addEventListener("click", () => {

    let current_password = document.getElementById("current_password");
    let new_password = document.getElementById("new_password");
    let new_password2 = document.getElementById("new_password2");

    if (new_password.value == new_password2.value) {

        data = {
            type: 'change_password',
            current_password: current_password,
            new_password: new_password,

        }
        params = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        }
        fetch("/employee/operations", params).then((data) => {
            return data.text()
        }).then((text) => {
            console.log(text);
        })
    } else {
        console.log("passwords are not the same");
        document.getElementById("change_password_warning").innerText = "passwords dont match";
    }

})










