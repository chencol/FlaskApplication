$(function() {
  $("#login_btn").bind("click", function(event) {
    event.preventDefault();
    $.ajax({
        url:env.base_api_url + "verify_user",
        xhrFields: {
            withCredentials: true
        },
        method:"POST",
        data:{
            name: $('input[id="username"]').val(),
            password: $('input[id="password"]').val()
        },
        success:function(data) {
            if (data.result != "true") {
              $("#login_error").css("color", "red");
              $("#login_error").css("opacity", "1");
              $("#login_error").text("Wrong username or password!");
            } else {
              username = data.username;
              $("#login_error").css("color", "black");
              $("#login_error").css("opacity", "1");
              $("#login_error").text(
                "Welcome home! Dear " + username + "! We are now bring u home!"
              );
              localStorage.setItem("access_token", data.token);
              localStorage.setItem("username", data.username);
//              sessionStorage.setItem("access_token", data.token);
//              sessionStorage.setItem("username", data.username);
              setTimeout(function() {
                   window.location.href = env.base_url + "home.html";
              }, 2000);
            }
        },
        error:function(){
            alert("error");
        }
    });
  })
})



