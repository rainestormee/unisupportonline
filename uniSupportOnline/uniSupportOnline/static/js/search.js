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
    const urlParams = new URLSearchParams(window.location.search);
    let found = false;
    let foo = 2;
    urlParams.forEach((k, v) => {
        console.log(k, v);
        if (v === 'foo') {
            found = true;
            foo = k;
        }
    })
    if (!found) {
        return;
    }

    this.getConversations().forEach(c => {
        if (c.id === foo) {
            c.classList.add("active");
        } else {
            c.classList.remove("active");
        }
    });
}

function switchChatMessage(name, id) {
    name = unescape(name)
    this.getConversations().forEach(e => {
        if (e.id === name) {
            e.classList.add("active")
        } else {
            e.classList.remove("active")
        }
    });
    window.location.assign("/help?foo=" + id,true);
}

function getConversations() {
    return Array.from(document.getElementById("conversation-list").children).filter(e => (e != null && e.id != null));
}