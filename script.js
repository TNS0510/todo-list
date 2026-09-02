// DOM Element References
const taskInput = document.getElementById('task-input');
const addBtn = document.getElementById('add-btn');
const taskList = document.getElementById('task-list');

// Load initial tasks from LocalStorage or default to empty array
let tasks = JSON.parse(localStorage.getItem('web_tasks')) || [];

/**
 * Saves current tasks array to browser LocalStorage.
 */
function saveTasks() {
    localStorage.setItem('web_tasks', JSON.stringify(tasks));
}

/**
 * Renders task items dynamically inside the HTML task-list container.
 */
function renderTasks() {
    taskList.innerHTML = '';

    if (tasks.length === 0) {
        taskList.innerHTML = '<li style="justify-content: center; color: #a6adc8;">No tasks yet! Add one above.</li>';
        return;
    }

    tasks.forEach(task => {
        const li = document.createElement('li');
        if (task.completed) {
            li.classList.add('completed');
        }

        // Task title text
        const titleSpan = document.createElement('span');
        titleSpan.textContent = task.title;

        // Action buttons container
        const actionsDiv = document.createElement('div');
        actionsDiv.className = 'actions';

        // Toggle Complete Button
        const completeBtn = document.createElement('button');
        completeBtn.className = 'action-btn';
        completeBtn.innerHTML = task.completed ? '↩️' : '✅';
        completeBtn.title = task.completed ? 'Mark Pending' : 'Mark Complete';
        completeBtn.addEventListener('click', () => toggleTask(task.id));

        // Delete Button
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'action-btn';
        deleteBtn.innerHTML = '🗑️';
        deleteBtn.title = 'Delete Task';
        deleteBtn.addEventListener('click', () => deleteTask(task.id));

        actionsDiv.appendChild(completeBtn);
        actionsDiv.appendChild(deleteBtn);

        li.appendChild(titleSpan);
        li.appendChild(actionsDiv);

        taskList.appendChild(li);
    });
}

/**
 * Adds a new task to the array and re-renders the UI.
 */
function addTask() {
    const title = taskInput.value.trim();
    if (!title) return;

    const newTask = {
        id: Date.now(), // Unique numeric timestamp ID
        title: title,
        completed: false
    };

    tasks.push(newTask);
    saveTasks();
    renderTasks();
    taskInput.value = '';
}

/**
 * Toggles completed status for a given task ID.
 */
function toggleTask(id) {
    tasks = tasks.map(task => {
        if (task.id === id) {
            return { ...task, completed: !task.completed };
        }
        return task;
    });
    saveTasks();
    renderTasks();
}

/**
 * Removes a task by ID from the list.
 */
function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    renderTasks();
}

// Event Listeners
addBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTask();
});

// Initial Render on Page Load
renderTasks();