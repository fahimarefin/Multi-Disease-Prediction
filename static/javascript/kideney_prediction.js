$(document).ready(function () {
    $('#uploadForm').submit(function (e) {
        e.preventDefault();  // Prevent the default form submission

        console.log("Function called");  // Debugging statement

        var form = new FormData(this);

        // Debugging statement to check CSRF token
        console.log("CSRF Token:", $('input[name=csrfmiddlewaretoken]').val());

        form.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());

        $.ajax({
            type: 'POST',
            url: '/kidney_prediction/',
            data: form,
            processData: false,
            contentType: false,
            success: function (response) {
                $("#result").text("Predicted Class: " + response.predicted_class);
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
                $("#result").text("Error predicting kidney: " + xhr.responseText);
            }
        });
    });
});
