function showResult(str) {
    if (str.length === 0) {
        this.getConversations().forEach(e => e.style.visibility = "visible");
    } else {
        this.getConversations().forEach(e => {
            if (e.id.toLowerCase().includes(str.toLowerCase())) {
                e.style.visibility = "visible";
            } else {
                e.style.visibility = "hidden";
            }
        });
    }
}

function activateFirst() {
    this.getConversations()[0].classList.add("active");
}

function switchChatMessage(name) {
    this.getConversations().forEach(e => {
        if (e.id === name) {
            e.classList.add("active")
        } else {
            e.classList.remove("active")
        }
    });
}

function getConversations() {
    return Array.from(document.getElementById("conversation-list").children).filter(e => (e != null && e.id != null));
}