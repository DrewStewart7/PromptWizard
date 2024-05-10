document.getElementById('darkMode').addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');
});


document.getElementById('myButton').addEventListener('click', function(event) {
    event.preventDefault();
    this.style.animation = 'none';
    this.offsetHeight; /* trigger reflow */
    this.style.animation = 'bounce 0.5s linear'; 
});

document.getElementById('myButton').addEventListener('click', function(event) {
    event.preventDefault();

    var promptText = document.getElementById('original-prompt').value;

    if (promptText.trim() !== '') {
        // Show spinner and disable button
        document.getElementById('spinner').style.display = 'block';
        this.disabled = true;
        document.getElementById('enhanced-prompt').textContent = "";

        fetch('http://127.0.0.1:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({prompt: promptText}),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('enhanced-prompt').textContent = data.prompt;

            // Hide spinner and enable button
            document.getElementById('spinner').style.display = 'none';
            this.disabled = false;
        })
        .catch((error) => {
            console.error('Error:', error);

            // Hide spinner and enable button
            document.getElementById('spinner').style.display = 'none';
            this.disabled = false;
        });
    }
});