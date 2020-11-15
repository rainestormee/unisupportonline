function showResult(str) {
    if (str.length === 0) {
        this.getConversations().forEach(e => {
            e.style.visibility = "visible";
            e.style.display = "grid";
        });
    } else {
        const len = this.getConversations().filter(e => e.id.toLowerCase().includes(str.toLowerCase())).length;
        this.getConversations().forEach(e => {
            if (unescape(e.id.toLowerCase()).includes(str.toLowerCase())) {
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

window.onload = function() {
    this.getConversations()[0].classList.add("active");
}

function switchChatMessage(name) {
    name = unescape(name)
    this.getConversations().forEach(e => {
        if (e.id === name) {
            e.classList.add("active")
        } else {
            e.classList.remove("active")
        }
    });
    window.location.assign("/help?foo=" + name,true);
}

function getConversations() {
    return Array.from(document.getElementById("conversation-list").children).filter(e => (e != null && e.id != null));
}