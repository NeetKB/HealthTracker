// Get the toggle button and the <html> element
const toggleButton = document.getElementById("dark-mode-toggle");
const htmlElement = document.documentElement;

// Check if dark mode is already applied by checking the class on <html> element
const isDarkMode = localStorage.getItem("darkMode") === "true";

// Apply dark mode class if dark mode is enabled
if (isDarkMode) {
  htmlElement.classList.add("dark");
  toggleButton.textContent = "Switch to Light Mode"; // Change button text
} else {
  toggleButton.textContent = "Switch to Dark Mode"; // Default text
}

// Toggle dark mode when button is clicked
toggleButton.addEventListener("click", () => {
  // Toggle the dark mode class on the <html> element
  htmlElement.classList.toggle("dark");

  // Store the user's preference in localStorage
  const darkModeEnabled = htmlElement.classList.contains("dark");
  localStorage.setItem("darkMode", darkModeEnabled);

  // Change the button text based on the current mode
  if (darkModeEnabled) {
    toggleButton.textContent = "Switch to Light Mode"; // Button text for Dark Mode
  } else {
    toggleButton.textContent = "Switch to Dark Mode"; // Button text for Light Mode
  }
});
