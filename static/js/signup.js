
function updateFileName() {
  const fileInput = document.getElementById('profile_picture');
  const fileNameSpan = document.getElementById('file-name');

  if (fileInput.files.length > 0) {
    fileNameSpan.textContent = fileInput.files[0].name;
  } else {
    fileNameSpan.textContent = '';
  }
}
