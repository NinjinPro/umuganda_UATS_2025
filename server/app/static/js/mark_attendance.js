document.addEventListener("DOMContentLoaded", () => {
    const attendanceList = document.querySelector(".attendance-list");
    const umugandaId = window.currentUmugandaId; // set this variable when admin selects an event

    // Fetch citizens dynamically
    fetch("/admin/citizens")
        .then(res => res.json())
        .then(data => {
            attendanceList.innerHTML = "";
            data.citizens.forEach(citizen => {
                const div = document.createElement("div");
                div.classList.add("citizen");
                div.innerHTML = `
                    <span>${citizen.name}</span>
                    <label>
                        <input type="checkbox" data-id="${citizen.id}">
                        Present
                    </label>
                `;
                attendanceList.appendChild(div);
            });

            // Add event listeners to checkboxes
            attendanceList.querySelectorAll("input[type=checkbox]").forEach(cb => {
                cb.addEventListener("change", () => {
                    const citizenId = cb.dataset.id;
                    const status = cb.checked ? "present" : "absent";

                    fetch("/admin/mark_attendance", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            citizen_id: citizenId,
                            umuganda_id: umugandaId,
                            status: status
                        })
                    })
                    .then(res => res.json())
                    .then(response => {
                        if (response.success) {
                            console.log(`Citizen ${citizenId} marked as ${status}`);
                        } else {
                            console.error("Error:", response.error);
                        }
                    })
                    .catch(err => console.error("Fetch Error:", err));
                });
            });
        });
});
