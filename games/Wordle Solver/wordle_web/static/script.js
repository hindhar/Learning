function makeGuess() {
    const guess = document.getElementById('guess-input').value.toLowerCase();

    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ guess: guess }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('feedback').innerText = data.feedback;
    });
}
