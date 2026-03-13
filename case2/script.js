let counter = 0;

// Элементы DOM
const counterDisplay = document.getElementById('counterDisplay');
const incrementBtn = document.getElementById('incrementBtn');
const decrementBtn = document.getElementById('decrementBtn');
const extremeMessage = document.getElementById('extremeMessage');

// Функция обновления отображения счётчика
function updateCounterDisplay() {
    counterDisplay.textContent = counter;

    // Изменение фона в зависимости от значения
    if (counter > 0) {
        counterDisplay.style.backgroundColor = 'yellow';
        counterDisplay.style.color = 'black';
    } else if (counter < 0) {
        counterDisplay.style.backgroundColor = 'green';
        counterDisplay.style.color = 'white';
    } else {
        counterDisplay.style.backgroundColor = 'red';
        counterDisplay.style.color = 'white';
    }

    // Активация/деактивация кнопок
    incrementBtn.disabled = counter >= 10;
    decrementBtn.disabled = counter <= -10;

    // Отображение сообщения о достижении экстремальных значений
    if (counter === 10 || counter === -10) {
        extremeMessage.textContent = 'Вы достигли экстремального значения';
    } else {
        extremeMessage.textContent = '';
    }
}

// Обработчики событий для кнопок
incrementBtn.addEventListener('click', () => {
    if (counter < 10) {
        counter++;
        updateCounterDisplay();
    }
});

decrementBtn.addEventListener('click', () => {
    if (counter > -10) {
        counter--;
        updateCounterDisplay();
    }
});

// Инициализация при загрузке страницы
updateCounterDisplay();
