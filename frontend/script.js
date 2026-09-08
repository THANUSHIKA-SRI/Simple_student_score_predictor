async function predictScore() {

    // Get values from the input boxes
    const hours = document.getElementById("hours").value;
    const attendance = document.getElementById("attendance").value;

    // Send data to FastAPI
    const response = await fetch("https://simple-student-score-predictor.onrender.com/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            hours_studied: Number(hours),
            attendance: Number(attendance)
        })
    });

    // Get prediction from API
    const result = await response.json();

    // Display prediction
    document.getElementById("result").innerText =
        "Predicted Score: " + result.predicted_score;
}