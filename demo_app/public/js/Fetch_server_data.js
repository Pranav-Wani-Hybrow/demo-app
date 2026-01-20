async function student_data(frm) {
    try {
        const response = await fetch(
            "http://127.0.0.1:8001/api/resource/Student%20Data/Hello-Pranav%20Wani",
            {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );

        const jsonData = await response.json();
        console.log(jsonData);

        return jsonData;

    } catch (error) {
        console.error("Error fetching data:", error);
        return null;
    }
}