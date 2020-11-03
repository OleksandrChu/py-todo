const form = document.getElementById('form');
let input = form.elements['title'].value;

form.addEventListener('submit', function (e) {
    e.preventDefault()
    const data = {id: extractId(), title: form.elements['title'].value};
    fetch(`http://127.0.0.1:8000/list/update/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => console.log(data));
});

function extractId() {
    const url = window.location.href;
    return parseInt(url
        .substring(url.lastIndexOf('/') - 1)
        .slice(0, -1));
}