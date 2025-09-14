let count = 0;

document.getElementById("increaseBtn").addEventListener("click", () => {
  count++;
  document.getElementById("counter").textContent = count;
});

document.getElementById("resetBtn").addEventListener("click", () => {
  count = 0;
  document.getElementById("counter").textContent = count;
});
