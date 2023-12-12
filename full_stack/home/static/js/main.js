(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


// Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
})(jQuery);


/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    const dropdown = document.getElementById("myDropdown")
    const button = document.querySelector('.dropbtn')
    dropdown.classList.toggle("show");

// Close the dropdown if the user clicks outside of it
    document.addEventListener('click', e => {
        if (!e.composedPath().includes(dropdown) && !e.composedPath().includes(button)
        ) {
            dropdown.classList.remove("show")
        }
    })
}

function myFunctionNotif() {
    const dropdown = document.getElementById("myDropdownNotif")
    const button = document.querySelector('.dropbtnnotif')
    dropdown.classList.toggle("show");

// Close the dropdown if the user clicks outside of it
    document.addEventListener('click', e => {
        if (!e.composedPath().includes(dropdown) && !e.composedPath().includes(button)
        ) {
            dropdown.classList.remove("show")
        }
    })
}

//! log in
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('containerlog');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

