// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
    const socialIcons = document.querySelectorAll('.social-media a');

    // Add event listener for hover effect
    socialIcons.forEach(icon => {
        icon.addEventListener('mouseover', function () {
            // Toggle animation class on hover
            this.classList.toggle('animate-bounce');
        });
        icon.addEventListener('animationend', function () {
            // Remove animation class when animation ends
            this.classList.remove('animate-bounce');
        });
    });
    // Animation for the home section
    gsap.from('.home-content', {
        opacity: 0,
        y: 100,
        duration: 1,
        delay: 0.5
    });

    gsap.from('.home-img', {
        opacity: 0,
        x: 100,
        duration: 1,
        delay: 0.7
    });

    gsap.from('.social-media a', {
        opacity: 0,
        y: -50,
        duration: 1,
        delay: 1.2,
        stagger: 0.2,
        ease: 'bounce.out'
    });

});
