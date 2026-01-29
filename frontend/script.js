const API_BASE = "http://127.0.0.1:8000";

let currentDocumentId = null;


async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const status = document.getElementById("uploadStatus");

  if (!fileInput.files.length) {
    status.innerText = "❌ Please select a file first.";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  status.innerText = "⏳ Uploading...";

  try {
    const res = await fetch(`${API_BASE}/upload`, {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    console.log("UPLOAD RESPONSE:", data);

    if (!data.document_id) {
      throw new Error("document_id missing from backend");
    }

    currentDocumentId = data.document_id;
    status.innerText = "✅ Document uploaded successfully!";

  } catch (err) {
    console.error(err);
    status.innerText = "❌ Upload failed.";
  }
}


async function askQuestion() {
  const question = document.getElementById("question").value;
  const answerBox = document.getElementById("answer");

  if (!currentDocumentId) {
    answerBox.innerText = "❌ Please upload a document first.";
    return;
  }

  if (!question.trim()) {
    answerBox.innerText = "❌ Enter a question.";
    return;
  }

  answerBox.innerText = "⏳ Generating answer...";

  try {
    const res = await fetch(`${API_BASE}/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        document_id: currentDocumentId,
        question: question
      })
    });

    const data = await res.json();
    answerBox.innerText = data.answer || "No answer found.";

  } catch (err) {
    console.error(err);
    answerBox.innerText = "❌ Error getting answer.";
  }
}
