document.addEventListener('DOMContentLoaded', function () {
    const dropdownButton = document.querySelector('button.bg-white.text-sky-600');
    const dropdownContent = document.querySelector('.dropdown-content');

    if (dropdownButton && dropdownContent) {

        dropdownButton.addEventListener('click', function (event) {
            event.stopPropagation();
            dropdownContent.classList.toggle('hidden');
        });

        window.addEventListener('click', function (event) {
            if (!dropdownButton.contains(event.target) && !dropdownContent.contains(event.target)) {
                dropdownContent.classList.add('hidden');
            }
        });
    }
});
