// ==== JS PERSONALIZADO ====

document.addEventListener('DOMContentLoaded', () => {
    console.log('CursosDjango está corriendo 🤖');

    const titulo = document.querySelector('h1');
    if (titulo) {
        titulo.addEventListener('mouseenter', () => {
            titulo.style.color = '#0d6efd';
        });
        titulo.addEventListener('mouseleave', () => {
            titulo.style.color = '';
        });
    }
});
