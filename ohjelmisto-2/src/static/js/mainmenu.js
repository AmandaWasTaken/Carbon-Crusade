
const username = localStorage.getItem('username');


function checkAuth() {
    if (!username) {
        window.location.href = '/';
        return false;
    }
    return true;
}

async function startGame() {
    if (!checkAuth()) return;

    try {
        const response = await fetch('/api/game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                action: 'start_game',
                user: username
            })
        });

        const data = await response.json();
        if (data.success) {
            showDifficultySelection();
        } else {
            showMessage(data.message, 'error');
        }
    } catch (error) {
        showMessage('Error starting game', 'error');
    }
}

async function showHighScores() {
    if (!checkAuth()) return;

    try {
        const response = await fetch('/api/highscores');
        const data = await response.json();

        if (data.success) {
            displayHighScores(data.scores);
        } else {
            showMessage('Error loading high scores', 'error');
        }
    } catch (error) {
        showMessage('Error loading high scores', 'error');
    }
}

async function showCredits() {
    const credits = [
        "JUHO MOLIN",
        "TEPPO TOROPAINEN",
        "ATTE STEN",
        "AMANDA SANDELL",
        "JERE PUNNONEN"
    ];

    const creditsHtml = `
        <div class="credits-container">
            <h2>CREDITS</h2>
            ${credits.map(name => `<div class="credit-item">${name}</div>`).join('')}
            <button class="menu-button" onclick="hideCredits()">Back</button>
        </div>
    `;

    document.querySelector('.menu-options').style.display = 'none';
    document.getElementById('messageArea').innerHTML = creditsHtml;
}

function hideCredits() {
    document.querySelector('.menu-options').style.display = 'flex';
    document.getElementById('messageArea').innerHTML = '';
}

function showDifficultySelection() {
    const difficultyHtml = `
        <div class="difficulty-container">
            <h2>Select Difficulty</h2>
            <button class="menu-button" onclick="startGameWithDifficulty(1)">HELPPO</button>
            <button class="menu-button" onclick="startGameWithDifficulty(2)">NORMAALI</button>
            <button class="menu-button" onclick="startGameWithDifficulty(3)">VAIKEA</button>
            <button class="menu-button" onclick="hideDifficultySelection()">Back</button>
        </div>
    `;

    document.querySelector('.menu-options').style.display = 'none';
    document.getElementById('messageArea').innerHTML = difficultyHtml;
}

function hideDifficultySelection() {
    document.querySelector('.menu-options').style.display = 'flex';
    document.getElementById('messageArea').innerHTML = '';
}

async function startGameWithDifficulty(difficulty) {
    try {
        const response = await fetch('/api/game/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user: username,
                difficulty: difficulty
            })
        });

        const data = await response.json();
        if (data.success) {
            showMessage('Starting game...', 'success');
            // game logic
        } else {
            showMessage(data.message, 'error');
        }
    } catch (error) {
        showMessage('Error starting game', 'error');
    }
}

function displayHighScores(scores) {
    const scoresHtml = `
        <div class="highscores-container">
            <h2>High Scores</h2>
            <div class="scores-list">
                ${scores.map((score, index) => `
                    <div class="score-item">
                        ${index + 1}. ${score.screen_name}: ${score.highscore}
                    </div>
                `).join('')}
            </div>
            <button class="menu-button" onclick="hideHighScores()">Back</button>
        </div>
    `;

    document.querySelector('.menu-options').style.display = 'none';
    document.getElementById('messageArea').innerHTML = scoresHtml;
}

function hideHighScores() {
    document.querySelector('.menu-options').style.display = 'flex';
    document.getElementById('messageArea').innerHTML = '';
}

function showMessage(message, type) {
    const messageArea = document.getElementById('messageArea');
    messageArea.textContent = message;
    messageArea.className = `message-area ${type}`;
}

function logout() {
    localStorage.removeItem('username');
    window.location.href = '/';
}


document.addEventListener('DOMContentLoaded', checkAuth);