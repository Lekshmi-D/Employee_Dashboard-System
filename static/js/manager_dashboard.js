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


const tasks = document.getElementsByClassName("singleTask");

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


});

const create_task =  document.getElementById("createTask");
const create_task_submit = document.querySelector(".create_task_submit");
const create_task_box =  document.querySelector(".new_task");

const close_button =  document.querySelector(".close_task_create");

create_task.addEventListener("click" , ()=>{
    console.log("showing box")
    create_task_box.style.display = "flex";
    
})
close_button.addEventListener("click" , ()=>{
    create_task_box.style.display = "none";
    console.log("close")
});

create_task_submit.addEventListener("click" , (event)=>{

    event.preventDefault();

    let csrftoken = getCookie('csrftoken');

    console.log(document.querySelector(".date").value)
    
    let data = {
        "type":"new_task",
        "title": document.querySelector(".task_title").value,
        "assigned_to": document.querySelector(".assigned_to").value,
        "date": document.querySelector(".date").value,
        "description": document.querySelector(".description").value,
        "username": "navadeep_manager",
        
    }
    console.log(document.querySelector(".title").value)
    console.log(JSON.stringify(data))
    let params = {
        method : "POST",
        headers : {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        credentials: 'same-origin',
        body: JSON.stringify(data)
    }   

    fetch("/manager/manager_operations", params).then((response)=>{
        return response.text();
    }).then((data)=>{
        console.log(data);
        create_task_box.style.display = "none";
        
    } )
    

    

})
