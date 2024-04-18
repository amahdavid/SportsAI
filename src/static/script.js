document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("prompt-form");
    const promptInput = document.getElementById("prompt");
    const responseContainer = document.getElementById("response");
  
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const prompt = promptInput.value.trim();
      if (!prompt) return;
  
      // Create a new XMLHttpRequest object
      const xhr = new XMLHttpRequest();
  
      // Configure the request
      xhr.open("POST", "http://localhost:8000/query");
      xhr.setRequestHeader("Content-Type", "application/json");
  
      // Define the behavior for when the request is complete
      xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            const responseData = JSON.parse(xhr.responseText);
            responseContainer.textContent = responseData.result;
          } else {
            console.error("Failed to fetch response from the server");
            responseContainer.textContent =
              "An error occurred. Please try again later.";
          }
        }
      };
  
      // Send the request with the prompt as JSON
      xhr.send(JSON.stringify({ prompt }));
  
      // Display loading message while waiting for response
      responseContainer.textContent = "Loading...";
    });
  });
  