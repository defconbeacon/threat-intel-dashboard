const socket = io();

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('new_threat', (data) => {
    const feed = document.getElementById('threat-feed');
    const div = document.createElement('div');
    div.className = 'threat';
    div.innerHTML = `
        <strong>Type:</strong> ${data.type}<br>
        <strong>Value:</strong> ${data.value}<br>
        <strong>Source:</strong> ${data.source}<br>
        <small>${new Date().toLocaleTimeString()}</small>
    `;
    feed.prepend(div);
});
