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

    element.addEventListener("click" , ()=>{

        console.log("showing");

        // taskView.style.display = "flex";
        console.log(element.getElementsByClassName("title")[0].textContent);
        taskView.getElementsByClassName("task_title")[0].textContent =       `Title:       ${element.getElementsByClassName("title")[0].textContent}`;
        taskView.getElementsByClassName("task_due_date")[0].textContent =    `Due:         ${element.getElementsByClassName("due_date")[0].textContent}`;
        taskView.getElementsByClassName("task_assigned_by")[0].textContent = `assigned by: ${element.getElementsByClassName("assigned_by")[0].textContent}`;
        taskView.getElementsByClassName("task_status")[0].textContent =      `status       ${element.getElementsByClassName("select_status")[0].value}`;
        taskView.getElementsByClassName("task_description")[0].textContent = `${element.getElementsByClassName("description")[0].textConten}`;

        taskView.style.display = "flex";
    })


    var status_select = element.getElementsByClassName("select_status")[0];
    status_select.addEventListener("change" , ()=>{ 
        
        let confirm_button = element.getElementsByClassName("confirm")[0];
        confirm_button.style.display = "flex";

        confirm_button.addEventListener("click" ,async  (event)=>{

            event.preventDefault();

            let data = {
                "type" :"update",
                "id" : element.id ,
                "status":  status_select.value ,
                // "username":"navadeep_satheesh"
            }

            let csrftoken = getCookie('csrftoken');

            let params = {
                method : "POST",
                headers : {
                    "Content-Type": "application/json",
                    'X-CSRFToken': csrftoken
                },
                credentials: 'same-origin',
                body: JSON.stringify(data)
            }

            await fetch("/employees/operations", params).then(  (response)=>{
                return response.text()
            } ).then((data)=>{
                console.log(data)
                if(data == "done"){

                    element.remove()
                }
            })


        })
    })
    
});









