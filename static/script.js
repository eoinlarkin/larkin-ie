const checkbox = document.querySelector("#dark-mode-toggle");
const html = document.querySelector("html");

const toggleDarkMode = function () {
  checkbox.checked
  ? html.classList.add("dark")
  : html.classList.remove("dark");
}

//calling the function directly
toggleDarkMode();
checkbox.addEventListener("click",toggleDarkMode);
