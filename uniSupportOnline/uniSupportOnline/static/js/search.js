function showResult(str) {
    if (str.length === 0) {
        this.getConversations().forEach(e => {
            e.style.visibility = "visible";
            e.style.display = "grid";
        });
    } else {
        const len = this.getConversations().filter(e => e.id.toLowerCase().includes(str.toLowerCase())).length;

        this.getConversations().forEach(e => {
            if (e.id.toLowerCase().includes(str.toLowerCase())) {
                e.style.visibility = "visible";
                e.style.display = "grid";
            } else {
                if (len === 0) {
                    e.style.visibility = "hidden";
                } else {
                    e.style.display = "none";
                }
            }
        });
    }
}

function activateFirst() {
    console.log("i want to die");
    this.getConversations().get(0).classList.add("active");
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