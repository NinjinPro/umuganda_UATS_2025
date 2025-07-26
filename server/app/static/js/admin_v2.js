const directions = document.querySelectorAll('.sidebar nav a');
const sections = document.querySelectorAll('.section');

directions.forEach(dir => {
    dir.addEventListener('click', (e) => {
        e.preventDefault();
        directions.forEach(l => l.parentElement.classList.remove('active'));
        dir.parentElement.classList.add('active');
        
        const sectionId = dir.dataset.section;
        sections.forEach(sec => sec.classList.remove('active'));
        document.getElementById(sectionId).classList.add('active');
    });
});