const form = document.getElementById("umugandaForm");

window.addEventListener("DOMContentLoaded", () => {
    form.addEventListener("submit", function(e) {
        e.preventDefault();
        const data = new FormData(this);
        const umuganda_date = data.get("umuganda_date");
        const title = data.get("title");
        const description = data.get("description");
        // const created_by = document.getElementById("created_by");
        const location = data.get("location");
        const start_time = data.get("start_time");
        const end_time = data.get("end_time");

        const submit_data = {
            title, description, umuganda_date, location, start_time, end_time
        }

        // console.log(submit_data);

        // const token = {
        //     "X-CSRFToken": document.querySelector("meta[name='csrf-token']").content
        // }

    apiRequest("/umuganda", "POST", submit_data)
        .then(response => {
            if (response.status === "failed") alert(response.msg);
            else if (response.status === "success") {
                alert("Umuganda was created successfully !!");
                form.reset();
                window.location.reload();
            };
        })
        .catch(err => alert(err));
    })
})
