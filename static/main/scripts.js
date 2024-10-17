document.addEventListener('DOMContentLoaded', function() {
    const catalogToggle = document.getElementById('catalog-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    catalogToggle.addEventListener('click', function(event) {
        event.preventDefault(); // Отменяем переход по ссылке
        dropdownMenu.classList.toggle('show'); // Переключаем класс "show"
    });

    // Закрываем меню, если клик был вне области меню
    document.addEventListener('click', function(event) {
        if (!catalogToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove('show');
        }
    });
});
