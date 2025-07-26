document.addEventListener("DOMContentLoaded", () => {
    const directions = document.querySelectorAll(".sidebar a");
    const sections = document.querySelectorAll(".section");

    directions.forEach(dir => {
        dir.addEventListener("click", e => {
            e.preventDefault();

            directions.forEach(l => l.parentElement.classList.remove("active"));
            dir.parentElement.classList.add("active");

            sections.forEach(sec => sec.classList.remove("active"));
            document.getElementById(dir.dataset.section).classList.add("active");
        });
    });

    document.getElementById("send-btn")?.addEventListener("click", () => {
        const input = document.getElementById("chat-input");
        const message = input.value.trim();
        if (!message) return;

        const msgBox = document.getElementById("chat-messages");
        const newMsg = document.createElement("p");
        newMsg.innerHTML = `<strong>You:</strong> ${message}`;
        msgBox.appendChild(newMsg);
        input.value = "";

        msgBox.scrollTop = msgBox.scrollHeight;
    });
});
