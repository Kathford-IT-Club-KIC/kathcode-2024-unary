// JavaScript (using jQuery for simplicity)
$(document).ready(function() {
    $('.nav-links li a').click(function() {
        $('.nav-links li a').removeClass('active');
        $(this).addClass('active');
    });
});
