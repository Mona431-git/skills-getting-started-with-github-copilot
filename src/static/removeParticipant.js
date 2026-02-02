document.addEventListener('click', (event) => {
  if (event.target.classList.contains('remove-participant')) {
    const participant = event.target.getAttribute('data-participant');
    // Logic to remove participant goes here
    console.log(`Removing participant: ${participant}`);
    // You can add a fetch call to remove the participant from the server if needed
  }
});