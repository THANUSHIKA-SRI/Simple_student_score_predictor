async function predictScore() {
    const hours = document.getElementById("hours").value;
    const attendance = document.getElementById("attendance").value;
    const resultDiv = document.getElementById("result");

    resultDiv.innerText = "Predicting...";

    try {
        const response = await fetch(
            "https://simple-student-score-predictor.onrender.com/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    hours_studied: Number(hours),
                    attendance: Number(attendance)
                })
            }
        );

        if (!response.ok) {
            throw new Error("Server returned " + response.status);
        }

        const result = await response.json();

        resultDiv.innerText =
            "Predicted Score: " + result.predicted_score;

    } catch (error) {
        console.error(error);
        resultDiv.innerText =
            "Error: " + error.message;
    }
}