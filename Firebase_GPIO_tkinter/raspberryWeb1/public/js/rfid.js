//menu
$(function () {
    $.ajax({
        dataType: "json",
        url: "../menu.json",
        success: function(data){
            var menuHtml = "";
            jQuery.each(data,function(key,value){
                menuHtml += "<li><a href=\"/"+ value + "\">" + key + "</a></li>\n";
            });

            $("nav ul").append(menuHtml);
        }
    });


});

//sign in
$(function(){
    let $alertMessage = $(".alertMessage");
    $alertMessage.hide();
    $('.signIn').on('click',function(event){
         $alertMessage.slideDown(400);
        event.preventDefault();
        $('.cancel').on("click",function(event){
            $alertMessage.slideUp(400);
        })
    });

});

//menu
$(function(){
    var menuState = false;
    $("#menu").on("click touchstart",function(event){
        menuState = !menuState;
        let smallWindow = $(window).width() <= 767;
        if (menuState && smallWindow) {
            console.log("menu open");
            $(this).attr("src","images/close.png");
            $("nav>ul").css("display","block");
        }else{
            console.log("menu close");
            $(this).attr("src","images/menu.png");
            $("nav>ul").css("display","none");
        }
        event.preventDefault();
    });
    $(window).resize(function(event){
        //console.log(window.innerWidth)
        if(window.innerWidth > 767){
            $("nav>ul").show();
        }
    });
});

// Initialize Firebase

// Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyAHgSjntOofP5uFmmkHLTmuyCsS3f9OeSc",
    authDomain: "raspberryfirebase.firebaseapp.com",
    databaseURL: "https://raspberryfirebase.firebaseio.com",
    projectId: "raspberryfirebase",
    storageBucket: "raspberryfirebase.appspot.com",
    messagingSenderId: "929629322713",
    appId: "1:929629322713:web:f46ba539fe32c1868eedc8"
  };
  // Initialize Firebase
firebase.initializeApp(firebaseConfig);

//Authentication Of Firebase
firebase.auth().signInWithEmailAndPassword("robert1@gmail.com", "123456")
    .then(function(result){
        console.log("login 成功");
    })
    .catch(function(error) {
  // Handle Errors here.
  var errorCode = error.code;
  var errorMessage = error.message;
  console.log(errorCode,errorMessage)
  // ...
});



//progress interface
//提取firestore

let myFirebase = firebase.firestore();

//firebase
$(document).ready(() => {
     myFirebase.collection("Door").onSnapshot((querySnapshot) => {
        $accessDisplay = $("#accessDisplay");
        $accessDisplay.empty();
        querySnapshot.query.orderBy("timestamp",  "desc").limit(20).get().then((querySnapshot) => {
            querySnapshot.forEach((doc) => {
            console.log("姓名:" + doc.data().name + "\n" + "時間:" + doc.data().time);
            let name = doc.data().name;
            let time = doc.data().time;

            $user = $("<div class='user'><h3>" + name + "</h3><p>" + time + "</p></div>");
            $accessDisplay.append( $user);
            });
        });



    });

});
