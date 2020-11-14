function showResult(str) {
    if (str.length === 0) {
 //       document.getElementById("conversation-list").style.display = "block";
        Array.from(document.getElementById("conversation-list").children).forEach(e => e.style.display = "grid");

    } else {
        Array.from(document.getElementById("conversation-list").children).forEach(e => {
            console.log(e.id);
            if (e.id == null) return;
            if (e.id.toLowerCase().includes(str.toLowerCase())) {
                e.style.display = "grid";

            } else {
                e.style.display = "none";
            }

        });
//        document.getElementById("conversation-list").style.display = "none";
    }
}