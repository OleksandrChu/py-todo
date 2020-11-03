const form = document.getElementById('form');
form.addEventListener('submit', function (e) {
    e.preventDefault()
    const data = {title: 'example2123'};
    fetch('http://127.0.0.1:8000/api/list/update/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }).then(response => response.json())
        .then(data => console.log(data));
});