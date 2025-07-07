document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const resultBox = document.getElementById("result");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const selectedModel = document.getElementById("model").value;
    const userPrompt = document.getElementById("prompt").value;

    const response = await fetch("/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: selectedModel,
        prompt: userPrompt
      })
    });

    const data = await response.json();
    if (data.response) {
      resultBox.innerText = data.response;
    } else if (data.error) {
      resultBox.innerText = `Error: ${data.error}`;
    } else {
      resultBox.innerText = "Unknown error occurred.";
    }
  });
});

  