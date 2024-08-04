function clearInput(inputId) {
  document.getElementById(inputId).value = '';
}

async function transformCode() {
  const activeTab = document.querySelector('.tab.active').textContent.toLowerCase();
  const input = document.getElementById(`${activeTab}Input`).value;
  const library = document.querySelector('input[name="library"]:checked').value;

  const data = {
    request_type: activeTab,
    target: library,
    data_str: input.replace(/\n/g, ' ').trim()
  };

  try {
    const response = await fetch('/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const result = await response.json();
    const resultElement = document.getElementById('result');
    resultElement.textContent = result.request_string;

    document.getElementById('copyButton').style.display = 'block';
  } catch (error) {
    console.error('Error:', error);
    document.getElementById('result').textContent = 'An error occurred while processing your request.';
  }
}

function copyResult() {
  const resultText = document.getElementById('result').textContent;
  navigator.clipboard.writeText(resultText).then(() => {
    const notification = document.getElementById('copyNotification');
    notification.style.display = 'block';
    setTimeout(() => {
      notification.style.display = 'none';
    }, 2000);
  });
}
