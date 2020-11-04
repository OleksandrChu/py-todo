const form = document.getElementById('form');
const checkbox = document.getElementById('done');

form.addEventListener('submit', ev =>  {
    ev.preventDefault()
    const data = {list_id: extractId(), title: form.elements['title'].value};
    fetch(TASK_CREATE_URL, initRequestConfig('POST', data))
        .then(response => response.json())
        .then(data => {
            console.log(data)});
});
