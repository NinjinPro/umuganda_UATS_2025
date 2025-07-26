async function apiRequest(url, method = "GET", data = null, headers = {}) {
    const defaultHeaders = {
        "Content-Type": "application/json",
        ...headers
    };

    const options = {
        method: method.toUpperCase(),
        headers: defaultHeaders,
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(url, options);
        const contentType = response.headers.get("content-type");
        const responseData = contentType && contentType.includes("application/json")
            ? await response.json()
            : await response.text();

        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${JSON.stringify(responseData)}`);
        }

        return responseData;
    } catch (error) {
        console.error("API Request Failed:", error);
        throw error;
    }
}
