const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// timeout function to remove error message automatically
setTimout(function(){
    $('#message').fadeOut('slow');
}, 3000);