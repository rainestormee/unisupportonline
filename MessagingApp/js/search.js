function showResult(str) {
    if (str.length === 0) {
        this.getConversations().forEach(e => e.style.display = "grid");
    } else {
        this.getConversations().forEach(e => {
            if (e.id.toLowerCase().includes(str.toLowerCase())) {
                e.style.display = "grid";
            } else {
                e.style.display = "none";
            }
        });
    }
}

function switchChatMessage(name) {
    this.getConversations().forEach(e => {
        if (e.id === name) {
            e.class = "conversation active";
            console.log(e.id);
        } else {
            e.class = "conversation";
        }
    });
}

function getConversations() {
    return Array.from(document.getElementById("conversation-list").children).filter(e => (e != null && e.id != null));
}