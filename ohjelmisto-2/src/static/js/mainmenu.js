document.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    if (username) {
        document.getElementById('username').textContent = username;
    }

    loadHighScores();
});

async function loadHighScores() {
    try {
        const response = await fetch('/get_high_scores');
        const scores = await response.json();

        const tbody = document.getElementById('highScoresBody');
        tbody.innerHTML = '';

        scores.forEach((score, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${score.screen_name}</td>
                <td>${score.highscore.slice(0, -2)}</td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading high scores:', error);
    }
}

function toggleHighScores() {
    const section = document.getElementById('highScoresSection');
    if (section.style.display === 'none') {
        section.style.display = 'block';
        loadHighScores();
    } else {
        section.style.display = 'none';
    }
}

function showDifficultySelector() {
    const modal = document.getElementById('difficultyModal');
    modal.style.display = 'flex';
}

function closeDifficultyModal() {
    const modal = document.getElementById('difficultyModal');
    modal.style.display = 'none';
}

function startGame(difficulty) {
    localStorage.setItem('gameDifficulty', difficulty);
    window.location.href = '/play';
}

function showCredits() {
    const modal = document.getElementById('creditsModal');
    modal.style.display = 'flex';
}

function closeCreditsModal() {
    const modal = document.getElementById('creditsModal');
    modal.style.display = 'none';
}

function closeGame() {
    const confirmClose = confirm("Are you sure you want to exit the game?");
    if (confirmClose) {
        window.close();
        setTimeout(() => {
            window.location.href = '/';
        }, 100);
    }
}


window.onclick = function(event) {
    const difficultyModal = document.getElementById('difficultyModal');
    const creditsModal = document.getElementById('creditsModal');
    if (event.target === difficultyModal) {
        difficultyModal.style.display = 'none';
    }
    if (event.target === creditsModal) {
        creditsModal.style.display = 'none';
    }
}