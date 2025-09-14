let count = 0;

const counterDisplay = document.getElementById("counter");
const incrementBtn = document.getElementById("incrementBtn");
const decrementBtn = document.getElementById("decrementBtn");
const resetBtn = document.getElementById("resetBtn");

// Update counter display
function updateCounter() {
  counterDisplay.textContent = count;
}

// Increment
incrementBtn.addEventListener("click", () => {
  count++;
  updateCounter();
});

// Decrement
decrementBtn.addEventListener("click", () => {
  count--;
  updateCounter();
});

// Reset
resetBtn.addEventListener("click", () => {
  count = 0;
  updateCounter();
});
