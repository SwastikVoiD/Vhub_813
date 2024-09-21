const tabs = document.querySelectorAll('#tabs li');
const tabContents = document.querySelectorAll('#tabs > div');

tabs.forEach((tab) => {
    tab.addEventListener('click', (e) => {
        const target = e.target.getAttribute('href');
        tabContents.forEach((content) => {
            content.style.display = 'none';
        });
        document.querySelector(target).style.display = 'block';
    });
});