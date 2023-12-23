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

//! LOG IN CLOSE
// document.addEventListener('DOMContentLoaded', function () {
//     const modal = document.getElementById("containerlog");

//     function closeModal() {
//         if (modal.classList.contains("show")) {
//             modal.classList.remove("show");
//             // Set backdrop opacity to 0 when modal is closed
//             setBackdropOpacity(0);
//         }
//     }

//     function openModal() {
//         if (!modal.classList.contains("show")) {
//             modal.classList.add("show");
//             // Set backdrop opacity to 0.5 when modal is opened
//             setBackdropOpacity(0.5);
//         }
//     }

//     document.addEventListener('click', function (e) {
//         const target = e.target;

//         // Check if the clicked element is outside the modal
//         if (!modal.contains(target)) {
//             closeModal();
//         }
//     });

//     // You can add additional logic to open the modal (e.g., a button click)
//     // For example, you can open the modal when clicking a button with id="openModal"
//     const openModalButton = document.getElementById("openModal");
//     if (openModalButton) {
//         openModalButton.addEventListener('click', openModal);
//     }

//     // You can also add logic to close the modal (e.g., a button click inside the modal)
//     // For example, you can close the modal when clicking a button with id="closeModal"
//     const closeModalButton = document.getElementById("closeModal");
//     if (closeModalButton) {
//         closeModalButton.addEventListener('click', closeModal);
//     }

//     // Function to set backdrop opacity
//     function setBackdropOpacity(opacity) {
//         const backdrop = document.querySelector('.modal-backdrop');
//         if (backdrop) {
//             backdrop.style.opacity = opacity;
//         }
//     }
// });



// ! DRIVER JS
const driver = window.driver.js.driver;

function homeInfo() {
    const driverObj = driver({
        showProgress: true,
        steps: [
          { element: '#information', popover: {title: "Info",description: "Click here to learn about the parts of the website that you do not understand." } },
          { element: '#login-signup', popover: { title: 'Log In & Sign Up', description: 'Click for user login and user registration.' } },
          { element: '.dropdownnotif', popover: { title: 'Notifications', description: 'Your notifications appear here.' } },
          { element: '.search-box', popover: { title: 'Search', description: 'Type to search.' } },
          { element: '.card', popover: { title: 'Card', description: 'Posts appear here.' } },
          { element: '.card-img-top', popover: { title: 'Card Image', description: 'Card image appear here.' } },
          { element: '.card-body', popover: { title: 'Card Body', description: 'Card informations appears here.' } },
          { element: '#card-user', popover: { title: 'Card User Name', description: 'Name and surname of the user who created the card.' } },
          { element: '#card-content', popover: { title: 'Card Content', description: 'Card content appear here.' } },
          { element: '#card-create', popover: { title: 'Card Creation Date', description: 'Card creation date appear here.' } },
          { element: '#card-detail', popover: { title: 'Card Detail', description: 'Click to comment on the card or get more information.' } },
        ]
      });

    driverObj.drive();
}

function detailInfo() {
    const driverObj = driver({
        showProgress: true,
        steps: [
          { element: '#containerdetail', popover: { title: 'Card', description: 'Posts appear here.' } },
          { element: '.card-img-top', popover: { title: 'Card Image', description: 'Card image appear here.' } },
          { element: '.card-body', popover: { title: 'Card Body', description: 'Card informations appears here.' } },
          { element: '#card-user', popover: { title: 'Card User Name', description: 'Name and surname of the user who created the card.' } },
          { element: '#card-content', popover: { title: 'Card Content', description: 'Card content appear here.' } },
          { element: '#card-create', popover: { title: 'Card Creation Date', description: 'Card creation date appear here.' } },
          { element: '#card-detail-comments', popover: { title: 'Card Comments', description: 'Card comments appears here.' } },
        ]
      });

    driverObj.drive();
}

function searchInfo() {
    const driverObj = driver({
        showProgress: true,
        steps: [
          { element: '#carddetail', popover: { title: 'Card', description: 'Posts appear here.' } },
          { element: '.card-img-top', popover: { title: 'Card Image', description: 'Card image appear here.' } },
          { element: '.card-body', popover: { title: 'Card Body', description: 'Card informations appears here.' } },
          { element: '#card-user', popover: { title: 'Card User Name', description: 'Name and surname of the user who created the card.' } },
          { element: '#card-content', popover: { title: 'Card Content', description: 'Card content appear here.' } },
          { element: '#card-create', popover: { title: 'Card Creation Date', description: 'Card creation date appear here.' } },
          { element: '#card-detail', popover: { title: 'Card Detail', description: 'Click to comment on the card or get more information.' } },

        ]
      });

    driverObj.drive();
}