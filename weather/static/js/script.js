
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function () {
        document.body.classList.add("search-active");
    });
});
// Chatbot Logic
function toggleChat() {
    const box = document.getElementById("chatBox");
    box.classList.toggle("hidden");
}

function sendMessage() {
    let input = document.getElementById("userInput");
    let msg = input.value.trim();
    if (!msg) return;

    let chat = document.getElementById("chatMessages");

    // USER MESSAGE
    chat.innerHTML += `
        <div class="flex justify-end">
            <div class="bg-sky-600 text-white p-2 rounded-full rounded-tr-none max-w-xs text-sm">
                ${msg}
            </div>
        </div>
    `;

    input.value = "";

    // BOT LOADING (placeholder for now)
    let loader = document.createElement("div");
    loader.id = "typing";
    loader.className = "bg-gray-200 text-sm p-2 rounded-full w-fit animate-pulse";
    loader.innerText = "Typing...";
    chat.appendChild(loader);

    chat.scrollTop = chat.scrollHeight;

    setTimeout(() => {
        loader.remove();

        chat.innerHTML += `
            <div class="bg-gray-200 text-sm p-2 rounded-full rounded-tl-none w-fit">
                I will get back to you soon!
            </div>
        `;

        chat.scrollTop = chat.scrollHeight;
    }, 1200);
}
