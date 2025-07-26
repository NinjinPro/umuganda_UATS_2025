document.addEventListener('DOMContentLoaded', function () {
    function safeBase64(str) {
    return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, (_, p1) =>
        String.fromCharCode(parseInt(p1, 16))
    ));
    }

    const flashMessages = document.querySelectorAll('.flash-message');

    flashMessages.forEach((msg) => {
        const messageText = msg.textContent.trim(); // Includes message + close button if inline
        const hash = safeBase64(messageText).slice(0, 30); // simple safe hash

        if (localStorage.getItem(`dismissed_flash_${hash}`)) {
            msg.remove();
            return;
        }

        // auto remove
        setTimeout(() => {
            msg.classList.add('fade-out');
            setTimeout(() => msg.remove(), 1000);
        }, 5000);

        // manual removal
        const closeBtn = msg.querySelector('.close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                localStorage.setItem(`dismissed_flash_${hash}`, 'true');
                msg.remove();
            });
        }
    });
});
