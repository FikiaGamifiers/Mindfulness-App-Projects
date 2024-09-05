console.log("Calculator script is connected!");

// Select the display element
const display = document.getElementById('result');

// Select all the buttons
const buttons = document.querySelectorAll('button');

// Create a variable to keep track of the current input
let currentInput = '';

let lastInput = '';

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.textContent;

        // Handle Clear button
        if (value === 'C') {
            currentInput = '';
            display.value = '';
            lastInput = '';
        }
        // Handle Equal button
        else if (value === '=') {
            try {
                currentInput = eval(currentInput);
                display.value = currentInput;
                lastInput = '';
            } catch (error) {
                display.value = 'Error';
                currentInput = '';
            }
        }
        // Handle numbers and decimal points
        else if (!isNaN(value) || value === '.') {
            if (value === '.' && lastInput === '.') {
                // Prevent multiple decimals
                return;
            }

            currentInput += value;
            display.value = currentInput;
            lastInput = value;
        }
        // Handle operators
        else {
            if (['+', '-', '*', '/'].includes(lastInput)) {
                // Prevent multiple operators in a row
                return;
            }

            currentInput += value;
            display.value = currentInput;
            lastInput = value;
        }
    });
});

// Handle keypress events for keyboard support
document.addEventListener('DOMContentLoaded', () => {
    const equalsButton = document.querySelector('button[onclick="calculate()"]');
    
    equalsButton.addEventListener('click', () => {
        equalsButton.classList.add('clicked');
        
        // Remove the class after the animation ends to reset
        setTimeout(() => {
            equalsButton.classList.remove('clicked');
        }, 500); // Match the duration of the transition
    });
});

// Simulate button click based on the key pressed
function simulateButtonClick(key) {
    buttons.forEach(button => {
        if (button.textContent === key || (key === 'Enter' && button.textContent === '=')) {
            button.click();
        } else if ((key === 'Backspace' || key === 'Delete') && button.textContent === 'C') {
            button.click();
        }
    });
}

// Theme toggle logic
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('change', () => {
    if (themeToggle.checked) {
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
    }
});
