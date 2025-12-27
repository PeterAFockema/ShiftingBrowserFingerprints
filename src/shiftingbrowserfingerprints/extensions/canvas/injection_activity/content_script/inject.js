window.addEventListener("message", function(e) {
    if (e.data && e.data === "canvas_intercept") {
        e.preventDefault()
        e.stopPropagation()
    }
}, false);