const wrapper = document.getElementById('wrapper');

function render(tasks) {
    tasks.map(t => wrapper.appendChild(template(t)))
}

function template(task) {
    const div = document.createElement('div');
    const button = document.createElement('button');
    const title = document.createElement('p');
    button.innerText = 'Update'
    button.addEventListener('click', (e) => {
        console.log(task.id)
    })
    div.appendChild(button);
    div.appendChild(title);
    return div;
}
