const wrapper = document.getElementById('wrapper');

function render(tasks) {
    tasks.map(t => wrapper.appendChild(wrapper))
}

 // <div style="display: flex; justify-content: space-between; margin: 8px; width: 25%">
 //            <p style="color: red;">{{ task.title }}</p>
 //            <button id="update_task">Update</button>
 //        </div>

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