const togglePassword = () => {
  const passwordInput = document.getElementById("password");
  const showPasswordButton = document.getElementById("showPasswordButton");
  
  const isPasswordVisible = passwordInput.type === "text";

  passwordInput.type = isPasswordVisible ? "password" : "text";
  showPasswordButton.innerHTML = isPasswordVisible ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
};
