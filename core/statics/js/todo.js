document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("todoForm");
    const input = document.getElementById("todoInput");
    const list = document.getElementById("todoList");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const text = input.value.trim();
        if (!text) return;

        addTask(text);
        input.value = "";
    });

    function addTask(text) {
        const li = document.createElement("li");
        li.className = "list-group-item d-flex justify-content-between align-items-center";

        li.innerHTML = `
            <span class="task-text">${text}</span>
            <div>
                <button class="btn btn-success btn-sm me-2 complete-btn">✓</button>
                <button class="btn btn-danger btn-sm delete-btn">✕</button>
            </div>
        `;

        // complete
        li.querySelector(".complete-btn").addEventListener("click", () => {
            li.classList.toggle("completed");
        });

        // delete
        li.querySelector(".delete-btn").addEventListener("click", () => {
            li.remove();
        });

        list.appendChild(li);
    }
});