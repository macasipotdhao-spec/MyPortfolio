document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // Reveal animations on scroll
    const reveals = document.querySelectorAll('.reveal');
    const animateOnScroll = () => {
        reveals.forEach(element => {
            const windowHeight = window.innerHeight;
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Run once on load

    // Hero initial animation
    const heroH1 = document.querySelector('.hero h1');
    const heroP = document.querySelector('.hero p');

    setTimeout(() => {
        if (heroH1) {
            heroH1.style.opacity = '1';
            heroH1.style.transform = 'translateY(0)';
            heroH1.style.transition = 'all 1s ease-out';
        }
    }, 300);

    setTimeout(() => {
        if (heroP) {
            heroP.style.opacity = '1';
            heroP.style.transform = 'translateY(0)';
            heroP.style.transition = 'all 1s ease-out';
        }
    }, 500);

    // Smooth smooth scrolling for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
