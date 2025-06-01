// app/static/js/main.js

console.log("main.js carregado!");

document.addEventListener('DOMContentLoaded', function() {
    // Efeito de Digitação com Typed.js
    const typedTextElement = document.getElementById('typed-text');
    
    if (typedTextElement) {
        const stringsToType = [
            "Desenvolvedor Full Stack",
            "Entusiasta de Python",
            "Apaixonado por Tecnologia",
            "Criador de Soluções Web"
        ];

        new Typed('#typed-text', {
            strings: stringsToType,
            typeSpeed: 70, // Velocidade de digitação em milissegundos
            backSpeed: 50, // Velocidade de "backspace" em milissegundos
            backDelay: 1000, // Tempo de espera antes de começar o backspace
            startDelay: 500, // Tempo de espera antes de começar a digitar
            loop: true, // Repetir a animação
            showCursor: true,
            cursorChar: '|',
        });
    }

    // Theme Toggle Functionality
    const themeToggleButton = document.getElementById('theme-toggle');
    const bodyElement = document.body;
    const sunIcon = document.querySelector('.theme-icon-sun');
    const moonIcon = document.querySelector('.theme-icon-moon');
    const preferedTheme = localStorage.getItem('theme');

    const applyTheme = (theme) => {
        if (theme === 'light') {
            bodyElement.classList.add('light-theme');
            sunIcon.classList.add('d-none');
            moonIcon.classList.remove('d-none');
        } else {
            bodyElement.classList.remove('light-theme');
            sunIcon.classList.remove('d-none');
            moonIcon.classList.add('d-none');
        }
    };

    // Apply saved theme on load or default to dark
    if (preferedTheme) {
        applyTheme(preferedTheme);
    } else {
        applyTheme('dark'); // Default theme
    }

    if (themeToggleButton) {
        themeToggleButton.addEventListener('click', () => {
            if (bodyElement.classList.contains('light-theme')) {
                applyTheme('dark');
                localStorage.setItem('theme', 'dark');
            } else {
                applyTheme('light');
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // Outras interações JavaScript do portfólio podem vir aqui
    // Ex: Scroll suave, animações ao rolar, etc.
});

// Futuro código JavaScript para interatividade do portfólio 