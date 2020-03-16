$(document).ready(function() {
//    token = sessionStorage.getItem("access_token")
    token = localStorage.getItem("access_token")
    if(token!=null){
        $.ajax({
            url:env.base_api_url + "access_control",
            xhrFields: {
                withCredentials: true
            },
            method:"GET",
            data:{
                token: token
            },
            success:function(data) {
                document.getElementById("greet").innerHTML = "Hello " + localStorage.getItem("username");
            },
            error:function(){
                alert("error");
            }
        })
    }else{
        window.location.href = env.base_url + "login.html"
    }
});