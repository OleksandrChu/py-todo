const form = document.getElementById('form');

form.addEventListener('submit', function (e) {
    e.preventDefault()
    const data = {id: extractId(), title: form.elements['title'].value};
    fetch(LIST_UPDATE_URL, initRequestConfig('PUT', data))
        .then(response => response.json())
        .then(data => console.log(data));
});

function extractId() {
    const url = window.location.href;
    return parseInt(url
        .substring(url.lastIndexOf('/') - 1)
        .slice(0, -1));
}

function initRequestConfig(method = 'GET', data = {}) {
    return {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }
}