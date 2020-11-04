const form = document.getElementById('form');

form.addEventListener('submit', function (e) {
    e.preventDefault()
    const data = {id: extractId(), title: form.elements['title'].value};
    fetch(LIST_UPDATE_URL, initRequestConfig('PUT', data))
        .then(response => response.json())
        .then(() => window.history.back());
});
