document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("prompt-form");
  const promptInput = document.getElementById("prompt");
  const responseContainer = document.getElementById("response");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const prompt = promptInput.value.trim();
    if (!prompt) return;

    try {
      const response = await fetch("http://your-backend-url/api/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch response from the server");
      }

      const responseData = await response.json();
      responseContainer.textContent = responseData.result;
    } catch (error) {
      console.error("Error:", error);
      responseContainer.textContent =
        "An error occurred. Please try again later.";
    }
  });
});
