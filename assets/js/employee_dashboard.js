const pending_list = document.querySelector("#pending");
const completed_list = document.querySelector("#completed");

const pending_tab =   document.getElementById("pending_tab");
const completed_tab = document.getElementById("completed_tab");

 pending_tab.addEventListener("click"  , ()=>{
    console.log("pending");
    pending_list.style.display  ="block";
    completed_list.style.display = "none";
});

 completed_tab.addEventListener("click"  , ()=>{
    console.log("completed");
    pending_list.style.display  ="none";
    completed_list.style.display = "block";
});